#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/17.
import re

from str2num import cn2dig

text = u"第十二章 北灵院"
cha = re.findall(ur'\u7b2c(.+?)\u7ae0', text)
if cha:
    for ch in cha:
        print ch
        print cn2dig(ch)
print cha

str = 'a123b'
print re.findall(r'a(.+?)b', str)
