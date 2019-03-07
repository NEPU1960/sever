#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/1/27 16:28
@desc:
'''

def trueReturn(msg='',data=''):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(msg='',data=''):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }