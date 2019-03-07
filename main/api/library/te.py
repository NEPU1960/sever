#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: te.py
@time: 2019/3/4 0004 08:29
@desc:
"""
import requests
status=requests.get('http://210.46.140.21')
print(status.status_code)
if status.status_code==200:
    print('scuss')
else:print('fail')