#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/3/4 23:14
@desc:教学计划
'''
from bs4 import BeautifulSoup
import time

header={
    'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Accept-Encoding':'gzip, deflate',
    'Host':'jwgl.nepu.edu.cn'
}
def get_jxjh(login):
    '''获取教学计划'''
    get_jxjh = login.get("http://jwgl.nepu.edu.cn/pyfajhgl.do?method=toViewJxjhXs&tktime=" + str(int(time.time())),
                         headers=header).text
    soup=BeautifulSoup(get_jxjh,'lxml')
    div=soup.find_all('div')
    cankao=['序号','学期','课程编号','课程名称','总学时','学分','课程体系','课程属性','方向','方向年度','考核方式','开课单位']
    info=[]
    for i in div[4]:
        table=i.find_all('tr')
        # print(table)
        for i in table:
            td=i.find_all('td')
            danwei={}
            for i in range(12):
                danwei[cankao[i]]=td[i].get_text('','\xa0')
                info.append(danwei)
    return info


if __name__ == '__main__':
    get_jxjh()