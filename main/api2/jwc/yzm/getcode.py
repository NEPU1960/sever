# coding: utf-8
import os
from main.api2.jwc import get_classifier_from_learn
from main.api2.jwc.yzm.common import *


def get_validate_code_from_image(img):
    img_piece = do_image_crop(img)
    X = img_list_to_array_list(img_piece)
    clf = get_classifier_from_learn()
    y = clf.predict(X)
    return "".join(y)

def test(sourse):
	name_list = os.listdir(sourse)
	num=0
	right=0
	for name in name_list:
		num=num+1
		img=Image.open(sourse+"/"+name)
		code = get_validate_code_from_image(img)
		if code==name[:4]:
			right=right+1
			#print("right")
		else:
			print("error:"+code+":"+name)
	print("共测试了"+str(num)+"张验证码")
	print("正确率:"+str(float(right/num)))   #输出准确率
if __name__ == '__main__':
    # test("images")
    img = Image.open("71.png")
    code = get_validate_code_from_image(img)
    print(code)
