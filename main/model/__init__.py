#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: __init__.py.py
@time: 2019/3/6 0006 14:34
@desc:
"""
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
from .bind_info import bind_info
from .ecard_info import ecard_info
from .jw_info import jw_info
from .library_info import library_info
from .openid_info import openid_info
from ..AES import AESCipher
from ..comman import trueReturn,falseReturn




# test=aes.encrypt('230622199407032050')
# print(test)
# print(aes.decrypt(test))
def add_jw_pwd(studentid,type_info,jw_pwd,IDnumber,ecard_pwd='',library_pwd='',info=''):
    from main import create_app
    app = create_app()
    secert = app.config['JWC_PASSWORD_SECRET_KEY']
    aes = AESCipher(secert)  # 秘钥

    student_info=bind_info.query.filter_by(studentid=studentid).first()
    if not student_info:
        pwd_info=bind_info(studentid=studentid,
                              jw_pwd=aes.encrypt(jw_pwd),
                           ecard_pwd=ecard_pwd,
                              library_pwd=aes.encrypt(library_pwd),
                           student_info=info,
                           type_info=type_info,
                           IDnumber=aes.encrypt(IDnumber))
        pwd_info.save()
def add_jw_info(studentid,score,timetable,plan,timetable_plan=''):
    info=jw_info.query.filter_by(studentid=studentid).first()
    if not info:
        jwinfo=jw_info(studentid=studentid,
                         score=score,
                         timetable=timetable,
                         plan=plan,
                         timetable_plan=timetable_plan)
        jwinfo.save()
def get_pwd(studentid):
    from main import create_app
    app = create_app()
    secert = app.config['JWC_PASSWORD_SECRET_KEY']
    aes = AESCipher(secert)  # 秘钥
    student_info=bind_info.query.filter_by(studentid=studentid).first()
    if not student_info:
        return falseReturn(msg='账户不存在')
    else:
        if student_info.jw_pwd:
            jw_pwd=aes.decrypt(student_info.jw_pwd)
        else:
            jw_pwd=''
        if student_info.library_pwd:
            library_pwd=aes.decrypt(student_info.library_pwd)
        else:
            library_pwd=''
        if student_info.ecard_pwd:
            ecard_pwd=aes.decrypt(student_info.ecard_pwd)
        else:
            ecard_pwd=''
        pwd={
            'jw':jw_pwd,
            'lib':library_pwd,
            'ecard':ecard_pwd
        }
        return pwd


