# -*- coding:utf-8 -*-
import os
import sys
import time
import hashlib
import md5
import base64
import json,urllib2
import requests


class O3api(object):

    access_key = '4b25521b23f968aa40b9995f560e82ac'
    secret_key = '5817c61ef5339c3265665b718b1c8244'
    spec = {
        'partner_id':'5978480999826931309aacc1',
        'partner_order_id':str(int(time.time())),
        'city_code':'110000',
        'goods': {
            'partner_goods_id': '598046a29982697250d79a4e',
            'name': '香辣螃蟹',
            'specs':'箱',
            'quantity':1,
            'price': 100,
        },
        'consignee':{
            'name': '张三',
            'address':'西二旗西路29号',
        },
        'extra_services':{
            'pa':{
                'receipt_amount':100,
                'pay_amount':10,
            },
            'delivery':{
                'delivery_partner_id':'597841b7998269234438935a',
                'production_code':'5983eaea998269427d89ba9c',
            },
        },
    }

    tt = str(int(time.time()))
    myMd5 = hashlib.md5()
    myMd5.update(tt)
    myMd5_Digest = myMd5.hexdigest()
    tick  = myMd5_Digest.upper()
    ticket = tick[:8]+'-'+tick[8:12]+'-'+tick[12:16]+'-'+tick[16:20]+'-'+tick[20:]
    params = {
        'access_key': '4b25521b23f968aa40b9995f560e82ac',
        'body':spec,
        'cmd': 'aoao.o2o.order.create',
        'time': int(time.time()),
        'version': 'v2.0',
        'ticket': ticket,
        }

    def api(self):
        print self.access_key

    def get_md5_value(self,src):
        myMd5 = hashlib.md5()
        myMd5.update(src)
        myMd5_Digest = myMd5.hexdigest()
        return myMd5_Digest

if __name__ == "__main__":

    server = O3api()

    print "75",server.params
    param = sorted(server.params.items(),key=lambda d:d[1],reverse = False)
    jo = json.dumps(param)
    secret_key = '5817c61ef5339c3265665b718b1c8244'
    sign_pure = {'md5',jo,secret_key}
    m = hashlib.md5()
    m.update(jo)
    m.hexdigest()
    sign = m.hexdigest()
    server.params['sign'] = sign
    # url = 'https://openapi.o3cloud.cn'
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    r = requests.post(url,data = server.params)
    print r.json()
    server.api()
