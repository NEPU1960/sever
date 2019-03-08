#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: get_info.py
@time: 2019/3/4 0004 20:54
@desc:获取个人信息
"""
from bs4 import BeautifulSoup
from main import create_app,make_celery
from main.comman import trueReturn
import time
celery=make_celery(create_app())
header={
    'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Accept-Encoding':'gzip, deflate',
    'Host':'jwgl.nepu.edu.cn'
}
@celery.task
def info(login):
    '''个人信息获取'''
    url="http://jwgl.nepu.edu.cn/xszhxxAction.do?method=addStudentPic&tktime="+str(int(time.time()))
    get_info = login.get(url).text
    soup=BeautifulSoup(get_info,'lxml')
    detailed_info=soup.find_all('tr')
    # print(detailed_info)
    info=detailed_info[4].find_all('td')
    IDcard = detailed_info[-2].find_all('td')
    # print(IDcard)
    IDnumber=IDcard[3].get_text('','\xa0')

    yuanxi=info[0].get_text()[3:]
    zhuanye=info[1].get_text()[3:]
    xuezhi=info[2].get_text()[3:]
    banji=info[3].get_text()[3:]
    xuehao=info[4].get_text()[3:]
    next_info = detailed_info[5].find_all('td')
    year=str(int(xuezhi)+int(xuehao[0:2]))
    xinxi={
        '姓名': next_info[1].get_text()[1:],
        '院系':yuanxi,
        '专业':zhuanye,
        '学制':xuezhi,
        '班级':banji,
        '学号':xuehao,
        '性别':next_info[3].get_text()[1:],
        '身份证':IDnumber,
        '毕业日期':'20'+year
    }
    # print(xinxi)
    get_info_picture = login.get("http://jwgl.nepu.edu.cn/uploadfile/studentphoto/pic/{}.JPG".format(xuehao),headers=header)
    with open(xuehao+'.jpg', 'wb')as f:
        f.write(get_info_picture.content)
    return xinxi
if __name__ == '__main__':
    info()