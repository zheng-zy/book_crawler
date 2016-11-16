#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/16.

import pymongo

connection = pymongo.MongoClient('192.168.97.120')
tdb = connection.book_crawler
db_test = tdb.test

jike = {'name': u'极客', 'age': '5', 'skill': 'Python'}
god = {'name': u'玉皇大帝', 'age': 36000, 'skill': 'creatanything', 'other': u'王母娘娘不是他的老婆'}
godslaver = {'name': u'月老', 'age': 'unknown', 'other': u'他的老婆叫孟婆'}
# db_test.insert(jike)
# db_test.insert(god)
# db_test.insert(godslaver)
# db_test.remove({'name': u'极客'})
import datetime
from bson.objectid import ObjectId

data_list = [{'book_chapter': u'\u7b2c\u4e24\u767e\u516b\u5341\u56db\u7ae0 \u4e00\u4e07\u4e09\u5343\u9897',
              'book_chapter_url': u'http://www.biquge.com/0_176/1260511.html',
              'book_id': ObjectId('582c412bd77ab32b04b05989'),
              'create_time': datetime.datetime(2016, 11, 16, 19, 21, 16, 9000)},
             {'book_chapter': u'\u7b2c\u4e09\u767e\u4e5d\u5341\u516b\u7ae0 \u9f99\u86c7\u6df7\u6742',
              'book_chapter_url': u'http://www.biquge.com/0_176/1269258.html',
              'book_id': ObjectId('582c412bd77ab32b04b05989'),
              'create_time': datetime.datetime(2016, 11, 16, 19, 21, 16, 25000)},
             {'book_chapter': u'\u7b2c\u4e5d\u767e\u56db\u5341\u4e94\u7ae0 \u7075\u795e\u6db2\u6210\u5f62!',
              'book_chapter_url': u'http://www.biquge.com/0_176/1341639.html',
              'book_id': ObjectId('582c412bd77ab32b04b05989'),
              'create_time': datetime.datetime(2016, 11, 16, 19, 21, 16, 98000)}]
db_test.insert(data_list)

print u'操作数据库完成！'
