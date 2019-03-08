#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: library_info.py
@time: 2019/3/8 0008 08:17
@desc:
"""
from . import db

class library_info(db.Model):
    __tablename__ = 'library_info'
    studentid = db.Column(db.String(32), primary_key=True, unique=True,
                       nullable=False)
    book_info = db.Column(db.String(32), nullable=True)




    def __init__(self, openid,book_info):
        self.openid = openid
        self.book_info=book_info

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self