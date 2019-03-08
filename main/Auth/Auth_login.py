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
from main.api.jwc.jwc_login import login_jwc,logout
from main.api.jwc.get_info import info
from main.api.library.login import library_login
from main.api.ecard.login import ecard_login
from main.api.yjs.login import get_login,get_info
from main.comman import falseReturn,trueReturn
from main import create_app
from ..model import add_jw_pwd
from . import Auth
from flask import request,jsonify
#=create_app()
from ..AES import AESCipher
@Auth.route('/',methods=['POST'])
def auth():
    xh=request.get_json()['studentid']
    pwd=request.get_json()['passwd']
    print(xh,pwd)
    if xh[2:4]=='80':#判断是否是研究生
        login_info=get_login(xh,pwd)
        if login_info['msg']!='100':
            return login_info
        else:
            back = get_info(xh)
            sfz=back['身份证']
            print(sfz)

    else:
        login=login_jwc(xh,pwd)
        if login['status']==False:
            return login
        else:
            login=login['data']
            back=info(login)
            list=[back]
            print(back)
            sfz=back['身份证']
    if 'X' in sfz:
        ecard_pwd=sfz[-7:-2] #一卡通密码获取
    else:
        ecard_pwd=sfz[-6:-2]
        name=ecard_login(xh,ecard_pwd)
        if name=='yes':
            ecard_pwd=ecard_pwd
        else:
            ecard_pwd=None
    back=library_login(xh)
    if back['status']==True:
        library_pwd='0000'
    else:
        library_pwd=None
    add_jw_pwd(studentid=xh,jw_pwd=pwd,library_pwd=library_pwd,ecard_pwd=ecard_pwd,student_info=back)
    return jsonify(back)
if __name__ == '__main__':
    xh='13010114033'
    print(xh[2:4])
    pwd='032050'
    auth(xh,pwd)