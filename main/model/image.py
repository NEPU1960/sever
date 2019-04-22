#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: image.py
@time: 2019/4/20 0020 10:48
@desc:
"""
from . import db

class Image(db.Model):
    __tablename__ = 'Image'
    imagename = db.Column(db.String(32), primary_key=True, unique=True,
                       nullable=False)
    image_url=db.Column(db.String(32),nullable=False)
    image_status = db.Column(db.String(32), nullable=False)

    def __init__(self, imagename, image_url,image_status):
        self.imagename = imagename
        self.image_url=image_url
        self.image_status=image_status

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self