#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: __init__.py.py
@time: 2019/3/6 0006 14:31
@desc:
"""
from flask import Blueprint

api=Blueprint('api',__name__)

from .routes import *

