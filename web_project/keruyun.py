# -*- coding:utf-8 -*-
import hmac
import requests
import time
import json
import hashlib
import re
import uuid
import arrow
import csv

shop_state_dict = {
    0: 100,
    -1: -100,
}

header = {
    'Content-Type': 'application/json'
}
# 根据时间戳生成ttl
timestamp = arrow.utcnow().timestamp
ttl = long(timestamp)
print type(ttl)

time_stamp = long(time.time())
print ttl,time_stamp, "14"

#客如云账户
app_key = "3d16c7da42f7fd0de1c2081d9c7f63ca"
# secret_key = "3d7cc9119162270044f2538107133f0e"


# 从数据库中直接找到access_key和secret_key
access_key = "1b5ffeee2017c86377e39adf6855e07b"
secret_key = "9571304a90eee6ce4487c49ca7c3c87b"

#客如云测试环境商家
# mobile= '18515806118'
# code = '31553'
# url = 'https://seaguard-dev.o3cloud.cn/1.0'
# seller_id = '59ef052199826902b79dc091'
# account_code = '50012'

#拉夏测试商家
mobile= '13535356868'
code = '31554'
url = 'https://seaguard-dev.o3cloud.cn/1.0'
seller_id = '5a026f0099826953a7667c81'
account_code = '50012'
mobile = '13535356868'

#客如云正式环境商家
# access_key = '9b08b25d807c13ab89d84bfcdd67d3f1'
# secret_key = 'ceb7a5478be62d5ffb733d5703c6332a'
# mobile = '15184315363'
# code = '31810'
# url = 'http://godview.meishisong.cn/message/'
# account_code = '50012'
# seller_id = '59f2b3d33d65ce5a3d2eee20'


def get_data(data):
    """

    :return:
    """
    json_data = json.dumps(data, ensure_ascii=True, default=str, separators=(',', ':'),
                               sort_keys=True)
    return json_data

def get_sha(json_data):

    hash = hashlib.sha256()
    hash.update(json_data.encode('utf-8'))
    return hashlib.sha256(json_data).hexdigest()

# def make_sign(data):
#     """
#     make sign
#     """
#     json_data = json.dumps(data, ensure_ascii=True, default=str, separators=(',', ':'),
#                                sort_keys=True)
#     return hmac.new(secret_key,json_data.encode("utf-8"), hashlib.sha256).hexdigest()
#
# def get_token():
#     """
#
#     :return:
#     """
#     data = {
#     "appKey" : "dd46f1fa380b125d25df64e65dd74519",
#     "shopIdenty" : 810063966,
#     "version" : "1.0",
#     "timestamp" : ttl,
#     }
#     sign = make_sign(data)
#     print sign,"43"

def shop_detail():
    """

    :return:
    """
    data = {
        "appKey": "3d16c7da42f7fd0de1c2081d9c7f63ca",
        "shopIdenty": 810063966,
        "timestamp": ttl,
        "version": "1.0",
    }
    token = "203a2740510bbdea7c9bd79bbf09c73c"
    app = "appKey3d16c7da42f7fd0de1c2081d9c7f63cashopIdenty810063966timestamp{0}version1.0{1}".format(ttl, token)
    sign = get_sha(app)
    print "102",sign

    rep = requests.post(url='https://testopenapi.keruyun.com/open/v1/shop/shopdetails?appKey=3d16c7da42f7fd0de1c2081d9c7f63ca&shopIdenty=810063966&version=1.0&timestamp={0}&sign={1}'.format(timestamp,sign), headers=header)
    # print rep.status_code
    ret = rep.content
    print ret,len(ret),"110"
    shops = rep.json()
    return shops

def shop_list():
    """

    :return:
    """
    data = {
        "appKey": "3d16c7da42f7fd0de1c2081d9c7f63ca",
        "shopIdenty": 810063966,
        "timestamp": ttl,
        "version": "1.0",
    }
    token = "203a2740510bbdea7c9bd79bbf09c73c"
    app = "appKey3d16c7da42f7fd0de1c2081d9c7f63cashopIdenty810063966timestamp{0}version1.0{1}".format(ttl, token)
    sign = get_sha(app)
    print "102",sign

    rep = requests.post(url='https://testopenapi.keruyun.com/open/v1/shop/shoplist?appKey=3d16c7da42f7fd0de1c2081d9c7f63ca&shopIdenty=810063966&version=1.0&timestamp={0}&sign={1}'.format(timestamp,sign), headers=header)
    # print rep.status_code
    ret = rep.content
    print ret,len(ret),"110"
    shops = rep.json()
    return shops
    # print shops,"112"
    # for shop in shops.data:
    #     # status = shop.get("status")
    #     print shop
    # print rep.json().get("result")[0].get("status"),"109"
    # print ret.decode(), "110",type(rep.content)
    # print rep.content

