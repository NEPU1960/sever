#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: get_password.py
@time: 2019/2/28 0028 08:42
@desc:识别一卡通密码键盘
"""

import os
from io import BytesIO
import time
import hashlib
import cv2
import numpy as np
from PIL import Image
import requests
import matplotlib.pyplot as plt
def get_new_pwd(md):
    search = {
        '64815e2fc717e5868bc67d964cb3cd5e': '0',
        '1daab1e22cb8de4fe73abdac88d4c4a2': '1',
        '7e84d3f49d0c97537fd5bcf4a1fcaa76': '2',
        'e68198bcb7298f0c123e05b832ab4998': '3',
        '8013c24d8a013a0a335e4b24f060266f': '4',
        '1d01f46dfbc4ed3acfcb9e85b0147fad': '5',
        'a2cc12324f78396a8a4d363f9bb49203': '6',
        '01cd6bb152f14d2ce9b36c889e3dcb0a': '7',
        'fbd3fb739f08aaede71b890e3dc72e35': '8',
        'a0009c7c70d5f65f3e2bd7bac7a6381a': '9'
    }
    return search[md]


def get_pay_keyboard_number_location(im, pwd):
    numbers = set(list(pwd))
    templates = {}
    positions = {}
    lie={}
    nimgpath ='' # 数字图片不在同目录时使用
    #nimgpath='/main/api2/ecard/get_pwd'
    for i in numbers:
        templates[i] = os.path.join(nimgpath, "{}.png".format(i))
    #img_rgb = cv2.imread(im)
    img_rgb = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

    for teNum, tepath in templates.items():
        template = cv2.imread(tepath)
        h,w = template.shape[:-1]

        # res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        res=cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
        threshold = .95  # 匹配度参数，1为完全匹配
        loc = np.where(res >= threshold)
        if len(loc) > 0:
             positions[teNum] = (list(loc[::-1][0])[0],list(loc[::][0])[0])
             lie={ '1': ([10], [36]), '5': ([9], [144]), '6': ([81], [106]), '3': ([81], [71])}
        else:
            print("Can not found number: [{}] in image: [{}].".format(tepath, im))
            return {'msg':'密码未能完全识别'}
    d={}
    new_pwd=[]
    #print(positions)
    for i in pwd:
        s = str(positions[i])
        m = hashlib.md5(s.encode())
        new_pwd.append(get_new_pwd(m.hexdigest()))

    return ''.join(new_pwd)

if __name__ == "__main__":
    url='http://yikatong.nepu.edu.cn/getpasswdPhoto.action'
    pw=requests.get(url)
    im = Image.open(BytesIO(pw.content))
    ls = get_pay_keyboard_number_location(im, '032050')
    print(ls)
    #print(ls)
    # for i in range(6):
    #     print(list(ls[i]))