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
from .library.search_book import get_name_book,get_info

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
@api.route('/library/search',methods=['POST'])
def search_library():
    book_name=request.get_json()['book_name']
    page=request.get_json()['page']
    shearch_result=get_name_book(book_name,page)
    return jsonify(shearch_result)
@api.route('/library/get_search_info',methods=['POST'])
def book_info():
    book_url=request.get_json()['herf']
    book_info=get_info(book_url)
    return jsonify(book_info)

