#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: find_password.py
@time: 2019/3/4 0004 19:45
@desc:
"""
import requests
def find_jwc_pwd():
    '''教务处密码找回'''
    url='http://jwgl.nepu.edu.cn/framework/enteraccount.jsp'
    data={
        'account':'130101140323'
    }
    session=requests.session()
    # info=session.post(url,data).text

    data2={
        'account':'130101140323',
        'sfzjh':'230622199407032050'
    }
    info=session.post('http://jwgl.nepu.edu.cn/yhxigl.do?method=resetPasswd',data2)
    if info.status_code==200:
        if '出错页面' in info.text:
            return {'msg': '学号输入错误'}
        elif '身份证件号输入错误或者你在系统中没有身份证号' in info.text:
            return {'msg': '身份证号输入错误'}
        else:
            print(info.text)
            return {'msg':'密码已重置为身份证后六位'}
    else:
        return {'msg':404}
if __name__ == '__main__':

    find_jwc_pwd()