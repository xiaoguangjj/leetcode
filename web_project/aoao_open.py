# -*- coding:utf-8 -*-
import os
import sys
import time
import hashlib
import md5
import base64
import json,urllib2
import requests
import hmac, uuid
from collections import OrderedDict
import collections

class O3api(object):

    access_key = '4b25521b23f968aa40b9995f560e82ac'
    secret_key = '5817c61ef5339c3265665b718b1c8244'
    spec = {
        "org_id":"5978480999826931309aacc1",
        "org_order_id":str(int(time.time())),
        "contract_id": '5983ed34998269427d89bf98',
        "city_code":'110000',
        "goods": {
            "name": '香辣螃蟹',
            "specs":'箱',
            "quantity":1,
            "price": 100,
        },
        "barcode": str(int(time.time())),
        "pay_type": 1,
        "consignor": {
            "name": '张三',
            "address":'西二旗西路29号',
            'phone': '13141458800',
        },
        "consignee":{
            "name": "lisi",
            "phone": "13141458811",
            "address":"西二旗西路28号",
        },
    }

    tt = str(int(time.time()))
    myMd5 = hashlib.md5()
    myMd5.update(tt)
    myMd5_Digest = myMd5.hexdigest()
    tick  = myMd5_Digest.upper()
    ticket = tick[:8]+'-'+tick[8:12]+'-'+tick[12:16]+'-'+tick[16:20]+'-'+tick[20:]
    # tick = uuid.uuid1()
    # ticket = tick.upper()
    params = {
        "access_key": "4b25521b23f968aa40b9995f560e82ac",
        "cmd": "aoao.o2o.order.create",
        "ticket": ticket,
        "time": int(time.time()),
        "body":{

        },
        "version": "v3.0",
        }

    def api(self):
        print self.access_key

    def get_md5_value(self,src):
        myMd5 = hashlib.md5()
        myMd5.update(src)
        myMd5_Digest = myMd5.hexdigest()
        return myMd5_Digest

    def make_sign(self, data):
        """
        make sign
        """
        json_data = json.dumps(data, ensure_ascii=True, default=str, separators=(',', ':'),
                               sort_keys=True)
        return hmac.new(str(self.secret_key), json_data.encode("utf-8"), hashlib.md5).hexdigest()

if __name__ == "__main__":

    server = O3api()
    access_key = '4b25521b23f968aa40b9995f560e82ac'
    secret_key = '5817c61ef5339c3265665b718b1c8244'
    spec = {
            "barcode": str(int(time.time())),
            "city_code":'110000',
            "consignee": {
                "address":"西二旗西路28号",
                "name": "lisi",
                "phone": "13141458811",
            },
            "consignor": {
                "address":'西二旗西路29号',
                "name": '张三',
                'phone': '13141458800',
            },
            "contract_id": '5983ed34998269427d89bf98',
            "goods": [{
                "name": '香辣螃蟹',
                "price": 100,
                "quantity":1,
                "specs": '500g',
                }
            ],
            "org_id": "5978480999826931309aacc1",
            "org_order_id": str(int(time.time())),
            "pay_type": 1,
    }

    tt = str(int(time.time()))
    myMd5 = hashlib.md5()
    myMd5.update(tt)
    myMd5_Digest = myMd5.hexdigest()
    tick = myMd5_Digest.upper()
    ticket = tick[:8]+'-'+tick[8:12]+'-'+tick[12:16]+'-'+tick[16:20]+'-'+tick[20:]
    # tick = uuid.uuid1()
    # ticket = str(tick).upper()
    params = {
        "access_key": "4b25521b23f968aa40b9995f560e82ac",
        "body": {
            "barcode": str(int(time.time())),
            "city_code":'110000',
            "consignee": {
                "address":"西二旗西路28号",
                "name": "lisi",
                "phone": "13141458811",
            },
            "consignor": {
                "address":'西二旗西路29号',
                "name": '张三',
                'phone': '13141458800',
            },
            "contract_id": '5983ed34998269427d89bf98',
            "goods": [{
                "name": '香辣螃蟹',
                "price": 100,
                "quantity":1,
                "specs": '500g',
                }
            ],
            "org_id": "5978480999826931309aacc1",
            "org_order_id": str(int(time.time())),
            "pay_type": 1,
        },
        "cmd": "aoao.o2o.order.create",
        "ticket": ticket,
        "time": int(time.time()),
        "version": "v3.0",
        }

    for key in sorted(params.iterkeys()):
        print "%s:%s" % (key, params[key])

    param = collections.OrderedDict(sorted(params.items(), key=lambda t: t[0]))

    sign = server.make_sign(params)
    params["sign"] = sign
    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    r = requests.post(url,data=json.dumps(params),headers=headers)
    print r.json(),"154",sign,"172",param


