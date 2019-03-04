#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/1/26 23:23
@desc:教务处模块，认证备用
'''
import requests
from PIL import Image
from io import BytesIO
from api.jwc.yzm.getcode import get_validate_code_from_image
from bs4 import BeautifulSoup
import time

global login
login = requests.session()
session = login.get('http://jwgl.nepu.edu.cn')
header={
    'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Accept-Encoding':'gzip, deflate',
    'Host':'jwgl.nepu.edu.cn'
}
# def get_session():
#     global login
#     login = requests.session()
#     session = login.get('http://jwgl.nepu.edu.cn')
#     return login

def login_jwc():
    '''教务处登陆'''
    denglu=time.time()
    code = login.get("http://jwgl.nepu.edu.cn/verifycode.servlet",headers=header)
    im = Image.open(BytesIO(code.content))
    im = im.convert('L')
    yzm = get_validate_code_from_image(im)
    zhanghe_data = {
        'USERNAME': '161201440101',
        'PASSWORD': '101044102161',
        'RANDOMCODE': yzm
    }
    data={
        'USERNAME': '130101140323',
        'PASSWORD': '032050',
        'RANDOMCODE': yzm
    }
    xinxijiyuan_data={
        'USERNAME': '140202140214',
        'PASSWORD': 'xinjiyuan18',
        'RANDOMCODE': yzm
    }
    success = login.post('http://jwgl.nepu.edu.cn/Logon.do?method=logon', data=data,headers=header)
    if "验证码错误!!" in success.text:
        return '验证码错误'
    elif '该帐号不存在或密码错误,请联系管理员' in success.text:
        return '学号或密码输入错误'
    else:
        hc = login.get('http://jwgl.nepu.edu.cn/Logon.do?method=logonBySSO',headers=header)
    #print(hc.text)
    denglujieshu=time.time()
    print('登陆消耗：',denglujieshu-denglu)
    return login


def socer():
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

    for i in div[5]:
        tr=i.find_all('tr')
        for i in tr:
            info = {}
            td=i.find_all('td')
            for i in range(len(td)):
                info[i]=td[i].get_text()
            score.append(info)
    for i in div[8]:
        span=i.find_all('span')
        xuefen={
            'total':span[0].get_text(),
            'finish':span[1].get_text(),
            'last':span[2].get_text(),
            'grade':span[3].get_text()[:-1]
        }

def info():
    '''个人信息获取'''
    url="http://jwgl.nepu.edu.cn/xszhxxAction.do?method=addStudentPic&tktime="+str(int(time.time()))
    get_info = login.get(url).text
    soup=BeautifulSoup(get_info,'lxml')
    detailed_info=soup.find_all('tr')
    info=detailed_info[4].find_all('td')

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
        '毕业日期':'20'+year
    }
    get_info_picture = login.get("http://jwgl.nepu.edu.cn/uploadfile/studentphoto/pic/{}.JPG".format(140202140214),headers=header)
    with open('zjz.jpg', 'wb')as f:
        f.write(get_info_picture.content)


def get_kb():
    url='http://jwgl.nepu.edu.cn/tkglAction.do?method=goListKbByXs&sql=&xnxqh=2016-2017-1&zc=&xs0101id=130101140323'
    url2='http://jwgl.nepu.edu.cn/tkglAction.do?method=goListKbByXs&istsxx=no&xnxqh=2018-2019-1&zc=&xs0101id=130101140323'
    get_info = login.get(url,headers=header).text
    # with open('get_kb.xml', 'wb') as f:
    #     f.write(get_info.content)
    soup=BeautifulSoup(get_info,'lxml')
    table=soup.find_all('table')
    # print(table)
    total=[]
    for i in table[:-3]:
        tr=i.find_all('tr')
        jieci = 0
        for i in tr[1:-1]:

            td=i.find_all('td',)
            #print(td)
            week = 0
            jieci=jieci+1
            for i in td:
                div=i.find_all('div',id=str(jieci)+'-'+str(week)+'-'+str(2))
                # week=week+1
                info={}

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
                                '周次': h[3],
                                '班级': h[1],
                            }
                            total.append(info)
                week = week + 1

                    # for i in range(len(h)/5):
            # for j in range(1,8):
            #     print(str(c)+'-'+str(j)+'-'+str(2))
            # c=c+1
    print(total)

def get_jxjh():
    get_jxjh = login.get("http://jwgl.nepu.edu.cn/pyfajhgl.do?method=toViewJxjhXs&tktime="+str(int(time.time())),headers=header)
    with open('jxjh.xml', 'wb') as f:
        f.write(get_jxjh.content)
def logout():
    login.get('http://jwgl.nepu.edu.cn/Logon.do?method=logout',headers=header)

if __name__ == '__main__':
    c=login_jwc()
    get_kb()
    logout()

