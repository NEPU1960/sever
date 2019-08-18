#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: queue.py
@time: 2019/3/7 0007 14:22
@desc:队列消息
"""
from main import create_app,make_celery
celery=make_celery(create_app())