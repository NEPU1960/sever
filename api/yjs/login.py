#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: login.py
@time: 2019/3/5 0005 16:14
@desc:
"""
import requests
from bs4 import BeautifulSoup
def get_login():
    data={
        'userName': '178003070655',
        'password': 'zhmsn5211314',
        'radiovalue':'student'
    }
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '172.16.199.2:8008',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url='http://172.16.199.2:8008/yjsjwgl/login.do'
    session=requests.session()
    session.post(url,data=data,headers=header)
    url='http://172.16.199.2:8008/yjsjwgl/xscjcx.do?act=find'
    data={
        'xn':'',
        'xq':''
    }
    '''研究生成绩查询'''
    info=session.post(url,data=data).text
    #print(info)
    soup=BeautifulSoup(info,'lxml')
    div=soup.find_all('div')
    score=[]
    for i in div:
        tr=i.find_all('tr')
        for i in tr[1:]:
            td=i.find_all('td')
            score_info={
                '学年':td[0].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t'),
                '学期':td[1].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t'),
                '课程名称':td[2].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t'),
                '课程性质':td[3].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t'),
                '学分':td[4].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t'),
                '正考成绩':td[5].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t'),
            }
            score.append(score_info)
    print(score)

get_login()


