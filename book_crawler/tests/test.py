#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/18.


html = '''<div id="list">
				<dl>
                    <dt>《大主宰》最新章节</b>（提示：已启用缓存技术，最新章节可能会延时显示，登录书架即可实时查看。）</dt>

                    <dd> <a href="/0_176/2507378.html">第一千三百六十二章 空间节点</a></dd>

                    <dd> <a href="/0_176/2507377.html">第一千三百六十一章 白龙机缘</a></dd>

                    <dd> <a href="/0_176/2507219.html">第一千三百六十章 天至尊之路</a></dd>

                    <dd> <a href="/0_176/2507132.html">第一千三百六十章 牧府扬威</a></dd>

                    <dd> <a href="/0_176/2506956.html">第一千三百五十九章 新晋霸主</a></dd>

                    <dd> <a href="/0_176/2506903.html">第一千三百五十八章 划分地盘</a></dd>

                    <dd> <a href="/0_176/2506141.html">第一千三百五十七章 八部浮屠显威</a></dd>

                    <dd> <a href="/0_176/2506083.html">第一千三百五十六章 临阵突破</a></dd>

                    <dd> <a href="/0_176/2505998.html">第一千三百五十五章 牧主战三霸</a></dd>



                    <dt>《大主宰》正文</dt>

                    <dd> <a href="/0_176/1228884.html">第一章 北灵院</a></dd>

                    <dd> <a href="/0_176/1228885.html">第二章 被踢出灵路的少年</a></dd>

                    <dd> <a href="/0_176/1228886.html">第三章 牧域</a></dd></dl></div>
'''

from scrapy.selector import Selector

sel = Selector(text=html, type="html")

list = sel.xpath('//div[@id="list"]')
for l in list:
    print l
