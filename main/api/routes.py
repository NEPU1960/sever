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
from main import create_app
from flask import request,jsonify
from ..Auth.get_openid import openid
from ..pyJWT import verify_bearer_token
import json
from ..comman import falseReturn,trueReturn

app=create_app()

@api.route('/',methods=['POST'])
def hello_world():
    code=request.get_json()['code']
    back=openid(code)
    if back['status']==False:
        return jsonify(falseReturn(msg='非法访问'))
    else:

        return 'Hello World!'
@api.route('/news/jwc_login')
def get_news_list():
    te = request.headers['Authorization'][7:]
    c=verify_bearer_token(te)
    print(c)
    return '1'