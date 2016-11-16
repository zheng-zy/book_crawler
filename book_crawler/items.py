# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    book_author = scrapy.Field()
    book_desc = scrapy.Field()

    book_id = scrapy.Field()
    book_chapter = scrapy.Field()
    book_chapter_url = scrapy.Field()
    book_context = scrapy.Field()
    create_time = scrapy.Field()


class BookInfo(scrapy.Item):
    # define the fields for your item here like:
    book_id = scrapy.Field()
    book_chapter = scrapy.Field()
    book_chapter_url = scrapy.Field()
    book_content = scrapy.Field()
    create_time = scrapy.Field()
