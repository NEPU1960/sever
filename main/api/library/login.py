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
from main.comman import trueReturn,falseReturn
session=requests.session()
from main import make_celery,create_app
celery=make_celery(create_app())
@celery.task
def library_login(xh,pwd='0000'):
    '''图书馆登陆'''
    login_data={
        'dztm':xh,
         'dzmm':pwd
    }
    is_success=session.post('http://210.46.140.21:8080/opac/dzjsjg.jsp',data=login_data)#图书馆登陆
    if is_success.status_code==200:
        is_success=is_success.text
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
                    #print(booke_txt[0].get_text()[:-1])
                    for i in range(13):
                        name[i]=booke_txt[i].get_text()[:-1]
                    xiangxi.append(name)
            print(xiangxi)
            back_list=[]#带有剩余过期时间的返回信息
            for i in xiangxi:
                tss=i[9]
                date1 = datetime.datetime.strptime(tss, "%Y-%m-%d %H:%M:%S")
                date2 = datetime.datetime.now()
                num = (date1 - date2).days
                i[13] = num
                back_list.append(i)
            return trueReturn(data=back_list)
        elif '读者密码错误！请重新输入！' in is_success:
            print('读者密码错误！请重新输入！')
            return falseReturn(msg='密码错误')
        else:
            print('读者条码号不存在！请重新输入！')
            return falseReturn(msg='学号错误')
    else:
        return falseReturn(msg='系统暂时访问失败')

def extend_booke(xh,dctm):
    '''图书续借'''
    extend_data={
        'dztm':xh,
        'dctm':dctm
    }
    back_message=session.post('http://210.46.140.21:8080/opac/dzxj.jsp',data=extend_data).text
    if 'success' in back_message:
        print('续借成功')
    else:print(back_message)
def logout_library():
    session.post('http://210.46.140.21:8080/opac/dztc.jsp')
if __name__ == '__main__':
    library_login('178003070655')
    logout_library()