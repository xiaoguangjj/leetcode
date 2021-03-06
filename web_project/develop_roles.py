# -*- coding:utf-8 -*-
import hashlib
import hmac
import json
import re
import uuid
import arrow
import requests
from bson import ObjectId
import time

#测试环境aoao_admin
# access_key = "53269c5a1905d3de1ba2782b6e2a8626"
# secret_key = "8ee401282e13cb5d8b6c81882ad26ca8"

#正式环境
access_key = "3e04a3cfa3a76682bd723b086b79763d"
secret_key = "6c1034fa711240a0ff971b0998b0134e"

# 根据uuid生成msg_id
msg_id = str(uuid.uuid4())
# 根据时间戳生成ttl
timestamp = arrow.utcnow().timestamp
ttl = timestamp

account_code = '50013' #jxg账号

# url = "https://seaguard-dev.o3cloud.cn/1.0"
# url = "http://127.0.0.1:8080/1.0"
url = "https://seaguard.o3cloud.cn/1.0" #aoao-seagurd正式环境


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
    sms_params = {
        # 'mobile': '15992454233',
        'type': 1,
        # 'code': '31536'
        'account_code': account_code,
    }
    # 根据url发送post请求，获取响应
    r = requests.post(url="{0}/io/sms/send".format(url), data=json.dumps(sms_params), headers=auth_headers)
    print r.content,"68"
    data = json.loads(r.content)
    # 从响应中取出验证码
    verify_code = str(re.findall(r'\d+', data["message"])[0])
    print verify_code, "78"
    return verify_code


def get_access_token():
    """
    登陆，获取响应中的access_token
    :return: access_token
    """
    # 获取短信验证码,
    verify_code = get_verify_code()
    # 根据2.10.1登录接口构造登陆的请求参数

    login_params = {
        'account_code': account_code,
        'verify_code': verify_code
    }
    # 根据url发送post请求，获取响应
    # req = requests.post(url='https://seaguard-dev.o3cloud.cn/1.0/auth/login',
    # data=json.dumps(login_params),
    # headers=auth_headers)

    req = requests.post(url='{0}/auth/login'.format(url), data=json.dumps(login_params), headers=auth_headers)
    print req.content, "91"
    # 从响应中取出access_token
    access_token = json.loads(req.content)['access_token']
    return access_token


# 根据access_token 构造token_headers
# access_token = get_access_token()# 需要验证码

token_headers = {
    # 'X-APP-KEY': access_key,
    'Content-Type': 'application/json',
    # 'X-TOKEN': '{0},{1}'.format(access_token, compute_x_token_sign(secret_key, access_token, msg_id, ttl)),
    # 'X-MSG-ID': '{0},{1}'.format(msg_id, ttl),
    'X-APP-KEY': 'c5d70a20b9d332116ddeb4a276260763',
    'X-TOKEN': '89b2ddb8f83955c790c5428767271031,d383a2984a1d67b3da7c6fba2760880a',
    'X-MSG-ID': '1513070834468,1513070834468'
}


def get_shop_list():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=token_headers)
    rep = requests.get(url='{0}/shops/?seller_id=59506623998269645c3a899c', headers=token_headers)
    print rep.status_code
    print rep.content

# 598bacfe3d65ce1285999871

def get_shop_detail():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/581b639b3d65ce45cced7bf8', headers=auth_headers)
    rep = requests.get(url='{0}/shops/595067a4998269645c3a8e2b', headers=token_headers)
    print rep.status_code
    print rep.content

def create_shops():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=token_headers)
    params = {
        "seller_id": "59506623998269645c3a899c",
        "city_code":"110000",
        "city_name":"北京市",
        "name":"京京",
        "linkman":"13141458801",
        "bd_poi":[116.52138157875468,39.91015228489031],
    }
    rep = requests.post(url='{0}/shops/'.format(url), data=json.dumps(params), headers=token_headers)
    print rep.status_code
    print rep.content

