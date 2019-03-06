#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: User.py
@time: 2019/3/6 0006 14:53
@desc:
"""
from . import db
class User(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
    openid = db.Column(db.String(32), primary_key=True, unique=True,
                       nullable=False)
    studentid = db.Column(db.String(20), nullable=True)
    jwpwd = db.Column(db.String(100), nullable=True)
    librarypwd = db.Column(db.String(100), nullable=True)
    ecardpwd = db.Column(db.String(100), nullable=True)
    def __init__(self,openid,studentid,jwpwd,librarypwd,ecardpwd):
        self.openid=openid
        self.studentid=studentid
        self.jwpwd=jwpwd
        self.librarypwd=librarypwd
        self.ecardpwd=ecardpwd
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
