#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019-08-17 22:30
@desc:
'''
from . import AD
from main import redis
from ..model import get_ad,get_version
from ..comman import trueReturn,falseReturn
from flask import jsonify

@AD.route('/ad')
def get_url():
    back=get_ad()
    return jsonify(trueReturn(data=back))
@AD.route('/version')
def version():
    ver=get_version()
    return jsonify(trueReturn(data=ver))