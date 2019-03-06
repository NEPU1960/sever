#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: get_openid.py
@time: 2019/3/6 0006 19:38
@desc:
"""
import requests
import json
def openid():
    appid='wx2d6c803a134581e6'
    secret='d20ddfe3841261ea72ea15df1254fd60'
    JSCODE='001zkQDr15GD3l0sjSDr1V7VDr1zkQDG'
    url='https://api.weixin.qq.com/sns/jscode2session?appid='+appid+'&secret='+secret+'&js_code='+JSCODE+'&grant_type=authorization_code'
    code2Session=requests.get(url).json()
    print(code2Session)
    # if 'errcode' in code2Session.keys():
    #     print('1')
    # else:
    #     openid=code2Session['openid']
    #     session_key=code2Session['session_key']
    #     print(openid,session_key)
    #
    # print(code2Session)
if __name__ == '__main__':
    openid()