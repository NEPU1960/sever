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
from . import api
import requests
from flask import request
from main.pyJWT import  verify_bearer_token
from main.api.zhaopin.get_list import nepu_news

@api.route('/',)
def login():
    # te=request.headers.get('Authorization')
    # print(te)
    # c=verify_bearer_token(te[7:])
    # print(c)
    return 'yes'
@api.route('/zhaopin')
def get_news_list():
    c=nepu_news()
    print(c)
    return nepu_news()