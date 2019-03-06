#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/1/26 23:17
@desc:
'''
class shuju():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://wenepu:945999685@localhost:3306/wenepu'

    @staticmethod
    def init_app(app):
        pass