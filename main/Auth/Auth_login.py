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
from main.api.yjs.login import get_login,get_info,get_score,get_class
from ..api.jwc.get_kb import get_kb
from ..api.jwc.jxjh import get_jxjh
from ..api.jwc.score import socer
from main.comman import falseReturn,trueReturn
from main import create_app
from ..model import *
from . import Auth
from flask import request,jsonify
import json
import time
#=create_app()
from ..pyJWT import create_token
from ..AES import AESCipher
@Auth.route('/',methods=['POST'])
def auth():
    xh=request.get_json()['studentid']
    pwd=request.get_json()['passwd']
    print(xh,pwd)
    if xh[2:4]=='80':#判断是否是研究生
        login_info=get_login(xh,pwd)

        if login_info['msg']!='100':
            return jsonify(login_info)
        else:
            type = '0'
            back_info = get_info(xh)
            score=get_score()
            kb=get_class()
            jw_status='1'
    else:
        login=login_jwc(xh,pwd)
        if login['status']==False:
            return jsonify(login)
        else:
            type = '1'
            login=login['data']
            back_info=info(login)
            score=socer(login)
            kb=get_kb(login,username=xh)
            jxjh=get_jxjh(login)
            add_jw_info(studentid=xh,score=str(score),timetable=str(kb),plan=str(jxjh))
            jw_status = '1'
    print(back_info)
    sfz=back_info['身份证']
    '''一卡通系统故障，暂时不提供'''
    if 'X' in sfz:
        ecard_pwd=sfz[-7:] #一卡通密码获取
    else:
        ecard_pwd=sfz[-8:-2]
    name=ecard_login(xh,ecard_pwd)
    if name=='yes':
        ecard_pwd=ecard_pwd
    else:
        ecard_pwd=None
    library_login_info=library_login(xh)
    if library_login_info['status']==True:
        library_pwd='0000'
        library_status='1'
    else:
        library_pwd=None
        library_status = '0'
    #add_jw_pwd(studentid=xh,jw_pwd=pwd,library_pwd=library_pwd,ecard_pwd=ecard_pwd,info=str(back_info),type_info=type,IDnumber=sfz)
    status={
        'jw_status':jw_status,
        'library_status':library_status,
    }
    token=create_app(xh,status)
    back_info={
        "jw":{
            "kb":kb,
            "score":score,
        },
        'library':library_login_info['data'],
        'header':token
    }
    # with open('{}.json'.format(xh),'wb') as f:
    #     f.write(json.dumps(back_info))

    return jsonify(back_info)
if __name__ == '__main__':
    xh='13010114033'
    print(xh[2:4])
    pwd='032050'
    auth(xh,pwd)