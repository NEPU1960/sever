#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: tel_number.py
@time: 2019/3/10 0010 10:22
@desc:
"""
from bs4 import BeautifulSoup
import requests
import urllib3
header={
    'Accept':	'*/*',
    'User-Agent':	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',

}
url='http://yxweb.nepu.edu.cn/dhcx'
session=requests.session()
session.get(url,headers=header)
def get_number():
    list_dw=session.get('http://yxweb.nepu.edu.cn/dhcx/',headers=header).content
    list_dw =list_dw.decode('gb2312')
    soup=BeautifulSoup(list_dw,'lxml')
    option=soup.find_all('option')
    list_dw=[]
    for i in option:
        list_dw.append(i.get_text())
    print(list_dw)


    url='http://yxweb.nepu.edu.cn/dhcx/index1.asp'
    print(url)
    tel=session.get('http://yxweb.nepu.edu.cn/dhcx/index1.asp?dw=%B9%FA%BC%CA%BA%CF%D7%F7%B4%A6',headers=header)
    print(tel.content.decode('unicode_escape').encode('utf-8'))
if __name__ == '__main__':
    get_number()