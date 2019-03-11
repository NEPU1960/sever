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
    '''课表中周数解析为列表'''
    if '单' or '双' in c:
        if '单' in c:
            print('单周',c)
            te = re.search('单.*', c).group()
            new = c.replace(te, '')
            t = new.split('-')
            zhou = []
            if ',' in new:
                d = new.split(',')
                del_dist = copy.deepcopy(d)
                for i in d:
                    if '-' in str(i):
                        del_dist.remove(i)
                        # del_dist.append(i)
                        zhou_info = i.split('-')
                        if int(zhou_info[0])%2==0:
                            if int(zhou_info[-1])%2==0:
                                for j in range(int(zhou_info[0])+1, int(zhou_info[-1]),2):
                                    # d.remove(i)
                                    del_dist.append(str(j))
                            else:
                                for j in range(int(zhou_info[0])+1, int(zhou_info[-1])+1,2):
                                    # d.remove(i)
                                    del_dist.append(str(j))
                        else:
                            if int(zhou_info[-1])  % 2== 0:
                                for j in range(int(zhou_info[0]), int(zhou_info[-1]),2):
                                    # d.remove(i)
                                    del_dist.append(str(j))
                            else:
                                for j in range(int(zhou_info[0]), int(zhou_info[-1])+1,2):
                                    # d.remove(i)
                                    del_dist.append(str(j))
            elif '-' in new:
                zhou_info = new.split('-')
                del_dist = []
                if int(zhou_info[0]) % 2 == 0:
                    if int(zhou_info[-1]) % 2 == 0:
                        for j in range(int(zhou_info[0]) + 1, int(zhou_info[-1]), 2):
                            # d.remove(i)
                            del_dist.append(str(j))
                    else:
                        for j in range(int(zhou_info[0]) + 1, int(zhou_info[-1]) + 1, 2):
                            # d.remove(i)
                            del_dist.append(str(j))
                else:
                    if int(zhou_info[-1]) % 2 == 0:
                        for j in range(int(zhou_info[0]), int(zhou_info[-1]), 2):
                            # d.remove(i)
                            del_dist.append(str(j))
                    else:
                        for j in range(int(zhou_info[0]), int(zhou_info[-1]) + 1, 2):
                            # d.remove(i)
                            del_dist.append(str(j))
            else:
                del_dist = t
        elif '双' in c:
            print('双周', c)
            te = re.search('双.*', c).group()
            new = c.replace(te, '')
            zhou = []
            if ',' in new:
                d = new.split(',')
                del_dist = copy.deepcopy(d)
                for i in d:
                    if '-' in str(i):
                        del_dist.remove(i)
                        # del_dist.append(i)
                        zhou_info = i.split('-')
                        if int(zhou_info[0]) % 2 == 0:
                            if int(zhou_info[-1]) % 2 == 0:
                                for j in range(int(zhou_info[0]) , int(zhou_info[-1])+ 1, 2):
                                    # d.remove(i)
                                    del_dist.append(str(j))
                            else:
                                for j in range(int(zhou_info[0]), int(zhou_info[-1]) , 2):
                                    # d.remove(i)
                                    del_dist.append(str(j))
                        else:
                            if int(zhou_info[1]) % 2 == 0:
                                for j in range(int(zhou_info[0])+1, int(zhou_info[-1])+1, 2):

                                    # d.remove(i)
                                    del_dist.append(str(j))
                            else:
                                for j in range(int(zhou_info[0])+1, int(zhou_info[-1]), 2):
                                    # d.remove(i)
                                    del_dist.append(str(j))
            elif '-' in new:
                zhou_info = new.split('-')
                del_dist = []
                if int(zhou_info[0]) / 2 == 0:
                    if int(zhou_info[-1]) / 2 == 0:
                        for j in range(int(zhou_info[0]), int(zhou_info[-1]) + 1, 2):
                            # d.remove(i)
                            del_dist.append(str(j))
                    else:
                        for j in range(int(zhou_info[0]), int(zhou_info[-1]), 2):
                            # d.remove(i)
                            del_dist.append(str(j))
                else:
                    if int(zhou_info[-1]) / 2 == 0:
                        for j in range(int(zhou_info[0]) + 1, int(zhou_info[-1]) + 1, 2):
                            # d.remove(i)
                            del_dist.append(str(j))
                    else:
                        for j in range(int(zhou_info[0]) + 1, int(zhou_info[-1]), 2):
                            # d.remove(i)
                            del_dist.append(str(j))
            else:
                del_dist = t

    else:
        te=re.search('周.*',c).group()
        new=c.replace(te,'')
        t=new.split('-')
        zhou=[]
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
            del_dist=t
    return del_dist
if __name__ == '__main__':
    print(get_zhou_list('3-15单周'))




