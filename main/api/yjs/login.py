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
import re
from main.api.yjs.jx import get_list
from ..queue import celery
from ...comman import falseReturn,trueReturn
session=requests.session()
header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '172.16.199.2:8008',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
def get_login(xh,pwd):
    '''登陆'''
    data={
        'userName': xh,
        'password': pwd,
        'radiovalue':'student'
    }

    url='http://172.16.199.2:8008/yjsjwgl/login.do'
    try:

        back_info=session.post(url,data=data,headers=header,timeout=(3.05, 5))
        if back_info.status_code!=200:
            return falseReturn(msg='系统暂时不能访问')
        elif '用户名或密码不正确' in back_info.text:

            return falseReturn(msg='学号或密码错误')
        else:
            return trueReturn(msg='100',data=session)
    except requests.exceptions.RequestException:
        return falseReturn(msg="连接超时")
@celery.task
def get_info(xh):
    '''获取个人信息'''
    url='http://172.16.199.2:8008/yjsjwgl/xsxxwh.do?method=xsgrxxwh'
    info=session.get(url,headers=header).text
    soup=BeautifulSoup(info,'lxml')
    name=str(soup.find_all('input')[5])
    zjhm=str(soup.find_all('input')[8])
    name=re.search('value=.+',name).group().replace('value="','').replace('"/>','')
    zjhm = re.search('value=.+', zjhm).group().replace('value="','').replace('"/>','')
    info={
        'xh':xh,
        'name':name,
        '身份证':zjhm
    }
    return info
@celery.task
def get_score(xn='',xq=''):
    '''成绩获取'''
    url='http://172.16.199.2:8008/yjsjwgl/xscjcx.do?act=find'
    data={
        'xn':xn,
        'xq':xq
    }
    '''研究生成绩查询'''
    info=session.post(url,data=data,headers=header).text
    #print(info)
    soup=BeautifulSoup(info,'lxml')
    div=soup.find_all('div')
    score=[]
    name=['xuenian','xueqi','classname','xingzhi','xuefen','classscore']
    xueqi = {}
    for i in div:
        tr=i.find_all('tr')
        for i in tr[1:]:
            score_info={}
            td=i.find_all('td')
            for j in range(0,6):
                score_info[name[j]]=td[j].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t')
            key=td[1].get_text('','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t')
            if key in xueqi:
                inter=xueqi[key]
                inter.append(score_info)
                xueqi[key]=inter
            else:
                xueqi_list=[]
                xueqi_list.append(score_info)
                xueqi[key]=xueqi_list
    for i in xueqi:
        score.append({i: xueqi[i]})
    print(score)
    return score
@celery.task
def get_class():
    '''课表获取'''

    # data={
    #     'dm':'',
    #     'xn':xn,
    #     'xq': xq
    # }
    url='http://172.16.199.2:8008/yjsjwgl/xsgrkbck.do'
    info=session.get(url,headers=header).text
    soup=BeautifulSoup(info,'lxml')
    div=soup.find_all('div')
    list=[]
    for i in div[3:]:
        tr=i.find_all('tr')
        for i in tr[1:]:
            td=i.find_all('td')
            fen=td[4].string
            te=fen.split('/')
            # print(te)
            for i in te:
                week = re.search('周.', i).group()

                jc = re.search('[0-9].*节', i).group()
                didian = re.search('【.+】', i).group()
                zhouci = re.search('】.+周', i).group()
                info_class={
                    'name':td[0].string,
                    'xuefen':td[1].string,
                    'teacher':td[2].string,
                    'xingzhi':td[3].string,
                    'week':week,
                    'jc':get_list(jc[:-1]),
                    'didian':didian,
                    'zhouci':get_list(zhouci[1:-2]),
                }
                list.append(info_class)
    return list
def yjs_loginout():
    session.get('http://172.16.199.2:8008/yjsjwgl/desSession.do')
if __name__ == '__main__':

    get_login()
    print(get_class())

