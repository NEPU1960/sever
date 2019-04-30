#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/3/4 22:37
@desc:
'''
import requests
import bs4
import json
from ...comman import trueReturn,falseReturn
def about(url):
    '''新闻解析'''
    # url='http://news.nepu.edu.cn/news/155168791695864583.html'
    news=requests.get(url)
    if news.status_code != 200:
        # pass
        return falseReturn(msg='暂时不能访问')
    else:
        print(news.encoding)
        # news = news.text.encode('iso-8859-1')
        news=news.text.encode('iso-8859-1').decode('gb18030')
        # news=news.decode('utf-8')
        # print(news.encoding)
        # news=news.content
        beautifulsoup=bs4.BeautifulSoup
        soup=beautifulsoup(news,'html.parser')
        titles = soup.find_all('title')[0].string[:-20]
        authors = soup.select('.puber')[0].string
        departments = soup.select('.bm')[0].string
        times = soup.select('.pubtime')[0].string
        msgs = soup.find('div', id='xwcontentdisplay')
        msg=str(msgs)
        print(msg)
        # msg=msg.replace("\"","\'")
        text={
            'title':titles,
            'authors':authors,
            'departments':departments,
            'times':times,
            'text':msg
        }
        print(text)


        return trueReturn(data=text)


if __name__ == '__main__':

    about('http://news.nepu.edu.cn/news/155554849951452585.html')