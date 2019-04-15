#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: classroom.py
@time: 2019/3/4 0004 14:19
@desc:空教室查询，详细信息需完善，暂不启用详细信息功能
"""
from main.api.jwc.jwc_login import login_jwc,logout
from bs4 import BeautifulSoup
import re
import time
from main.api.jwc.get_week import today_week
from main.comman import trueReturn,falseReturn
from ..queue import celery
header={
    'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Accept-Encoding':'gzip, deflate',
    'Host':'jwgl.nepu.edu.cn'
}
username='130101140323'
pwd='032050'
login1=login_jwc(username,pwd)
zc=today_week()['zhou']
xq=today_week()['week']
@celery.task
def te():
    '''查询空教室'''
    if login1['status']==False:
        return falseReturn(msg='暂时不能查询')
    else:
        login=login1['data']
        data={
            'typewhere':'xszq',
            'xnxqh':'2018-2019-2',
            'xqbh':'00001',
            'jxqbh':'',
            'jxlbh':'',
             'jsbh':'',
            'bjfh':'%3D',
            'rnrs':'',
            'jszt':'',
            'zc':zc,
            'zc2':zc,
            'xq':xq,
            'xq2':xq,
            'jc':'',
            'jc2':'',
        }
        back=login.post('http://jwgl.nepu.edu.cn/jiaowu/kxjsgl/kxjsgl.do?method=queryKxxxByJs&typewhere=xszq',data=data).text
        soup=BeautifulSoup(back,'lxml')
        table=soup.find_all('table')
        lb=[]
        sj=['','one','two','three','four','five','six']
        for i in table[:-3]:
            tr=i.find_all('tr')

            for i in tr[3:-2]:
                class_info = {}
                td=i.find_all('td')
                #print(td)
                jc = 0
                for i in td:
                    text=i.get_text()
                    # print(i.get_text('','\r\n\t\t\t\t\t\t\t\t'),jc)
                    if jc==0:
                        try:
                            room_name = re.search('((1H-)|(2A-)|(1F-)|(主楼.))[0-9]+',text).group() #匹配教学楼
                            roomID = re.search('ue=.\w+', str(i)).group()
                            # print(roomID[4:])
                            # print(room_name)
                            class_info['room'] = room_name
                            class_info['roomID']=roomID[4:]
                        except:
                              break
                    else:
                        jc_bh=sj[jc]#上课时间转编号
                        if '◆' in text:
                            class_info[jc_bh]='sk'#上课
                        elif 'Ｊ' in text:
                            class_info[jc_bh]='jy'#借用
                        elif 'Ｘ' in text:
                            class_info[jc_bh]='sd'#锁定
                        elif 'Κ' in text:
                            class_info[jc_bh]='ks'#考试
                        elif 'Ｇ' in text:
                            class_info[jc_bh] = 'guding'#固定调课
                        elif 'Ｌ' in text:
                            class_info[jc_bh] = 'linshi'#临时调课
                        else:class_info[jc_bh] = 'kx'#空闲
                    jc = jc + 1
                if class_info:
                    lb.append(class_info)
                else:
                    pass
        return trueReturn(data=lb)
def get_info_room(kc='0304',jsbh='00030'):
    '''查询教室占用情况'''#还需要完善，暂时不启用
    zc = today_week()['zhou']
    kcsj=str(today_week()['week'])+kc
    if login1['status']==False:
        return falseReturn(msg='暂时不能查询')
    else:
        login=login1['data']
        url = 'http://jwgl.nepu.edu.cn/jiaowu/kxjsgl/kxjsgl.do?method=goQueryjszyqk&xnxqh=2018-2019-2&jsbh='+jsbh+'&kcsj='+kcsj+'&typewhere=' \
               'xszq&startZc='+str(zc)+'&endZc='+str(zc)+'&startJc=&endJc=&startXq=1&endXq=1&jszt=&type=add'
        room_info=login.get(url).text
        soup=BeautifulSoup(room_info,'lxml')
        tr=soup.find_all('tr')
        new_lb=[]
        title={
            "周次：":"zc",
            "教室状态：":"status",
            "教室：":"classroom",
            "时间标志：":"sjbz",
            "备注：":"text",
            "时间：":"time",
            "申 请 人：":"shenqingren",
            "课程：":"class"
        }
        for i in tr[2:3]:
            td=i.find_all('td')

            for i in td[1:]:
                new_lb.append(i.get_text('','\r\n\t\t\t\t\t\t\t\t\t\t'))
        #print(new_lb)

        info={}
        a=0
        b=2
        print(new_lb)
        for i in range(8):
            info[title[new_lb[a]]]=new_lb[b]
            a=a+3
            b=b+3
        print(info)
        return trueReturn(data=info)

if __name__ == '__main__':
    star=time.time()
    c=te()
    print(c)
    d=get_info_room()
    print(d)
    logout()
    end=time.time()
    print(end-star)