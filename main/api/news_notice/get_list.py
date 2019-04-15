#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/3/4 22:40
@desc:
'''
import requests
from bs4 import BeautifulSoup


def nepu_news(page):
        data = {
            'scriptSessionId': '35414762109FC07BB0EC446FA567A77F4',
            'callCount': '1',
            'page': '/type/520202.html',
            'c0-scriptName': 'portalAjax',
            'c0-methodName': 'getNewsXml',
            'c0-id': '0',
            'c0-param0': 'string:5202',
            'c0-param1': 'string:520202',
            'c0-param2': 'string:news_',
            'c0-param3': 'number:20',
            'c0-param4': 'number:'+page,
            'c0-param5': 'null:null',
            'c0-param6': 'null:null',
            'batchId': '0'
        }
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '349',
            'Content-Type': 'text/plain',
            'Host': 'news.nepu.edu.cn',
            'Origin': 'http://news.nepu.edu.cn',
            'Referer': 'http://news.nepu.edu.cn/type/520202.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
        url = 'http://news.nepu.edu.cn/dwr/call/plaincall/portalAjax.getNewsXml.dwr'
        html = requests.post(url, data=data, headers=headers)
        if html.status_code != 200:#判断请求是否成功
            return 404
        else:
            get_news = html.content
            get_news = get_news.decode('unicode_escape')#编码
            soup = BeautifulSoup(get_news, 'html.parser')
            msg = soup.find_all('title', attrs={'name': ''})
            time = soup.select('link')
            t = soup.find_all('pubdate')
            bq = soup.find_all('lmmc')
            link = soup.find_all('guid')
            time_table = []
            for d in t:
                tm = d.string
                time_table.append(tm)
            table_link = []
            for c in link:
                dz = c.string
                table_link.append(dz)

            for b in bq:
                yw = b.string
            table = []
            for a in msg:
                title = a.string
                table.append(title)
            title_list = {}
            # for i in range(20):
            #     title_list = {(table[i], time_table[i]): table_link[i]}
            #     # print(title_list)
            #     print(title_list)
            get_title=[]
            for i in range(20):
                title_list={
                    'name':table[i],
                    'time':time_table[i],
                    'link':table_link[i]
                }
                get_title.append(title_list)
            print(get_title)

if __name__ == '__main__':
    nepu_news()

