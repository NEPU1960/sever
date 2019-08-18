#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019-08-17 22:42
@desc:
'''
from . import db

class AD(db.Model):
    __tablename__ = 'AD'
    Number = db.Column(db.String(20), primary_key=True, unique=True,
           nullable=False,doc='序号')
    Url = db.Column(db.String(100), nullable=True,doc='图片地址')
    Version=db.Column(db.String(100),nullable=True,doc='版本号')
    Text=db.Column(db.String(100),nullable=True,doc='备注')
    Date=db.Column(db.Date,nullable=True,doc='添加日期')
    def __init__(self, Number,Url,Version,Text,Date):
        self.Number = Number
        self.Url=Url
        self.Version=Version
        self.Text=Text
        self.Date=Date

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self