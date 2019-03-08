#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: jw_info.py
@time: 2019/3/8 0008 08:12
@desc:
"""
from . import db

class jw_info(db.Model):
    __tablename__ = 'jw_info'
    studentid = db.Column(db.String(32), primary_key=True, unique=True,
                       nullable=False)
    score = db.Column(db.String(100), nullable=True)
    timetable=db.Column(db.String(100),nullable=True)#课表
    plan=db.Column(db.String(100),nullable=True)#教学计划
    timetable_plan=db.Column(db.String(100),nullable=True)



    def __init__(self,studentid,score,timetable,plan,timetable_plan):
        self.studentid = studentid
        self.bind_number=score
        self.timetable=timetable
        self.plan=plan
        self.timetable=timetable
        self.timetable_plan=timetable_plan

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self