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

c="onclick=seegc('zyk','zyk0519750')"
print(re.search('zyk[0-9]+',c).group())
# print(re.search('zyk[^\b]\'',c).group())

