#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: __init__.py.py
@time: 2019/3/6 0006 14:34
@desc:
"""
from flask_sqlalchemy import SQLAlchemy
from main import create_app
app=create_app()

db=SQLAlchemy(app)