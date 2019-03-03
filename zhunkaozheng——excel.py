#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: zhunkaozheng——excel.py
@time: 2019/2/25 0025 10:31
@desc:
"""
import xlrd
import json
from redis import Redis
r=Redis(host='182.254.226.202',port=6379,db=4)
def read_excel():
    workbook=xlrd.open_workbook('1.xls')
    sheet = workbook.sheet_by_index(0)
    all_nrows=sheet.nrows
    all_ncols=sheet.ncols
    for i in range(all_nrows):
        Style=sheet.cell(i, 0).value
        Department=sheet.cell(i, 1).value
        Specialty=sheet.cell(i, 2).value
        Classes=sheet.cell(i, 3).value
        Name=sheet.cell(i, 4).value
        StudentID=sheet.cell(i, 5).value
        Admission=sheet.cell(i, 6).value
        Search={'StudentID':StudentID,'name':Name,'style':Style,'Admission':Admission,'class':Classes,'department':Department,'specislty':Specialty}
        search=json.dumps(Search)
        print(search)
        r.set('cet'+str(StudentID),search,ex=3600)
    print(Search)
    c=json.dumps(Search)
    print(c)
    # with open('cet.json','wb') as f:
    #     f.write(c)
    # with open('cet.json', 'w') as json_file:
    #     json.dump(Search, json_file)

read_excel()