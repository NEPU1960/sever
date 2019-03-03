# coding: utf-8
"""
labeled_images文件夹中：
1. 包含的文件夹名为标记名
2. 标记名下的文件夹中包含了学习图片
"""
import time
import os
from sklearn import svm
from PIL import Image
from numpy import array
#from utils import *

clf = None


def get_image_fit_data(dir_name):
    """读取labeled_images文件夹的图片，返回图片的特征矩阵及相应标记"""
    X = []
    Y = []
    name_list = os.listdir(dir_name)
    for name in name_list:
        if not os.path.isdir(os.path.join(dir_name, name)):
            continue
        image_files = os.listdir(os.path.join(dir_name, name))
        for img in image_files:
            i = Image.open(os.path.join(dir_name, name, img))
            X.append(array(i).flatten())
            Y.append(name)

    return X, Y


def get_classifier_from_learn():
    """学习数据获取分类器"""
    t = time.time()
    global clf
    if not clf:
        clf = svm.SVC(kernel='linear')  #线性准确率高一点
        #clf = svm.SVC()   #默认为rbf
        X, Y = get_image_fit_data("labeled_images")
        clf.fit(X, Y)
        print("学习用了"+str(time.time()-t)+"s")
    return clf      #学习到的矩阵


def main():
    clf = get_classifier_from_learn()
    print(type(clf))



if __name__ == '__main__':
    main()
