import requests
import bs4


def getsession():
    global login
    login = requests.session()
    session = login.get('http://jwgl.nepu.edu.cn')
    print(session.cookies)
    return login


def getcode():
    code = login.get("http://jwgl.nepu.edu.cn/verifycode.servlet")
    print(code.cookies)
    with open('yzm.jpg', 'wb')as f:
        f.write(code.content)
    return login


def login_jwc(yzm):
    data = {
        'USERNAME': '130101140323',
        'PASSWORD': '032050',
        'RANDOMCODE': yzm
    }
    success = login.post('http://jwgl.nepu.edu.cn/Logon.do?method=logon', data=data)
    hc = login.get('http://jwgl.nepu.edu.cn/Logon.do?method=logonBySSO')


def socer():
    cj_data = {
        'kksj': '2016-2017-1',
        'kcxz': '',
        'kcmc': '',
        'xsfs': 'qbcj'
    }
    get_kb = login.post('http://jwgl.nepu.edu.cn/xszqcjglAction.do?method=queryxscj', data=cj_data)
    print(get_kb.text)
    with open('cj.xml', 'wb') as f:
        f.write(get_kb.content)

    # print(get_kb.text)


def info():
    get_info = login.get("http://jwgl.nepu.edu.cn/xszhxxAction.do?method=addStudentPic&tktime=1536886386000")
    with open('get_info.xml', 'wb') as f:
        f.write(get_info.content)
    get_info_picture = login.get("jwgl.nepu.edu.cn/uploadfile/studentphoto/pic/130101140323.JPG")
    with open('zjz.jpg', 'wb')as f:
        f.write(get_info_picture.content)


def get_kb():
    get_info = login.get(
        "http://jwgl.nepu.edu.cn/tkglAction.do?method=kbxxXs" + "&istsxx=no" + "&xnxqh=2013-2014-1" + "&zc=" + "xs0101id=130101140323")
    with open('get_kb.xml', 'wb') as f:
        f.write(get_info.content)


def get_jxjh():
    get_jxjh = login.get("http://jwgl.nepu.edu.cn/pyfajhgl.do?method=toViewJxjhXs&tktime=1536886624000")
    with open('jxjh.xml', 'wb') as f:
        f.write(get_jxjh.conent)


getsession()
getcode()
yzm = input('yzm')
login_jwc(yzm)
socer()
info()
get_kb()
get_jxjh()