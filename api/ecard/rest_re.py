import requests
import re
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup
from struct import *
import random
import os
from PIL import Image
import math
import operator
from functools import reduce
import time
import io
import hashlib
import threading

class Ecard():
    # 程序初始化
    def __init__(self, name, psd):
        self.fee=0
        self.name = name
        self.passwd = psd
        self.s = requests.session()
        self.s.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
            'Host': 'yikatong.nepu.edu.cn',
        }
        self.s.auth=HTTPDigestAuth("178003070655", "032050")
        r = self.s.get("http://yikatong.nepu.edu.cn/homeLogin.action", )
    # 得到密码键盘并且生成字典
    def getmy(self):
        r = self.s.get("http://yikatong.nepu.edu.cn/getpasswdPhoto.action", )
        im = Image.open(io.BytesIO(r.content))
        imgry = im.convert('L')
        threshold = 118
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out = imgry.point(table, '1')
        l = []
        for n in range(4):
            for m in range(3):
                t = out.crop((10 + 36 * m, 36 + 36 * n, 10 + 23 + 36 * m, 36 + 23 + 36 * n))
                # print n,m
                # t.save(str(n)+str(m)+".png")
                l.append(hashlib.md5(t.tobytes()).hexdigest())
        k = {'1a5ab29e791b7759bf9f51da27af49fb': '7', '60d6fa3d848c9fc74347c3d7c9e86d5c': '0',
             '5860f6a18a4355bcbdb3b7f1c7d80787': '6', '5a68148875a7001a054bf1ab95c06126': '9',
             'e800012a5b5043b554076633bb161347': '5', '7e8010bb279a1bdc42174acc32b1d151': '3',
             '69e286508b8baed0a291fcf316867414': '8', '55ab3b7bb08dedb8f98ce7c72626e3b7': '1',
             '2e5103732bd2fa2f86498da3d655e1cc': '2', '34272c5cf72623e66dc362c666520cc4': '4',
             'd4f9349ba354b26bb4f9aacb4f0ad346': 'C', 'ddf37cebd7e30de1a1b605d895e1f5b6': 'X'}
        new_l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'C', 'X']
        l = map(lambda x: k[x], l)
        # {'C': 'C', 'X': 'X', '1': '2', '0': '7', '3': '0', '2': '6', '5': '1', '4': '4', '7': '8', '6': '9', '9': '5', '8': '3'}
        keys_map = dict(zip(l, new_l))
        return keys_map
    # 获取验证码，可能是我见过的最弱智的验证码了， 居然根据随机数生成，随机数固定，验证码固定
    def get_check_pic(self):
        self.s.get("http://yikatong.nepu.edu.cn/getCheckpic.action?rand=" + str(random.uniform(0, 1)),
                   )
    # 组装数据
    def get_data(self):
        passwdn = ""
        b = self.getmy()
        for i in self.passwd:
            passwdn += str(b[i])
        self.data = {
            "imageField.x": "20",
            "imageField.y": "12",
            "loginType": "2",
            "name": self.name,
            "passwd": str(passwdn),
            "rand": '0000',
            "userType": "1",
        }

    # 登入主页面
    def login(self):
        self.get_check_pic()
        self.get_data()
        print(self.data)
        url = 'http://yikatong.nepu.edu.cn/loginstudent.action'
        r = self.s.post(url, data=self.data)
    #获取个人信息
    def get_per_data(self):
        r = self.s.get("http://yikatong.nepu.edu.cn/accountcardUser.action", data=self.data, )  # 信息页面
        soup = BeautifulSoup(''.join(r.text))
        i = soup.find_all("td", attrs={"class", "neiwen"})
        account = soup.find_all("div", attrs={"align": "left"})
        self.account = account[1].string
        print(self.account)
        print(i[46].string)
    #获取当日流水
    def get_tday_data(self):
        self.data = {
            "account": self.account,
            "inputObject": "all",
            "Submit": "+%C8%B7+%B6%A8+",
        }
        # session.get("http://yikatong.nepu.edu.cn/accounttodayTrjn.action",auth=HTTPDigestAuth("ylli1_15","22422X@s"))
        r = self.s.post("http://yikatong.nepu.edu.cn/accounttodatTrjnObject.action", data=self.data,)  # 当日流水
        print(r.text)
    #获取间隔时间内的流水情况
    def get_mday_data(self):
        # 获取页面
        r = self.s.post("http://yikatong.nepu.edu.cn/accounthisTrjn.action", data=self.data,)
        url=self.get_re_url(r)
        # 提交第一次账号
        r = self.s.post("http://yikatong.nepu.edu.cn" + url, data=self.data, )
        url=self.get_re_url(r)
        # 提交日期
        self.data = {
            "inputEndDate": "20170930",
            "inputStartDate": "20170801",
        }
        r = self.s.post("http://yikatong.nepu.edu.cn" + url, data=self.data, )
        url=self.get_re_url(r)
        r = self.s.post("http://yikatong.nepu.edu.cn/accounthisTrjn.action" + url,)
        soup = BeautifulSoup(''.join(r.text))
        content = soup.find_all("td", attrs={"align:center"})
        r.encoding = "gb2312"
        print(r.text)
        #计算出总页数
        exp = re.compile("&nbsp;&nbsp;.(\d{1,2}).*&nbsp.*\d")
        PageCount = int(exp.findall(r.text)[0])
        return PageCount
    def get_single_page(self,i):
        print('开始了',i)
        self.data = {
            "pageNum": i
        }
        r = self.s.post("http://yikatong.nepu.edu.cn/accountconsubBrows.action", data=self.data,)
        if(not re.findall('table',r.text)):self.get_single_page(i)
        with open('page'+str(i)+'.txt','w') as f:
            f.write(r.text)
        soup = BeautifulSoup(''.join(r.text))
        content = soup.find_all("tr", attrs={"class": re.compile("^listbg")})
        print(time.time())
        lock.acquire()
        for j in content:
            fee_ = float(j.find_all("td")[6].string)
            if (fee_ < 0):
                self.fee += fee_
        lock.release()
    #获取跳转网址
    def get_re_url(self,r):
        # 操作正在进行获取查询url
        soup = BeautifulSoup(''.join(r.text))
        con = soup.find_all("form")[0]
        exp = re.compile('action="(.*)"\sid')
        url = exp.findall(str(con))[0]
        return url
    #挂失
    # def card_lock(self):
    #     # 挂失
    #     self.data = {
    #         "account": self.account,
    #     }
    #     r = session.post("http://ecard.cauc.edu.cn/accountDoLoss.action", data=self.data, )
    #     r.encoding = "gb2312"
    #     r = session.post("http://ecard.cauc.edu.cn/accountReportingloss.action", data=self.data,)
    #
    #     r.encoding = "gb2312"
if __name__ == '__main__':
    e = Ecard("178003070655", "032050")
    e.login()
    e.get_per_data()
    e.get_tday_data()
    count=e.get_mday_data()
    lock=threading.Lock()
    threads=[]
    for i in range(1,count+1):
        t=threading.Thread(target=e.get_single_page,args=(i,))
        t.start()