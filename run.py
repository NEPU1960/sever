#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: run.py
@time: 2019/2/25 0025 09:28
@desc:
"""
from api import creat_app
app=creat_app()
if __name__ == '__main__':
    app.run()