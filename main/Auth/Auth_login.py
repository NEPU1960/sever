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
from main.api2.library.login import library_login
from main.api2.ecard.login import ecard_login
from main.api2.yjs.login import get_login,get_info
from main.comman import falseReturn,trueReturn
def auth(xh,pwd):
    if xh[2:4]=='80':#判断是否是研究生
        login=get_login(xh,pwd)
        back=get_info(xh)
        print(back)
    else:
        login=login_jwc(xh,pwd)
        if login['status']==False:
            return login
        else:
            login=login['data']
            back=info(login)
            print(back)
            sfz=back['身份证']
            if 'X' in sfz:
                ecard_pwd=sfz[-7:-2] #一卡通密码获取
            else:
                ecard_pwd=sfz[-6:-2]
            # name=ecard_login(xh,ecard_pwd)
            #     # print
    back=library_login(xh)
    print(back)


if __name__ == '__main__':
    xh='13010114033'
    print(xh[2:4])
    pwd='032050'
    auth(xh,pwd)