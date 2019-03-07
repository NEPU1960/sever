#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: get_kb.py
@time: 2019/3/6 0006 08:52
@desc:获取课表
"""
from bs4 import BeautifulSoup
from main.api.jwc.zhouchuli import get_zhou_list
from main import create_app,make_celery
celery=make_celery(create_app())
header={
    'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Accept-Encoding':'gzip, deflate',
    'Host':'jwgl.nepu.edu.cn'
}
@celery.task
def get_kb(login,username,xnxqh='2018-2019-2'):
    '''获取课表'''
    url='http://jwgl.nepu.edu.cn/tkglAction.do?method=goListKbByXs&sql=&xnxqh='+xnxqh+'&zc=&xs0101id='+username
    get_info = login.get(url,headers=header).text
    soup=BeautifulSoup(get_info,'lxml')
    table=soup.find_all('table')
    total=[]
    for i in table[:-3]:
        tr=i.find_all('tr')
        jieci = 0
        for i in tr[1:-1]:
            td=i.find_all('td',)
            week = 0
            jieci=jieci+1
            for i in td:
                div=i.find_all('div',id=str(jieci)+'-'+str(week)+'-'+str(2))
                for i in div:
                    test=i.get_text(' ', '<br/>')
                    h = test.split(' ')
                    width=len(h)/5
                    if width<1:
                        info={
                            '星期':week,
                            '节次':jieci,
                            '课程':None,
                            '教师':None,
                            '教室':None,
                            '周次':None,
                            '班级':None,
                        }
                        total.append(info)
                    else:
                        for i in range(int(width)):
                            info={
                                '星期': week,
                                '节次': jieci,
                                '课程': h[0],
                                '教师': h[2],
                                '教室': h[4],
                                '周次': get_zhou_list(h[3]),
                                '班级': h[1],
                            }
                            total.append(info)
                week = week + 1
    return total