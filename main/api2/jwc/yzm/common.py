# coding: utf-8
from numpy import array
from PIL import Image

def do_image_crop(img):
    """做图片切割，返回块图片列表"""
    start = 3
    width = 10
    top = 0
    height = 25

    img_list = []

    def init_table(threshold=135):
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        return table

    img = img.convert("L").point(init_table(), '1')
    for i in range(4):
        new_start = start + width * i
        box = (new_start, top, new_start + width, height)
        piece = img.crop(box)

        img_list.append(piece)

    return img_list

def smartcut(img):
    def init_table(threshold=135):
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        return table
    img = img.convert("L").point(init_table(), '1')
    '''
    :param img:
    :param outDir:
    :param count: 图片中有多少个图片
    :param p_w: 对切割地方多少像素内进行判断
    :return:
    '''
    count=4
    p_w=3
    w, h = img.size
    pixdata = img.load()
    eachWidth = int(w / count)
    beforeX = 0
    img_list=[]
    for i in range(count):

        allBCount = []
        nextXOri = (i + 1) * eachWidth

        for x in range(nextXOri - p_w, nextXOri + p_w):
            if x >= w:
                x = w - 1
            if x < 0:
                x = 0
            b_count = 0
            for y in range(h):
                if pixdata[x, y] == 0:
                    b_count += 1
            allBCount.append({'x_pos': x, 'count': b_count})
        sort = sorted(allBCount, key=lambda e: e.get('count'))
        nextX = sort[0]['x_pos']
        box = (beforeX, 0, nextX, h)
        piece = img.crop(box)
        img_list.append(piece)
        beforeX = nextX
    return img_list
def img_list_to_array_list(img_list):
    """PIL Image对象转array_list"""
    array_list = []
    for img in img_list:
        array_list.append(array(img).flatten())
    return array_list
if __name__ == "__main__":
    img=Image.open("cnmx.png")
    for im in do_image_crop(img):
        im.show()
        im.save('test.png')
