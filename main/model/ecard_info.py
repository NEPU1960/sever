#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: ecard_info.py
@time: 2019/3/8 0008 08:08
@desc:
"""
from . import db

class ecard_info(db.Model):
    __tablename__ = 'ecard_info'
    studentid = db.Column(db.String(32), primary_key=True, unique=True,
                       nullable=False)
    ecard_sum = db.Column(db.String(20), nullable=True)




    def __init__(self, openid, ecard_sum):
        self.openid = openid
        self.ecard_sum=ecard_sum

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self