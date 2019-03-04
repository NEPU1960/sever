#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: login.py
@time: 2019/3/3 0003 16:06
@desc:
"""
import requests
from bs4 import BeautifulSoup
import datetime
session=requests.session()
def library_login():
    '''图书馆登陆'''
    # session.get('http://210.46.140.21:8080/opac/index_wdtsg.jsp')
    login_data={
        'dztm':'178003070655',
         'dzmm':'0000'
    }
    is_success=session.post('http://210.46.140.21:8080/opac/dzjsjg.jsp',data=login_data).text#图书馆登陆
    if 'success' in is_success:
        booke_info=session.get('http://210.46.140.21:8080/opac/index_wdtsg.jsp').text
        soup=BeautifulSoup(booke_info,'lxml')
        jiexi=soup.find_all('tr')
        xiangxi = []
        #print(jiexi[1])
        for i in jiexi[1]:
            c=i.find_all('tr')
            # print(c[1])
            for booke in c[1:]:
                name={}
                booke_txt=booke.find_all('td',class_='bordertd')
                print(booke_txt[0].get_text()[:-1])
                for i in range(13):
                    name[i]=booke_txt[i].get_text()[:-1]
                xiangxi.append(name)
        print(xiangxi)
        back_list=[]#带有剩余过期谁建的返回信息
        for i in xiangxi:
            if i[10] =='':
                tss=i[9]
                date1 = datetime.datetime.strptime(tss, "%Y-%m-%d %H:%M:%S")
                date2 = datetime.datetime.now()
                num = (date1 - date2).days
                print(num)

            else:
                tss = i[10]
                date1 = datetime.datetime.strptime(tss, "%Y-%m-%d %H:%M:%S")
                date2 = datetime.datetime.now()
                num = (date1 - date2).days
                print(num)
                i[13] = num
            i[13] = num
            back_list.append(i)






    elif '读者密码错误！请重新输入！' in is_success:
        print('读者密码错误！请重新输入！')
        return '登陆失败'
    else:
        print('读者条码号不存在！请重新输入！')
        return '登陆失败'

def extend_booke():
    '''图书续借'''
    extend_data={
        'dztm':'178003070655',
        'dctm':'01234687'
    }
    back_message=session.post('http://210.46.140.21:8080/opac/dzxj.jsp',data=extend_data)
    print(back_message.text)
def logout_library():
    session.post('http://210.46.140.21:8080/opac/dztc.jsp')
library_login()
extend_booke()
logout_library()