# 根据uuid生成msg_id
msg_id = str(uuid.uuid4())
# 根据时间戳生成ttl
timestamp = arrow.utcnow().timestamp
ttl = timestamp


def compute_x_auth_sign(secret_key, msg_id, ttl):
    """
    生成X-AUTH的函数
    :param secret_key: secret_key
    :param msg_id: uuid
    :param ttl: timestamp
    :return: md5加密的32位hash值
    """
    return hmac.new(str(secret_key), '{0}:{1}'.format(msg_id, ttl), hashlib.md5).hexdigest()


def compute_x_token_sign(secret_key, access_token, msg_id, ttl):
    """
    生成X-TOKEN的函数
    :param secret_key: secret_key
    :param access_token: access_token
    :param msg_id: uuid.uuid4()
    :param ttl: timestamp
    :return: md5加密的32位hash值
    """
    return hmac.new(str(secret_key), '{0}:{1}:{2}'.format(access_token, msg_id, ttl), hashlib.md5).hexdigest()


# 构造x-auth请求方式的headers
auth_headers = {
    'X-APP-KEY': access_key,
    'X-MSG-ID': '{0},{1}'.format(msg_id, ttl),
    'X-AUTH': compute_x_auth_sign(secret_key, msg_id, ttl),
    'Content-Type': 'application/json'
}


def get_verify_code():
    """
    调用io通用服务的发送短信接口发送验证码
    :return: verify_code
    """
    # 根据2.14.2发送短信接口的接口文档构造请求参数
    # sms_params = {
    #     'mobile': '15219066560',
    #     'type': 1,
    #     'code': '31128'
    # }
    sms_params = {
        'mobile': mobile,#15992454233安鲜达',
        'type': 1,
        # 'account_code':account_code,
        'code': code,#31536'安鲜达'
    }
    # 根据url发送post请求，获取响应
    r = requests.post(url="{0}/io/sms/send".format(url), data=json.dumps(sms_params), headers=auth_headers)
    print r.content, "68"
    data = json.loads(r.content)
    print type(data),"70"
    # 从响应中取出验证码
    verify_code = str(re.findall(r'\d+', data["message"])[0])
    print verify_code, "78"
    return verify_code


def get_access_token():
    """
    登陆，获取响应中的access_token
    :return: access_token
    """
    # 获取短信验证码
    verify_code = get_verify_code()
    # 根据2.10.1登录接口构造登陆的请求参数
    # login_params = {
    #     'mobile': '15219066560',
    #     'code': '31128',
    #     'verify_code': verify_code
    # }

    login_params = {
        'mobile': mobile,#15992454233'
        'code': code,#31536'
        'verify_code': verify_code,
        'account_code': account_code,
    }
    # 根据url发送post请求，获取响应
    # req = requests.post(url='https://seaguard-dev.o3cloud.cn/1.0/auth/login', data=json.dumps(login_params), headers=auth_headers)

    req = requests.post(url='{0}/auth/login'.format(url), data=json.dumps(login_params), headers=auth_headers)
    print req.content, "91"
    # 从响应中取出access_token
    access_token = json.loads(req.content)['access_token']
    return access_token


# 根据access_token 构造token_headers
access_token = get_access_token()
token_headers = {
    'X-APP-KEY': access_key,
    'Content-Type': 'application/json',
    'X-TOKEN': '{0},{1}'.format(access_token, compute_x_token_sign(secret_key, access_token, msg_id, ttl)),
    'X-MSG-ID': '{0},{1}'.format(msg_id, ttl),
}


def get_shop_list():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44', headers=token_headers)
    rep = requests.get(url='{0}/shops/?seller_id=59506623998269645c3a899c'.format(url), headers=token_headers)
    print rep.status_code
    print rep.content

# 598bacfe3d65ce1285999871

def get_shop_detail():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/581b639b3d65ce45cced7bf8', headers=auth_headers)
    rep = requests.get(url='{0}/shops/59f15a5b998269377ca0c3d4'.format(url), headers=token_headers)
    print rep.status_code
    print rep.content


