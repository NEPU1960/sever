#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: score.py
@time: 2019/3/6 0006 08:48
@desc:成绩查询
"""
import requests
from bs4 import BeautifulSoup
from ..queue import celery
header={
    'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Accept-Encoding':'gzip, deflate',
    'Host':'jwgl.nepu.edu.cn'
}

@celery.task
def socer(login):
    '''成绩查询'''
    cj_data = {
        'kksj': '',
        'kcxz': '',
        'kcmc': '',
        'xsfs': 'qbcj'
    }
    get_kb = login.post('http://jwgl.nepu.edu.cn/xszqcjglAction.do?method=queryxscj', data=cj_data,headers=header).text
    soup=BeautifulSoup(get_kb,'lxml')
    div=soup.find_all('div')
    score=[]
    name=['number','xuehao','name','xuenian','class-name','class-score','biaozhi','xingzhi','leibie','xueshi','xuefen','xingzhi','buchongxueqi']
    xueqi = {}
    for i in div[5]:#获取成绩
        tr=i.find_all('tr')
        for i in tr:
            info = {}
            td=i.find_all('td')
            for i in range(len(td)):
                info[name[i]]=td[i].get_text()
                # "0": " 71",
                # "1": "161201440101",
                # "2": "张贺",
                # "3": "2018-2019-1",
                # "4": "申论",
                # "5": "83",
                # "6": " ",
                # "7": "专业选修课",
                # "8": "限选",
                # "9": "32",
                # "10": "2",
                # "11": "正常考试",
                # "12": " "
            key=td[3].get_text()
            if key in xueqi:
                inter=xueqi[key]
                inter.append(info)
                xueqi[key]=inter
            else:
                xueqi_list=[]
                xueqi_list.append(info)
                xueqi[key]=xueqi_list

            # xueqi[td[3].get_text()]=info
            # score.append(xueqi)
    for i in xueqi:
        score.append({i:xueqi[i]})
    score.reverse()

    for i in div[8]:#获取学分
        span=i.find_all('span')
        xuefen={
            'total':span[0].get_text(),
            'finish':span[1].get_text(),
            'last':span[2].get_text(),
            'grade':span[3].get_text()[:-1]
        }
    return {'score':score,'xuefen':xuefen}