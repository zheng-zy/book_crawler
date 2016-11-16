#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/16.

from datetime import datetime

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

from ..db import tdb, db_book
from ..items import BookCrawlerItem, BookInfo

list_first_item = lambda x: x[0] if x else None


class BookSpider(scrapy.Spider):
    name = "biquge"
    # allowed_domains = ['biquge.com']
    start_urls = [
        "http://www.biquge.com/0_176/"
    ]
    prefix_url = 'http://www.biquge.com'

    def parse(self, response):
        tdb.book.remove()
        tdb.book_info.remove()

        selector = Selector(response)

        book = BookCrawlerItem()
        book['book_name'] = list_first_item(selector.xpath(u'//h1/text()')).extract()
        book['book_url'] = response.url
        div_info = selector.xpath(u'//div[@id="info"]/p/text()')
        # print div_info[0].extract().split(u'：')
        book['book_author'] = div_info[0].extract().split(u'：')[1].strip()
        div_intro = list_first_item(selector.xpath(u'//div[@id="intro"]/p/text()'))
        book['book_desc'] = div_intro.extract()
        # print dict(book)
        book_id = db_book.insert(dict(book))
        # book_id = yield book
        print 'book_id', book_id
        chapters = selector.xpath(u'//div[@id="list"]/dl/dd/a')
        # print list_first_item(chapters[0].xpath(u'text()')).extract()
        # print list_first_item(chapters[0].xpath(u'@href')).extract()
        chapter_dict = {}
        for chapter in chapters:
            book_info = BookInfo()
            book_info['book_id'] = book_id
            book_info['book_chapter'] = list_first_item(chapter.xpath(u'text()')).extract()
            book_info['book_chapter_url'] = self.prefix_url + list_first_item(chapter.xpath(u'@href')).extract()
            book_info['create_time'] = datetime.now()
            chapter_dict[book_info['book_chapter_url']] = dict(book_info)
            yield Request(url=book_info['book_chapter_url'], meta={'book_info': book_info},
                          callback=self.parse_detail)

    def parse_detail(self, response):
        book_info = response.meta['book_info']
        selector = Selector(response)
        contents = selector.xpath(u'//div[@id="content"]/text()')
        book_content = ''
        for content in contents:
            book_content += content.extract().strip()
        book_info['book_content'] = book_content
        yield book_info
        # db_book_info.insert(dict(book_info))
