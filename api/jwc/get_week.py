#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: get_week.py
@time: 2019/3/5 0005 08:45
@desc:
"""
import time
import datetime
def today_week():
    week=time.localtime()
    get_week=time.strftime("%w",week)#星期
    st=datetime.datetime.strptime('2019-03-04', "%Y-%m-%d")#开学日期
    en=datetime.datetime.now()
    jg=(en-st).days#日期间隔

    zhou=int(jg/7+1)
    print('今天星期：',get_week)
    print('第',zhou,'周')
if __name__ == '__main__':
    today_week()
