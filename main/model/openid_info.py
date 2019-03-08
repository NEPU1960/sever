#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: openid_info.py
@time: 2019/3/8 0008 07:58
@desc:
"""
from . import db

class openid_info(db.Model):
    __tablename__ = 'openid_info'
    openid = db.Column(db.String(32), primary_key=True, unique=True,
                       nullable=False)
    studentid = db.Column(db.String(20), nullable=True)
    bind_number=db.Column(db.String(20),nullable=True)#绑定次数
    user_type=db.Column(db.String(20),nullable=True)



    def __init__(self, openid, studentid,bind_number,user_type):
        self.openid = openid
        self.studentid = studentid
        self.bind_number=bind_number
        self.user_type=user_type

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self