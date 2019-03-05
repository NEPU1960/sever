#!/usr/bin/python
# -*- coding:gbk -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/3/4 00:07
@desc:
'''
import re
import copy
def get_zhou_list(c):
    te=re.search('周.*',c).group()
    new=c.replace(te,'')
    t=new.split('-')
    zhou=[]
    # for i in range(int(t[-2]),int(t[:-1])+1):
    #     print(i)
    #     zhou.append(i)
    if ',' in new:
        d=new.split(',')
        del_dist = copy.deepcopy(d)
        for i in d:
            if '-' in str(i):
                del_dist.remove(i)
                # del_dist.append(i)
                zhou_info=i.split('-')
                for j in range(int(zhou_info[0]),int(zhou_info[-1])+1):
                    # d.remove(i)
                    del_dist.append(str(j))
    elif '-' in new:
        zhou_info = new.split('-')
        del_dist=[]
        for j in range(int(zhou_info[0]), int(zhou_info[-1]) + 1):
            # d.remove(i)
            del_dist.append(str(j))
    else:
        del_dist=[new]
    return del_dist




