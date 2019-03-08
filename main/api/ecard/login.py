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
from main.api.ecard.get_password import get_pay_keyboard_number_location
from bs4 import BeautifulSoup
global session
import re
from PIL import Image
from io import BytesIO
from ... import celery

session=requests.session()



def ecard_login(xh,pwd):
    header = {
        'Content - Type': 'application / x - www - form - urlencoded',
        'Connection': 'Keep-Alive',
        'Host': 'yikatong.nepu.edu.cn',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
        'Accept':	'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*'
    }
    url = 'http://yikatong.nepu.edu.cn/'
    session.get(url+'homeLogin.action')
    session.get(url+'getCheckpic.action?rand=8888.197958871872')
    get_pass_url = 'http://yikatong.nepu.edu.cn/getpasswdPhoto.action'
    pw = requests.get(get_pass_url)
    im = Image.open(BytesIO(pw.content))
    new_pwd = get_pay_keyboard_number_location(im, pwd)
    #print(new_pwd)
    data={
        "imageField.x": "20",
        "imageField.y": "12",
        'name':xh,
        'userType':'1',
        'passwd':new_pwd,
         'loginType':'2',
        'rand':'8888'
    }
    try:
        back_info=session.post('http://yikatong.nepu.edu.cn/loginstudent.action',data=data,headers=header, timeout=(3.05, 5))
        #print(back_info.content)
        if '登陆失败，密码错误' in back_info:
            return '密码输入错误'
        elif '登陆失败，无此用户名称！' in back_info:
            return '账号输入错误'
        else:
            '''获取用户信息、账号'''
            user_info=session.get('http://yikatong.nepu.edu.cn/accountcardUser.action').text
            soup=BeautifulSoup(user_info,'lxml')
            te=soup.find_all('table')
            number=soup.find_all('div')
            user_number=number[4].string#一卡通账号获取
            print(user_number)
            for i in te[1:2]:
                tr=i.find_all('td')
                te=tr[-5].string
            a = re.search('.+(卡)', te).group()
            b = re.search('(额).+(当)', te).group()
            c = re.search('(过渡余额).+(上)', te).group()
            yue={
                '卡余额':a[:-2],
                '当前过渡余额':b[2:-2],
                '上次过渡余额':c[5:-2],
            }
            print(yue)
            ecard_post_data = {
                'account': user_number,
                'inputObject': 'all',
                'Submit': '+确+定+'
            }
            get_usernumber=session.post('http://yikatong.nepu.edu.cn/accounthisTrjn.action',data=ecard_post_data).text #获取账号
            #print(get_usernumber)
            soup=BeautifulSoup(get_usernumber,'lxml')
            adress=str(soup.find_all('form'))
            sc = re.search(r'"/accounthisTrjn.action[^\s]*', adress).group()#获取账单查询地址
            # print(sc)
            post_url='http://yikatong.nepu.edu.cn'+sc[1:-1]
            post=session.post(post_url,data=ecard_post_data,headers=header).text
            # print(post)
            soup2=BeautifulSoup(post,'lxml')
            adress2=str(soup2.find_all('form'))
            sc = re.search(r'"/accounthisTrjn.action[^\s]*', adress2).group()  # 获取日期提交地址
            # print(sc)
            post_url = 'http://yikatong.nepu.edu.cn' + sc[1:-1]
            # print('查询日期地址',post_url)
            ecard_post_time_data={
                'inputStartDate':'20181201',
                'inputEndDate':'20181231'
            }
            te=session.post(post_url,data=ecard_post_time_data).text
            #print(te)
            soup3=BeautifulSoup(te,'lxml')
            adress3=str(soup3.find_all('form'))
            # print(adress3)
            exp = re.compile('action="(.*)"\sid')
            url = exp.findall(str(adress3))[0]
            last_sc3 = re.search(r'__continue=[^\s]*', adress3).group()  # 获取查询提交地址
            post_url2 = 'http://yikatong.nepu.edu.cn/accounthisTrjn.action'+url
            test={
                '__continue' :last_sc3[:-1]
            }
            te = session.get(post_url2,headers=header).text
            exp = re.compile("&nbsp;&nbsp;.(\d{1,2}).*&nbsp.*\d")
            PageCount = int(exp.findall(te)[0])#总页面数
            print(PageCount)

            '''获取页信息'''
            data={
                'pageNum':'1'
            }
            te=session.post('http://yikatong.nepu.edu.cn/accountconsubBrows.action',data=data,headers=header).text
            soup = BeautifulSoup(te, 'lxml')
            jixi = soup.find_all('tr', attrs={"class": re.compile("^listbg")})
            # print(jixi)
            zhangdan = []
            for i in jixi:
                td = i.find_all('td')
                info = {
                    '时间': td[0].string,
                    '交易类型': td[1].string,
                    '子系统名称': td[2].string,
                    '电子账户': td[3].string,
                    '交易额': td[4].string,
                    '现有余额': td[5].string,
                    '次数': td[6].string,
                    '状态': td[7].string
                }
                zhangdan.append(info)  # 总消费记录
            print(zhangdan)

            return 'yes'
    except requests.exceptions.RequestException:
        return {'msg':"连接超时"}

if __name__ == '__main__':
    c=ecard_login('178003070655','032050')
    print(c)