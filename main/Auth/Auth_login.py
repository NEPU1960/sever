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
from main.api.ecard.login import ecard_login,get_tday_data,get_month_bill,get_ecard_info,loginout
from main.api.yjs.login import get_login,get_info,get_score,get_class,yjs_loginout
from ..api.jwc.get_kb import get_kb
from ..api.jwc.jxjh import get_jxjh
from ..api.jwc.score import socer
from main.comman import falseReturn,trueReturn
from main import create_app
from ..model import *
from . import Auth
from flask import request,jsonify
import json
import json
import time
#=create_app()
from ..pyJWT import create_token
from ..AES import AESCipher
library_status="0"
ecard_status="0"

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
            yjs_loginout()

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
            # add_jw_info(studentid=xh,score=str(score),timetable=str(kb),plan=str(jxjh)) #存储
            logout()
            jw_status = '1'
    print(back_info)
    sfz=back_info['身份证']
    '''一卡通系统故障，暂时不提供'''
    if 'X' in sfz:
        ecard_pwd=sfz[-7:-2] #一卡通密码获取
    else:
        ecard_pwd=sfz[-6:]
        '''一卡通系统验证'''
    name=ecard_login(xh,ecard_pwd)
    if name['status']==True:
        '''一卡通登录成功'''
        try:
            ecard_pwd=ecard_pwd
            ecard_ID=get_ecard_info()
            ecard_ye=ecard_ID['data']
            ecard_ID=str(ecard_ID['msg'])
            month_bill = get_month_bill(ecard_ID)
            day_bill=get_tday_data(ecard_ID)
            loginout()
            ecard_status='1'
            back_ecard={
                'yue': ecard_ye,
                'month_bill': month_bill['data'],
                'day_bill':day_bill['data']
            },
        except:
            ecard_status = '0'
            ecard_ye = ''
            back_ecard = {},
    else:
        ecard_pwd=None
        ecard_status = '0'
        ecard_ye=''
        back_ecard={},
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
        'ecard_status':ecard_status
    }
    token=create_token(xh,status)
    back_info={
        "jw":{
            "kb":kb,
            "score":score,
        },
        'library':library_login_info['data'],
        'ecard':back_ecard,
         'header':str(token, encoding='utf-8'),
        'library_status':library_status,
        'ecard_status':ecard_status,
        'jw_status':"1"
    }
    # with open('{}.json'.format(xh),'wb') as f:
    #     f.write(json.dumps(back_info))
    print(back_info)

    return jsonify(trueReturn(data=back_info))
