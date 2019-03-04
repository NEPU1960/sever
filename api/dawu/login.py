#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: login.py
@time: 2019/3/4 0004 15:14
@desc:
"""
import requests
import re
from bs4 import BeautifulSoup
def login():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url='http://61.167.120.8/users/sign_in'
    url2='http://61.167.120.8/'
    login = requests.session()
    get_token=login.get(url2,headers=header).text
    soup=BeautifulSoup(get_token,'lxml')
    search_token=soup.find_all('input')[1]
    t = re.search('value.*', str(search_token)).group()
    token=t[7:-3]
    print(t,token)
    data={
        'utf8':'✓',
        'authenticity_token':token,
        'user[account_numb]':'170702140207',
        'user[password]':'Stu140207',
        'user[remember_me]':'0',
        'commit':'登录',
    }
    t=login.post(url,data=data,headers=header)
    info=login.get(url2,data=data,headers=header).text
    #print(info)
    find_soup=BeautifulSoup(info,'lxml')
    table=find_soup.find_all('tbody')
    #print(table)
    for i in table[1:2]:
        print(i.find_all('tr'))

login()