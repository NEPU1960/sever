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
def create_token(IDnumber,status):
    payload = {
        "iss": "wenepu",
        "iat": int(time.time()),
        "aud": "qkyzs",
        "sub": IDnumber,
        "username": '戚开元',
        "status":status
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    print(token)
    # return True, {'access_token': token, 'account_id': '178003070655'}
    return token


def verify_bearer_token(token):
    #  如果在生成token的时候使用了aud参数，那么校验的时候也需要添加此参数


    try:
        payload = jwt.decode(token, 'secret', audience='qkyzs', algorithms=['HS256'])
        if payload:
            return payload
        else:
            raise jwt.InvalidTokenError

    except jwt.ExpiredSignatureError:
        return 'Token过期'

    except jwt.InvalidTokenError:
        return '无效Token'

if __name__ == '__main__':
    status={
        'ecard':'0'
    }
    token=create_token('178003070655',status)
    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3ZW5lcHUiLCJpYXQiOjE1NTE5Mjc4NTAsImF1ZCI6InFreXpzIiwic3ViIjoiMTc4MDAzMDcwNjU1IiwidXNlcm5hbWUiOiJcdTYyMWFcdTVmMDBcdTUxNDMiLCJzdGF0dXMiOnsiZWNhcmQiOiIwIn19.X_oGr8n6wIPLeFeZ6irGnNQpe5x0btmHWwUuPTO_Oqk'
    print(verify_bearer_token(token))
