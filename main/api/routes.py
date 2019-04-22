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
from .jwc.classroom import te,get_info_room
from .yjs.login import get_login,get_score,get_class
from .news_notice.notice_list import nepu_notice
from .news_notice.get_list import nepu_news
from ..pyJWT import verify_bearer_token
# from .news_notice.jiexi import about
from .jwc.get_week import today_week

from .news_notice.jiexi import about
import ast

app=create_app()

@api.route('/news/newslist')
def get_news_list():
    news_list=nepu_news(1)
    return jsonify(news_list)
@api.route('/news/jiexi')
def get_news_text():
    get=request.args.getlist('url')
    print(get)
    news_text=about(get[0])
    print(news_text)
    return jsonify(news_text)

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
@api.route('/jwc/score_updata',methods=['GET'])
def score_updata():
    '''更新成绩'''
    # xh='161201440101'
    print(request.headers.get("Authorization"))
    xh=verify_bearer_token(request.headers.get("Authorization"))['sub']#获取token信息
    print(xh)
    pwd_info=get_pwd(xh)
    print(pwd_info)
    jw_pwd=pwd_info['jw']
    if xh[2:4] == '80':
        '''研究生登陆'''
        login=get_login(xh,jw_pwd)
        if login['status']==True:
            back=get_score()
            return jsonify(trueReturn(data=back))
        else:
            return jsonify(falseReturn(msg=login))
    else:
        # pwd_info=get_pwd(xh)
        # jw_pwd=pwd_info['jw']
        login=login_jwc(xh,jw_pwd)
        if login['status']==True:
            back=socer(login['data'])
            return jsonify(trueReturn(data=back,msg='1'))
        else:
            if login['msg']=='教务系统暂时无法访问':
                return jsonify(falseReturn(msg='教务系统暂时无法访问，成绩更新失败'))
            else:
                return jsonify(falseReturn(msg='密码已修改，需重新登录教务系统'))


@api.route('/jwc/kb_updata',methods=['GET'])
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
@api.route('/kong',methods=['GET'])
def kjs():
    '''空教室查询'''
    back=te()
    back=back
    redis.set('kong',json.dumps(back),ex=36000)
    return jsonify(back)
@api.route('/classinfo',methods=['GET'])
def classinfo():
    '''空教室具体信息查询'''
    back = get_info_room()
    return jsonify(back)
@api.route('start')
def start():
    try:
        info = verify_bearer_token(request.headers.get("Authorization"))['sub']  # 获取token信息
    except:
        return "未绑定"
    week=today_week()


