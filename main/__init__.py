#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/1/26 23:13
@desc:
'''
from flask import Flask

import os
from .config import shuju
from celery import Celery
from redis import Redis
from main.model import db

redis=Redis(host='127.0.0.1',port=6379,db=10)

def create_app():
    app=Flask(__name__)
    app.config.from_object(shuju)
    shuju.init_app(app)
    db.init_app(app)
    from .api import api
    app.register_blueprint(api,url_prefix='/api')
    return app
def make_celery(app):
    """
    integrate Celery with Flask
    http://flask.pocoo.org/docs/0.10/patterns/celery/#configuring-celery
    """
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


