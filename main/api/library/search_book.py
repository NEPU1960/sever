#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: search_booke.py
@time: 2019/3/4 0004 08:44
@desc:
"""
import requests
import re
from bs4 import BeautifulSoup
from ..queue import celery
@celery.task
def get_name_book(book_name,page):
    '''图书检索'''
    session=requests.session()
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '210.46.140.21:8080',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    session.get('http://210.46.140.21:8080/opac/',headers=header)
    jsc=book_name.encode('gb2312')
    sort='kdm desc,datestr'.encode('gb2312')
    get_data={
        'ifface':'true',
        'jsc':jsc,
        'jstj':'title',
        'sort':sort,
        'orderby':'desc',#排序方式
        'geshi':'bgfm',
        'page':page
    }
    data={
    'page':'1',
    'oper':'1andSP',
    'addquery':'false',
    'changpage':'true',
    'geshi':'bgfm',
     'ifface':'true',
    'filterfl':'',
    'filterdcd':'',
    'filtersub':'',
     'filterkdm':'',
     'viewallsub':'false',
    'jstj':'title',
     'jsc':jsc,
}

    get_book_list=session.post('http://210.46.140.21:8080/opac/jdjsjg.jsp',data=get_data,headers=header).text
    #print(get_book_list)
    soup=BeautifulSoup(get_book_list,'lxml')
    table=soup.find_all('td',class_="fltd")
    #print(table)
    result=[]
    info_book={}
    for i in table[1:]:
        #print(i)
        herf=re.search('zyk[0-9]+',str(i)).group()#获取书地址
        text=i.get_text('\xa0','<br/>')
        new_text=text.split('\xa0')
        #print(new_text)
        try:
            info_book={
                    'book_name':new_text[0],
                    'book_number':new_text[1],
                    'book_auth':new_text[2],
                    'ISBN':new_text[4],
                    'book_press':new_text[6],
                    'date':new_text[8],
                    'herf':'http://210.46.140.21:8080/opac/ckgc.jsp?kzh='+herf

                }
            result.append(info_book)
        except:pass
    return result

def get_info(url):
    '''获取图书详细信息'''
    get=requests.get(url).text
    soup=BeautifulSoup(get,'lxml')
    table=soup.find_all('table')
    extend_info = {}
    for i in table[1:2]:
        tr=i.find_all('tr')
        info_1=tr[1].find_all('td')[1].get_text('','\xa0')
        info_2=tr[2].find_all('td')[1].get_text('','\xa0')
        info_3 = tr[3].find_all('td')[1].get_text()
        info_4=tr[4].find_all('td')[1].get_text('','\xa0')
        info_5 = tr[5].find_all('td')[1].get_text('', '\xa0')
        info_6 = tr[6].find_all('td')[1].get_text('', '\xa0')
        extend_info={
            'name':info_1.split('/')[0],
            'author':info_1.split('/')[1],
            'ISBN':info_2.split('/')[0],
            'pice':info_2.split('/')[1],
            '出版社':info_3.split(' ')[1],
            'time':info_3.split(' ')[2],
            'topic':info_4.split('/')[0],
            '页数':info_5,
            '摘要':info_6

        }
    return extend_info



if __name__ == '__main__':
    get_name_book('新媒体')