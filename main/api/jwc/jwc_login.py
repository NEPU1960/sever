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
from main.api.jwc.yzm.getcode import get_validate_code_from_image
from main.comman import trueReturn,falseReturn

login = requests.session()
session = login.get('http://jwgl.nepu.edu.cn')
header={
    'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Accept-Encoding':'gzip, deflate',
    'Host':'jwgl.nepu.edu.cn'
}

def login_jwc(username,pwd):
    '''教务处登陆'''
    code = login.get("http://jwgl.nepu.edu.cn/verifycode.servlet",headers=header)
    if code.status_code==200:
        im = Image.open(BytesIO(code.content))
        im = im.convert('L')
        yzm = get_validate_code_from_image(im)
        data={
            'USERNAME': username,
            'PASSWORD': pwd,
            'RANDOMCODE': yzm
        }
        success = login.post('http://jwgl.nepu.edu.cn/Logon.do?method=logon', data=data,headers=header)

        if "验证码错误!!" in success.text:
            login_jwc()
        elif '该帐号不存在或密码错误,请联系管理员' in success.text:
            return falseReturn(msg='学号不存在或密码错误')
        else:
            login.get('http://jwgl.nepu.edu.cn/Logon.do?method=logonBySSO',headers=header)
        return trueReturn(data=login)
    else:
        return falseReturn(msg='教务系统暂时无法访问')

def logout():
    '''登出教务系统'''
    login.get('http://jwgl.nepu.edu.cn/Logon.do?method=logout',headers=header)

if __name__ == '__main__':
    c=login_jwc('178003070655','111')
    print(c)
    logout()

