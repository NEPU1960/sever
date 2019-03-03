#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/1/26 23:13
@desc:
'''
from flask import Flask
from api.config import *

def creat_app():
    app=Flask(__name__)
    app.config.from_object(shuju)
    shuju.init_app(app)
    return app




