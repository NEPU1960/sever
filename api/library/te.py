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
import re

te='45.46元（卡余额）0.00元(当前过渡余额)50.00元(上次过渡余额)'
a=re.search('.+(卡)',te).group()
b=re.search('(额).+(当)',te).group()
c=re.search('(过渡余额).+(上)',te).group()
print(a[:-2],b[2:-2],c[5:-2])

