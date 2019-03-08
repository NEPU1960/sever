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

def add_jw_pwd(studentid,jw_pwd,ecard_pwd='',library_pwd='',student_info=''):
    studentid=bind_info.query.filter_by(studentid=studentid).first()
    if not studentid:
        pwd_info=bind_info(studentid=studentid,
                              jw_pwd=jw_pwd,
                           ecard_pwd=ecard_pwd,
                              library_pwd=library_pwd,
                           student_info=student_info)
        pwd_info.save()
    else:
        studentid.jw_pwd=jw_pwd
        studentid.update()




