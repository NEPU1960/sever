#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: routes.py
@time: 2019/3/6 0006 15:07
@desc:
"""

import requests

def login():
    appid='wx2d6c803a134581e6'
    secret='d20ddfe3841261ea72ea15df1254fd60'
    JSCODE=''
    url='https://api.weixin.qq.com/sns/jscode2session?appid='+appid+'&secret='+secret+'&js_code=JSCODE&grant_type=authorization_code'
    code2Session=requests.get(url).text

    return 'yes'