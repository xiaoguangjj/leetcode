# -*- coding:utf-8 -*-

#引入人脸识别 SDK
from aip import AipFace
import urllib,urllib2,sys
import ssl
import base64
import requests
import json
#定义常量
APP_ID = '10315355'
API_KEY = 'uW0kjxcbwXIVhfZj3TsHlV6w'
SECRET_KEY = 'BDr5Q7Q9ncLXtLh8iomlt2mqDlzFNKdA'
URL = 'https://aip.baidubce.com/rest/2.0/face/v1/detect'

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"

#初始化AipFace对象
aipFace = AipFace(APP_ID,API_KEY,SECRET_KEY)

#读取图片
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

#定义参数变量
options = {
    'max_face_num':1,
    'face_fileds':"age,beauty,experssion,faceshape",
}
#调用人脸属性检测接口
result = aipFace.detect(get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face1.jpg'),options)
# print result

#调用人脸两两对比接口
result = aipFace.match([
    get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face1.jpg'),
    get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face2.png'),
    # get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face.png'),


])
print result,"41"

##该参数如果不填则使用默认值
options = {
    'user_top_num':0,
    'face_top_num':1,
    'top_num':1,
}

result = aipFace.verifyUser(
    'uid1',
    'group1',
    get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face1.jpg'),
    options
)
print result,'63'

result = aipFace.identifyUser(
    'group1',
    get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face1.jpg'),
    options
)
print result,"65"

result = aipFace.addUser(
    'uid1',
    'user info',
    'group1',
    get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face1.jpg')
)
print result,'70'

result = aipFace.updateUser(
    'uid1',
    'user info',
    'group1',
    get_file_content('/Users/user/myproject/aoao/script_o3_api/templates/face1.jpg')
)
print result,"79"

result = aipFace.getUser('uid1')
print result,"82"

# result = aipFace.getUser('uid1','group1')
# print result,'85'

#该参数如果不慎则使用默认值
options = {
    'start':0,
    'num':100,
}

result = aipFace.getGroupList(options)
print result,"94"

result = aipFace.getGroupUsers('group1',options)
print result,'97'

#二进制方式打开图片文件
def picture(token):
    # request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
    request_url = 'https://aip.baidubce.com/rest/2.0/face/v1/detect'

    f = open('/Users/user/myproject/aoao/script_o3_api/templates/48043.jpg','rb')
    # img = base64.b16encode(f.read())
    img = f.read()
    # print img,'26'
    # exit()
    # params = {"image":img,"top_num":5}
    params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
    params = urllib.urlencode(params)

    # access_token = '24.271aeb29697210a9e143980d26b78b8e.2592000.1512207577.282335-10315355'
    access_token = token
    request_url = request_url + "?access_token="+access_token
    request = urllib2.Request(url=request_url,data=params)
    request.add_header('Content-Type','application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        print content

def face_check():
    """

    :return:
    """
    url = 'https://aip.baidubce.com/rest/2.0/face/v1/detect'
    # access_token = '24.271aeb29697210a9e143980d26b78b8e.2592000.1512207577.282335-10315355'
    header ={'Content-Type':'application/x-www-form-urlencoded', 'access_token':'24.271aeb29697210a9e143980d26b78b8e.2592000.1512207577.282335-10315355'}
    f = open('/Users/user/myproject/aoao/script_o3_api/templates/face.jpg','r')
    # img = base64.b16encode(f.read())
    img = f.read()

    params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
    rep = requests.post(url=url, data = json.dumps(params),headers=header)
    print rep.status_code
    print rep


if __name__ == '__main__':

    #client_id 为官网获取的AK，client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(API_KEY,SECRET_KEY)
    request = urllib2.Request(host)
    request.add_header('Content-Type','application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()

    if(content):
        token = content[1:88].split(':')[1][1:-1]
        # picture(token)
        print token

    # face_check()