def create_shops():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44', headers=token_headers)
    shops = shop_detail()
    shop = shops.get("result")[0]
    print shop,shop.get("commercialID"),"262"
    params = {
        "org_shop_id":shop.get("commercialID"),
        "seller_id": "59ef052199826902b79dc091",#59506623998269645c3a899c",#str(shop.get("commercialID")),
        "city_code":shop.get("cityCode"),
        "city_name": shop.get("cityName"),
        "name": shop.get("commercialName"),
        "linkman":shop.get("commercialContact"),
        "mobile": shop.get("commercialPhone"),
        "tel": shop.get("commercialPhone"),
        "state": shop_state_dict[shop.get("status")],
        "address":shop.get("commercialAddress"),
        "address_detail":shop.get("address_detail"),
        "bd_poi":shop.get("latLong"),#[116.52138157875468,39.91015228489031],
    }

    rep = requests.post(url='{0}/shops/'.format(url), data = json.dumps(params),headers=token_headers)
    print rep.status_code
    print rep.content
    # print "265",shop[0]


def update_shops():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44', headers=token_headers)
    shops = shop_detail()
    shop = shops.get("result")

    lat = [float(shop.get("latlong").split(',')[1]),float(shop.get("latlong").split(',')[0])]
    print shop.get("latlong"),"283",[float(shop.get("latlong").split(',')[1]),float(shop.get("latlong").split(',')[0])]
    params = {
        "org_shop_id": str(shop.get("commercialId")),
        "city_code": shop.get("cityCode"),
        "city_name": shop.get("cityName"),
        "name": shop.get("commercialName"),
        "linkman": shop.get("commercialContact"),
        "mobile": shop.get("commercialPhone"),
        # "tel": "",
        # "state": shop_state_dict[shop.get("status")],
        "address": shop.get("commercialAddress"),
        # "address_detail": "",#shop.get("commercialAddress"),
        "bd_poi":lat,#[116.52138157875468,39.91015228489031],
    }
    # rep = requests.post(url='https://seaguard-dev.o3cloud.cn/1.0/shops/59ef052199826902b79dc091', data = json.dumps(params),headers=token_headers)
    rep = requests.post(url='{0}/shops/59f15a5b998269377ca0c3d4'.format(url),data = json.dumps(params),headers=token_headers)

    print rep.status_code
    print rep.content

def create_shops_csv():
    """

    :return:
    """
    csvFile = open('/data/haidilao.csv', "r")
    csv_reader = csv.reader(csvFile)
    line_num = 0
    for row in csv_reader:
        line_num += 1
        if (line_num != 1):
            print row,row[0],"314"
            org_shop_id = str(row[0].decode('GB2312').encode('utf-8'))
            shop_name = str(row[1].decode('GB2312').encode('utf-8'))
            mobile = str(row[2].decode('GB2312').encode('utf-8'))
            link_man = str(row[3].decode('GB2312').encode('utf-8'))
            poi = str(row[4].decode('GB2312').encode('utf-8'))
            adress = str(row[5].decode('GB2312').encode('utf-8'))

            # lat = [float(poi.split('[')[1].split(',')[0]),float(poi.split(',')[1].split(']')[0])]
            lat = [float(poi.split(',')[0]),float(poi.split(',')[1])]
            print lat,"323",type(float(poi.split(',')[0]))
            params = {
                "org_shop_id":org_shop_id,
                "seller_id": '59ef052199826902b79dc091'.format(seller_id),#59506623998269645c3a899c',",#str(shop.get("commercialID")),
                "city_code":"110000",
                "city_name": "北京市",
                "name": shop_name,
                "linkman":link_man,
                "mobile": mobile,
                "address":adress,
                # "address_detail":"",#加上此项，会让界面显示的地址信息 变成 地址 + 详细地址
                "bd_poi":lat,#[116.52138157875468,39.91015228489031],
            }
            #
            rep = requests.post(url='{0}/shops/'.format(url), data = json.dumps(params),headers=token_headers)
            # print rep.status_code
            print rep.content

