#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: login.py
@time: 2019/2/28 0028 16:29
@desc:
"""
import requests
from api.ecard.get_password import get_pay_keyboard_number_location
from bs4 import BeautifulSoup
global session
from requests.auth import HTTPDigestAuth
import re
import time
session=requests.session()
session.auth=HTTPDigestAuth("178003070655", "032050")


def get_re_url( r):
    # 操作正在进行获取查询url
    soup = BeautifulSoup(''.join(r.text))
    con = soup.find_all("form")[0]
    exp = re.compile('action="(.*)"\sid')
    url = exp.findall(str(con))[0]
    return url

def login():
    header = {
        'Content - Type': 'application / x - www - form - urlencoded',
        'Connection': 'Keep-Alive',
        'Host': 'yikatong.nepu.edu.cn',
        'Connection':	'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
        'Accept':	'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*'
    }

    session.get('http://yikatong.nepu.edu.cn/homeLogin.action')
    session.get('http://yikatong.nepu.edu.cn/getCheckpic.action?rand=8888.197958871872')
    url = 'http://yikatong.nepu.edu.cn/getpasswdPhoto.action'
    pwd=session.get(url)
    with open('im.jpg','wb') as f:
        f.write(pwd.content)
    new_pwd=get_pay_keyboard_number_location('im.jpg','032050')
    data={
        "imageField.x": "20",
        "imageField.y": "12",
        'name':'178003070655',
        'userType':'1',
        'passwd':new_pwd,
         'loginType':'2',
        'rand':'8888'
    }

    ecard_login=session.post('http://yikatong.nepu.edu.cn/loginstudent.action',data=data,headers=header)
    # te=session.get('http://yikatong.nepu.edu.cn/accountleftFrame.action',headers=header)
    # print(te.text)
    get_usernumber=session.get('http://yikatong.nepu.edu.cn/accounthisTrjn.action').text #获取账号
    #print(choose_user)
    soup=BeautifulSoup(get_usernumber,'lxml')
    user_number=soup.find('select').get_text()#获取账号
    adress=str(soup.find_all('form'))
    sc = re.search(r'"/accounthisTrjn.action[^\s]*', adress).group()#获取账单查询地址
    # print(sc)
    post_url='http://yikatong.nepu.edu.cn'+sc[1:-1]
    # print('账单地址',post_url)
    #print(user_number)
    ecard_post_data={
        'account':user_number,
        'inputObject':'all',
        'Submit' :'+ % C8 % B7 + % B6 % A8 +'
    }
    post=session.post(post_url,data=ecard_post_data).text
    # print(post)
    soup2=BeautifulSoup(post,'lxml')
    adress2=str(soup2.find_all('form'))
    sc = re.search(r'"/accounthisTrjn.action[^\s]*', adress2).group()  # 获取日期提交地址
    # print(sc)
    post_url = 'http://yikatong.nepu.edu.cn' + sc[1:-1]
    # print('查询日期地址',post_url)
    ecard_post_time_data={
        "inputEndDate": "20170930",
        "inputStartDate": "20170801",
    }
    te=session.post(post_url,data=ecard_post_time_data).text
    #print(te)
    soup3=BeautifulSoup(te,'lxml')
    adress3=str(soup3.find_all('form'))
    # print(adress3)
    exp = re.compile('action="(.*)"\sid')
    url = exp.findall(str(adress3))[0]
    print(url)
    last_sc3 = re.search(r'__continue=[^\s]*', adress3).group()  # 获取查询提交地址
    print('最终查询地址',last_sc3[:-1])
    post_url2 = 'http://yikatong.nepu.edu.cn/accounthisTrjn.action'+url
    test={
        '__continue' :last_sc3[:-1]
    }
    print(post_url2)
    test_url='http://yikatong.nepu.edu.cn/accounthisTrjn.action?__continue=6a5891cbdf5c768522168250b7eb1534'
    post_header = {
        'Content - Type': 'application / x - www - form - urlencoded',
        'Connection': 'Keep-Alive',
        'Host': 'yikatong.nepu.edu.cn',
        'Referer':post_url,
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language':'zh-CN',
        'Content-Length':	'0',
        'Pragma':	'no-cache',
        'Accept-Encoding':	'gzip, deflate'
    }
    te = session.post(post_url2,headers=post_header).text
    print(te)


    # info=session.post('http://yikatong.nepu.edu.cn/accounthisTrjn.action?__continue=01fc9786b8fc802bc910007d43a2cc10')
    # print(info.text)
    '''获取用户信息、账号'''
    user_info=session.get('http://yikatong.nepu.edu.cn/accountcardUser.action')
    print(user_info.text)



login()