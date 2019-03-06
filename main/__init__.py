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
from flask_sqlalchemy import SQLAlchemy
import os
from .config import shuju

db=SQLAlchemy()



def create_app():
    app=Flask(__name__)
    app.config.from_object(shuju)
    shuju.init_app(app)
    db.init_app(app)

    from .api2 import api
    app.register_blueprint(api)
    return app



