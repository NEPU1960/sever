#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: Auth_login.py
@time: 2019/3/7 0007 08:43
@desc:
"""
from main.api2.jwc.jwc_login import login_jwc,logout
from main.api2.jwc.get_info import info
from main.api2.ecard.login import ecard_login
def auth(xh,pwd):
    login=login_jwc(xh,pwd)
    back=info(login)
    print(back)
    sfz=back['身份证']
    if 'X' in sfz:
        ecard_pwd=sfz[-7:-2]
    else:
        ecard_pwd=sfz[-6:-2]
    name=ecard_login(xh,ecard_pwd)
    print(name)

if __name__ == '__main__':
    xh='130101140323'
    pwd='032050'
    auth(xh,pwd)