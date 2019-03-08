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
    studentid = db.Column(db.String(32), primary_key=True, unique=True,
           nullable=False)
    jw_pwd = db.Column(db.String(20), nullable=True)
    ecard_pwd=db.Column(db.String(20),nullable=True)
    library_pwd=db.Column(db.String(20),nullable=True)
    student_info=db.Column(db.String(20),nullable=False)




    def __init__(self, studentid,jw_pwd,ecard_pwd,library_pwd,student_info):
        self.studentid = studentid
        self.jw_pwd=jw_pwd
        self.ecard_pwd=ecard_pwd
        self.library_pwd=library_pwd
        self.student_info=student_info

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self