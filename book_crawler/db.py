#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/16.

import pymongo

connection = pymongo.MongoClient('192.168.97.120')
tdb = connection.book_crawler
db_book = tdb.book
db_book_info = tdb.book_info

# jike = {'name': u'极客', 'age': '5', 'skill': 'Python'}
# god = {'name': u'玉皇大帝', 'age': 36000, 'skill': 'creatanything', 'other': u'王母娘娘不是他的老婆'}
# godslaver = {'name': u'月老', 'age': 'unknown', 'other': u'他的老婆叫孟婆'}
# post_info.insert(jike)
# post_info.insert(god)
# post_info.insert(godslaver)
# post_info.remove({'name': u'极客'})

print u'操作数据库完成！'
