#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/16.

import pymongo

from ..items import Book, BookInfo


class MongoPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.books = {}

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'books')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db.drop_collection("BookInfo")
        self.db.drop_collection("Book")

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if isinstance(item, Book):
            book_id = self.db[item.__class__.__name__].insert(dict(item))
            self.books[spider.start_urls[0]] = book_id
        if isinstance(item, BookInfo):
            item['book_id'] = self.books.get(spider.start_urls[0], 0)
            self.db[item.__class__.__name__].insert(dict(item))
        return item
