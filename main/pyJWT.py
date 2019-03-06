#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: pyJWT.py
@time: 2019/3/5 0005 20:50
@desc:
"""
import jwt
import time


# 使用 sanic 作为restful api 框架
def create_token():
    # grant_type = request.json.get('grant_type')
    # username = request.json['username']
    # password = request.json['password']
    # if grant_type == 'password':
    #     account = verify_password(username, password)
    # elif grant_type == 'wxapp':
    #     account = verify_wxapp(username, password)
    # if not account:
    #     return {}
    payload = {
        "iss": "gusibi.com",
        "iat": int(time.time()),
        "exp": int(time.time()) + 8,
        "aud": "qkyzs",
        "sub": '178003070655',
        "username": '戚开元',
        "type""y"
        "scopes": ['open']
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    print(token)
    # return True, {'access_token': token, 'account_id': '178003070655'}
    return token


def verify_bearer_token(token):
    #  如果在生成token的时候使用了aud参数，那么校验的时候也需要添加此参数
    payload = jwt.decode(token, 'secret', audience='qkyzs', algorithms=['HS256'])

    if payload:
        print(payload)
        return True, token
    return False, token

create_token()
token=b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJndXNpYmkuY29tIiwiaWF0IjoxNTUxNzkwOTQ1LCJleHAiOjE1NTE3OTA5NTMsImF1ZCI6InFreXpzIiwic3ViIjoiMTc4MDAzMDcwNjU1IiwidXNlcm5hbWUiOiJcdTYyMWFcdTVmMDBcdTUxNDMiLCJ0eXBleXNjb3BlcyI6WyJvcGVuIl19.0xRl9f648409i9YAtILwVMn3fjmGhKAxXHV2cWg1Evc'

verify_bearer_token(token)
