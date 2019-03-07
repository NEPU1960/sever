#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/1/26 23:17
@desc:
'''
from celery.schedules import crontab
class shuju():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://wenepu:945999685@localhost:3306/wenepu'

    @staticmethod
    def init_app(app):
        pass

    # celery 配置
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERYBEAT_SCHEDULE = {
        'every-15-min-at-8-to-22': {
            'task': 'express.update',
            'schedule': crontab(minute='*/15', hour='8-22')
        },
        'every-1-hour': {
            'task': 'access_token.update',
            'schedule': crontab(minute=0, hour='*/1')
        },
        'every-9-am': {
            'task': 'library.return_books',
            'schedule': crontab(minute=0, hour='9')
        }
    }