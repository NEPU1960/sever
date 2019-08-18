#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019-08-17 22:29
@desc:
'''
from flask import Blueprint

AD=Blueprint('AD',__name__)

from .routes import *