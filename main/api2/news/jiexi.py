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
def about():
    url='http://news.nepu.edu.cn/news/155168791695864583.html'
    news=requests.get(url)
    if news.status_code != 200:
        return 404
    else:
        news=news.content
        beautifulsoup=bs4.BeautifulSoup
        soup=beautifulsoup(news,'html.parser')
        titles = soup.find_all('title')[0].string[:-20]
        authors = soup.select('.puber')[0].string
        departments = soup.select('.bm')[0].string
        times = soup.select('.pubtime')[0].string
        msgs = soup.find('div', id='xwcontentdisplay')
        text={
            'title':titles,
            'authors':authors,
            'departments':departments,
            'times':times,
            'msgs':msgs
        }
        print(text)

if __name__ == '__main__':

    about()