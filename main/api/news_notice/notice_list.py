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
from operator import itemgetter, attrgetter

def nepu_notice(tag,page):
    get_title = []
    department={
        'home':['/type/520203.html','5202','520203','http://news.nepu.edu.cn/dwr/call/plaincall/portalAjax.getNewsXml.dwr'],
        'jw':['/jwc/type/350312.html','3503','350312','http://glbm1.nepu.edu.cn/jwc/dwr/call/plaincall/portalAjax.getNewsXml.dwr'],
        'yjs':['/yjsxy/typelist/170111.html','1701','170111','http://glbm3.nepu.edu.cn/yjsxy/dwr/call/plaincall/portalAjax.getNewsXml.dwr'],
        'xsy':['/xsy/typenews/190214.html','1902','190214','http://glbm1.nepu.edu.cn/xsy/dwr/call/plaincall/portalAjax.getNewsXml.dwr'],
        'tw':['/tw/type/390113.html','3901','390113','http://glbm2.nepu.edu.cn/tw/dwr/call/plaincall/portalAjax.getNewsXml.dwr']

    }
    for i in tag:
        # for pag in range(1,int(page)+1):
            data = {
                'httpSessionId':'825F0C3C97DF22F7F6037E8C01298AEE',
                'scriptSessionId': '35414762109FC07BB0EC446FA567A77F4',
                'callCount': '1',
                'page': department[i][0],
                'c0-scriptName': 'portalAjax',
                'c0-methodName': 'getNewsXml',
                'c0-id': '0',
                'c0-param0': 'string:'+department[i][1],
                'c0-param1': 'string:'+department[i][2],
                'c0-param2': 'string:news_',
                'c0-param3': 'number:15',
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
                'Content-Type': 'text/plain',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
            }
            url = 'http://news.nepu.edu.cn/dwr/call/plaincall/portalAjax.getNewsXml.dwr'
            jw_url='http://glbm1.nepu.edu.cn/jwc/dwr/call/plaincall/portalAjax.getNewsXml.dwr'
            html = requests.post(department[i][3], data=data, headers=headers)
            if html.status_code != 200:#判断请求是否成功
                return 404
            else:
                get_news = html.content
                get_news = get_news.decode('unicode_escape')#编码
                soup = BeautifulSoup(get_news, 'html.parser')
                #print(soup)
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
                #print(table)
                title_list = {}
                # for i in range(20):
                #     title_list = {(table[i], time_table[i]): table_link[i]}
                #     # print(title_list)
                #     print(title_list)

                for j in range(10):
                    title_list={
                        'name':table[j],
                        'time':time_table[j],
                        'link':table_link[j]
                    }
                    get_title.append(title_list)
    notice_list=sorted(get_title, key=itemgetter('time'), reverse=True)
    return notice_list

if __name__ == '__main__':
    tag=['home','jw','yjs','tw',]
    nepu_news(tag,'1')

