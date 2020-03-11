---
title: Python 3.7创建Scrapy项目报错
date: 2018-10-27 21:30:32
tags: [python,scrapy,爬虫]
---
当我使用 *Python 3.7* 创建一个 *Scrapy* 爬虫程序后，在运行时报了很多错误信息，最后定位的错误如下：

    <module>
    from twisted.conch import manhole, telnet
    File "c:\python37\lib\site-packages\twisted\conch\manhole.py", line 154
    	def write(self, data, async=False):
                              ^
    SyntaxError: invalid syntax

可以看到是这个名为 **async** 的变量出错了，经过查询知道这个变量名在 *Python 3.7* 中被定义为了系统关键字，所以我们只需要在错误信息中写明的python文件中将该关键字重命名即可！