def update_shops_csv(line):
    csvFile = open('/data/haidilao.csv', "r")
    csv_reader = csv.reader(csvFile)
    line_num = 0
    for row in csv_reader:
        line_num += 1
        if (line_num == line):
            print row,row[0],"314",line
            org_shop_id = str(row[0].decode('GB2312').encode('utf-8'))
            shop_name = str(row[1].decode('GB2312').encode('utf-8'))
            mobile = str(row[2].decode('GB2312').encode('utf-8'))
            link_man = str(row[3].decode('GB2312').encode('utf-8'))
            poi = str(row[4].decode('GB2312').encode('utf-8'))
            adress = str(row[5].decode('GB2312').encode('utf-8'))
            lat = [float(poi.split(',')[0]),float(poi.split(',')[1])]

            params = {
                "org_shop_id":org_shop_id,
                "seller_id": '59ef052199826902b79dc091',#59506623998269645c3a899c',",#str(shop.get("commercialID")),
                "city_code":"110000",
                "city_name": "北京市",
                "name": shop_name,
                "linkman":link_man,
                "mobile": mobile,
                "address":adress,
                "address_detail":"",
                "bd_poi":lat,#[116.52138157875468,39.91015228489031],
            }
            # rep = requests.post(url='https://seaguard-dev.o3cloud.cn/1.0/shops/59ef052199826902b79dc091', data = json.dumps(params),headers=token_headers)
            rep = requests.post(url='{0}/shops/59f2ef289982690866090c03'.format(url),data = json.dumps(params),headers=token_headers)

            print rep.status_code
            print rep.content

def create_shops_laxia():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44', headers=token_headers)
    # shops = shop_detail()
    # shop = shops.get("result")[0]
    # print shop,shop.get("commercialID"),"262"
    # params = {
    #     "org_shop_id":'53205320',
    #     "seller_id": "5a026f0099826953a7667c81",#59506623998269645c3a899c",#str(shop.get("commercialID")),
    #     "city_code":'131000',
    #     "city_name": '廊坊市',
    #     "name": '河北廊坊新华路万千百货LA',
    #     "linkman":'王书娟',
    #     "mobile": '15030653000',
    #     # "tel": shop.get("commercialPhone"),
    #     "state": 100,
    #     "address":'河北廊坊市广阳区新华路与永丰道交叉口西侧万达百货4F',
    #     # "address_detail":shop.get("address_detail"),
    #     "bd_poi":[116.713778,39.527606],
    # }
    params = {
        "org_shop_id":'6563',
        "seller_id": "5a026f0099826953a7667c81",#59506623998269645c3a899c",#str(shop.get("commercialID")),
        "city_code":'110000',
        "city_name": '北京市',
        "name": '北京丹棱街欧美汇LA',
        "linkman":'李春梅',
        "mobile": '15811310482',
        # "tel": shop.get("commercialPhone"),
        "state": 100,
        "address":'北京市海淀区丹棱街1号欧美汇购物中心B1层',
        # "address_detail":shop.get("address_detail"),
        "bd_poi":[116.321165,39.985382],
    }
    rep = requests.post(url='{0}/shops/'.format(url), data = json.dumps(params),headers=token_headers)
    print rep.status_code
    print rep.content

def update_shops_laxia():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44', headers=token_headers)
    # shops = shop_detail()
    # shop = shops.get("result")[0]
    # print shop,shop.get("commercialID"),"262"
    params = {
        "org_shop_id":'53205320',
        # "shop_id": "5a026f0099826953a7667c81",#59506623998269645c3a899c",#str(shop.get("commercialID")),
        "city_code":'131000',
        "city_name": '廊坊市',
        "name": '河北廊坊新华路万千百货LA',
        "linkman":'王书娟',
        "mobile": '15030653000',
        # "tel": shop.get("commercialPhone"),
        "state": 100,
        "address":'河北廊坊市广阳区新华路与永丰道交叉口西侧万达百货4F',
        # "address_detail":shop.get("address_detail"),
        "bd_poi":[116.713778,39.527606],
    }

    rep = requests.post(url='{0}/shops/5a02b52d99826953a76687fe'.format(url), data = json.dumps(params),headers=token_headers)
    print rep.status_code
    print rep.content

if __name__ == '__main__':
    # shop_list() #客如云商家列表
    # shop_detail()#客如云商家详情
    # create_shops()#从客如云平台导入嗷嗷系统
    # get_shop_detail()#获取商户详情
    # update_shops()#编辑商户
    get_shop_list()#获取商户列表
    # create_shops_csv()#从csv文件里获取商户并创建商户
    # update_shops_csv(6) #编辑数据第几行数据
    # create_shops_laxia()
    # update_shops_laxia()
