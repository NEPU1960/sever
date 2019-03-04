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
    url='http://61.167.120.8/users/sign_in'
    url2='http://61.167.120.8/'
    get_token=requests.get(url2).text
    soup=BeautifulSoup(get_token,'lxml')
    search_token=soup.find_all('input')[1]
    t = re.search('value.*', str(search_token)).group()
    token=t[7:-3]
    print(t,token)
    login='登陆'.encode('utf-8')
    header={
        'Content-Type': 'text/html; charset=utf-8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive'
        }
    data={
        'utf8':'%E2%9C%93',
        'authenticity_token':token,
        'user[Baccount_numb]':'170702140207',
        'user[Bpassword]':'Stu140207',
        'user[Bremember_me]':'0',
        'commit':login,
    }
    login=requests.session()
    login.post(url,data=data,headers=header)
    info=login.post(url2,data=data,headers=header)
    print(info.text)
login()