def update_shops():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=auth_headers)
    # rep = requests.get(url='https://seaguard-dev.o3cloud.cn/1.0/shops/?seller_id=581a7e4a3d65ce45cced7a44',
    # headers=token_headers)
    params = {
        # "shop_id": "59ed97ea99826902d9dce0f7",
        "city_code":"110000",
        "city_name":"北京市",
        "name":"京京",
        "linkman":"京京",
        "mobile":"13141458801",
        "address_detail":"通惠大厦",
        "bd_poi":[116.52138157875468,39.91015228489031],
    }
    rep = requests.post(url='{0}/shops/59ed97ea99826902d9dce0f7'.format(url),
                        data=json.dumps(params),
                        headers=token_headers)
    print rep.status_code
    print rep.content


def create_develop_detail():
    param = {
        'org_id': '59c89c423d65ce4bf134ed9a', #商户id
        'org_type': 2,
        'operator_id': '5a2f7c0d3d65ce5ede8a0b7c',
        'state': 100,
        'live_mode': True,
    }

    param = json.dumps(param)
    rep = requests.post(url='{0}/develops/'.format(url), headers=token_headers, data=param)
    # print rep.status_code
    print rep
    print rep.content
    # print '123'

def get_develop_detail():
    """

    :return:
    """
    rep = requests.get(url='{0}/develops/5a1fbe1f3d65ce56e202de08'.format(url), headers=token_headers)
    print rep
    print rep.content


def get_develop_list():
    """

    :return:
    """
    get_develop_info = {
        "org_id":'59f2b3d33d65ce5a3d2eee20',
        # 'page': 1,
        # 'limit': 2,
    }
    print json.dumps(get_develop_info)
    rep = requests.get(url='{0}/develops/?org_id={1}'.format(url, '5a2f7c0d3d65ce5ede8a0b7c'), headers=token_headers)
    print rep
    print rep.content


def update_develop_detail():
    # rep = requests.get(url='http://127.0.0.1:8080/1.0/shops/581b639b3d65ce45cced7bf8', headers=auth_headers)
    param = {
        'org_id': '59f2b3d33d65ce5a3d2eee20',
        "operator_id" : '5a2f7c0d3d65ce5ede8a0b7c',
        'hook_url':"https://testopenapi.keruyun.com/open/v1/delivery/status/push",
        # 'access_key': '7e990d38012fbc92d24cc26329a924ac',
        # 'secret_key': 'e523058f27be7815fb9995c25630f352'
    }

    rep = requests.post(url='{0}/develops/59f6c58a3d65ce5a3d948b09'.format(url),
                        data=json.dumps(param),
                        headers=token_headers)
    print rep.status_code, "234"
    print rep.content, "235"
    print "236:", rep


def ksort(d):
    return ['{0}{1}'.format(k, d[k].encode('utf-8')) for k in sorted(d.keys()) if k != 'sign']

def generate_get_sign( params, secret_key):
        """
        生成请求token的签名
        :param params:
        :param secret_key:
        :return:
        """
        sign_str = ''.join(ksort(params)) + secret_key
        sha256_sign = hashlib.sha256(sign_str).hexdigest()
        return sha256_sign

def keruyun_token():
    """

    :return:
    """
    token_url = "https://openapi.keruyun.com/open/v1/token/get"
    url = "{0}?appKey={1}&shopIdenty={2}&version=1.0&timestamp={3}" \
                  "&sign={4}".format(token_url, access_key, org_shop_id, str(int(time.time())),
                                     generate_get_sign(params, secret_key))

    headers = {
                'Content-Type': 'application/json'
            }

if __name__ == '__main__':
    # get_shop_list()
    # get_shop_detail()
    # get_delelop()
    # create_shops()
    # update_shops()

    #开发者接口
    # create_develop_detail() #开发者详情
    get_develop_list() #开发者列表
    # update_develop_detail() #编辑开发者信息
