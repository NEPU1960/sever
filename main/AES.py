#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: AES.py
@time: 2019/3/8 0008 08:56
@desc:
"""
from Crypto.Cipher import AES
from Crypto import Random
import base64
from main import create_app
app=create_app()
class AESCipher:

    """
    加密解密方法
    http://stackoverflow.com/questions/12524994
    """

    def __init__(self, key):
        self.BS = 16
        self.pad = lambda s: s + \
            (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        self.key = key

    def encrypt(self, raw):
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:]))
if __name__ == '__main__':
    print(app.config['JWC_PASSWORD_SECRET_KEY'])
    aes=AESCipher(app.config['JWC_PASSWORD_SECRET_KEY'])#秘钥
    test=aes.encrypt('230622199407032050')
    print(test)
    print(aes.decrypt(test))