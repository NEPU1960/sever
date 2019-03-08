#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: bind_info.py
@time: 2019/3/8 0008 08:18
@desc:
"""
from . import db

class bind_info(db.Model):
    __tablename__ = 'bind_info'
    studentid = db.Column(db.String(20), primary_key=True, unique=True,
           nullable=False,doc='学号')
    jw_pwd = db.Column(db.String(100), nullable=True,doc='教务密码')
    ecard_pwd=db.Column(db.String(100),nullable=True,doc='一卡通密码')
    library_pwd=db.Column(db.String(100),nullable=True,doc='图书馆密码')
    student_info=db.Column(db.String(300),nullable=True,doc='个人信息')
    IDnumber=db.Column(db.String(60),nullable=False,doc='身份证号')
    type_info=db.Column(db.String(20),nullable=False,doc='账号类型')
    def __init__(self, studentid,jw_pwd,ecard_pwd,library_pwd,student_info,type_info,IDnumber):
        self.studentid = studentid
        self.jw_pwd=jw_pwd
        self.ecard_pwd=ecard_pwd
        self.library_pwd=library_pwd
        self.student_info=student_info
        self.type_info=type_info
        self.IDnumber=IDnumber

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self