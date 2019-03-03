#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: ceshi.py
@time: 2019/2/28 0028 11:00
@desc:
"""
import hashlib
s='81, 106'
m= hashlib.md5(s.encode())
print(m.hexdigest())
c={'3': (18, 147), '1': (54, 111), '7': (90, 39), '8': (90, 75), '4': (54, 39), '6': (18, 111), '9': (54, 75), '2': (18, 75), '0': (18, 39), '5': (90, 111)}
print((c['3'])[0])
d={}
for i in c:
    s=str(c[i])
    m = hashlib.md5(s.encode())
    d[m.hexdigest]=i
    print(m.hexdigest(),i)
print(d)
search={
    '64815e2fc717e5868bc67d964cb3cd5e': '0',
    '1daab1e22cb8de4fe73abdac88d4c4a2': '1',
    '7e84d3f49d0c97537fd5bcf4a1fcaa76': '2',
    'e68198bcb7298f0c123e05b832ab4998': '3',
    '8013c24d8a013a0a335e4b24f060266f': '4',
    '1d01f46dfbc4ed3acfcb9e85b0147fad': '5',
    'a2cc12324f78396a8a4d363f9bb49203': '6',
    '01cd6bb152f14d2ce9b36c889e3dcb0a': '7',
    'fbd3fb739f08aaede71b890e3dc72e35': '8',
    'a0009c7c70d5f65f3e2bd7bac7a6381a':'9'
}

