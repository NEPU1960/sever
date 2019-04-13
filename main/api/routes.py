# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: routes.py
@time: 2019/3/6 0006 15:07
@desc:
"""
from . import api
import requests
from flask import request
from main.pyJWT import  verify_bearer_token
from main.api.zhaopin.get_list import nepu_news
from main import create_app,redis
from flask import request,jsonify
from ..Auth.get_openid import openid
from ..pyJWT import verify_bearer_token
import json
from ..comman import falseReturn,trueReturn
from .library.search_book import get_name_book,get_info
from ..model import get_pwd
from .jwc.jwc_login import login_jwc,logout
from .jwc.score import socer
from .jwc.get_kb import get_kb
from .jwc.classroom import te
from .yjs.login import get_login,get_score,get_class
import ast

app=create_app()

@api.route('/',methods=['POST'])
def hello_world():
    '''
    获取header，根据header判断账号类型
    1、根据账号类型返回图片地址
    2、返回一卡通，图书馆信息
    3、根据数据库是否更新过，返回成绩信息
    4、返回弹窗提示信息
    5、浮动窗口信息
    '''
@api.route('/news/jwc_login')
def get_news_list():
    te = request.headers['Authorization'][7:]
    c=verify_bearer_token(te)
    print(c)
    return '1'
@api.route('/library/search',methods=['POST'])
def search_library():
    '''图书馆检索'''
    book_name=request.get_json()['book_name']
    page=request.get_json()['page']
    print(book_name)
    shearch_result=get_name_book(book_name,page=1)
    return jsonify(trueReturn(data=shearch_result))
@api.route('/library/get_search_info',methods=['POST'])
def book_info():
    '''获取书籍详细信息'''
    book_url=request.get_json()['herf']
    book_info=get_info(book_url)
    return jsonify(trueReturn(book_info))
@api.route('jwc/score_updata',methods=['GET'])
def score_updata():
    '''更新成绩'''
    xh='178003070655'
    pwd_info=get_pwd(xh)
    jw_pwd=pwd_info['jw']
    if xh[2:4] == '80':
        login=get_login(xh,jw_pwd)
        if login['status']==True:
            back=get_score()
        else:
            return jsonify(login)
    else:
        pwd_info=get_pwd(xh)
        jw_pwd=pwd_info['jw']
        login=login_jwc(xh,jw_pwd)
        if login['status']==True:
            back=socer(login['data'])

        else:
            if login['msg']=='教务系统暂时无法访问':
                return jsonify(falseReturn(msg='教务系统暂时无法访问，成绩更新失败'))
            else:
                return jsonify(falseReturn(msg='密码已修改，需重新登录教务系统'))
    return jsonify(trueReturn(data=back))

@api.route('jwc/kb_updata',methods=['GET'])
def kb_updata():
    '''更新课表'''
    xh = '178003070655'
    pwd_info = get_pwd(xh)
    jw_pwd = pwd_info['jw']
    pwd_info=get_pwd(xh)
    jw_pwd=pwd_info['jw']
    if xh[2:4] == '80':
        login = get_login(xh, jw_pwd)
        if login['status']==True:
            back=get_class()
        else:
            return jsonify(login)
    else:
        login=login_jwc(xh,jw_pwd)
        if login['status']==True:
            back=get_kb(login['data'],xh)

        else:
            if login['msg']=='教务系统暂时无法访问':
                return jsonify(falseReturn(msg='教务系统暂时无法访问，成绩更新失败'))
            else:
                return jsonify(falseReturn(msg='密码已修改，需重新登录教务系统'))
    return jsonify(trueReturn(data=back))
@api.route('kong',methods=['GET'])
def kjs():
    '''空教室查询'''
    back=redis.get('kong')
    back=json.loads(back)
    if not back:
        back=te()
        back=back
        redis.set('kong',json.dumps(back),ex=36000)
    return jsonify(back)


