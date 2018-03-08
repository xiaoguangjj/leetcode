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
import logging

class O3Api(object):

    # secret_key = '5817c61ef5339c3265665b718b1c8244'
    def getticket(self):
        """
        get ticket
        """
        tick = uuid.uuid1()
        ticket = str(tick).upper()
        return ticket

    def make_sign(self, data):
        """
        make sign
        """
        json_data = json.dumps(data, ensure_ascii=True, default=str, separators=(',', ':'),
                               sort_keys=True)
        return hmac.new(str(self.secret_key), json_data.encode("utf-8"), hashlib.md5).hexdigest()

if __name__ == "__main__":

    server = O3Api()
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
                "phone": '13141458800',
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
            "org_order_pushed_at": int(time.time()),
            "pay_type": 1,
        },
        "cmd": "aoao.o2o.order.create",
        "ticket": server.getticket(),
        "time": int(time.time()),
        "version": "v3.0",
    }

    sign = server.make_sign(params)
    params["sign"] = sign

    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    r = requests.post(url,data=json.dumps(params), headers=headers)
    print r.json()

    spec = {
        "access_key": "4b25521b23f968aa40b9995f560e82ac",
        "body": {
            "org_id": "5978480999826931309aacc1",
            "org_order_id": str(int(time.time())),
            "page": 1,
            "limit": 10,
            "detail_mode": 2,
        },
        "cmd": "aoao.o2o.order.find",
        "ticket": server.getticket(),
        "time": int(time.time()),
        "version": "v3.0",
    }

    sign = server.make_sign(spec)
    spec["sign"] = sign
    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    # r = requests.post(url,data=json.dumps(spec), headers=headers)
    # print r.json()

    close = {
        "access_key": "4b25521b23f968aa40b9995f560e82ac",
        "body": {
            "org_id": "5978480999826931309aacc1",
            "org_order_id": "1505273166",
            "closed_note": "顾客关闭",
        },
        "cmd": "aoao.o2o.order.close",
        "ticket": server.getticket(),
        "time": int(time.time()),
        "version": "v3.0",
    }

    sign = server.make_sign(close)
    close["sign"] = sign
    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    # r = requests.post(url,data=json.dumps(close), headers=headers)
    # print r.json()

    location = {
        "access_key": "4b25521b23f968aa40b9995f560e82ac",
        "body": {
            "org_id": "5978480999826931309aacc1",
            "org_order_ids": [
                "1505273166",
            ]
        },
        "cmd": "aoao.o2o.order.location",
        "ticket": server.getticket(),
        "time": int(time.time()),
        "version": "v3.0",
    }

    sign = server.make_sign(location)
    location["sign"] = sign
    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    # r = requests.post(url,data=json.dumps(location), headers=headers)
    # print r.json()

    confirm = {
        "access_key": "4b25521b23f968aa40b9995f560e82ac",
        "body": {
            "org_id": "5978480999826931309aacc1",
            "org_order_id": "1505273166",
        },
        "cmd": "aoao.o2o.order.status.confirm",
        "ticket": server.getticket(),
        "time": int(time.time()),
        "version": "v3.0",
    }

    sign = server.make_sign(confirm)
    confirm["sign"] = sign
    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    # r = requests.post(url,data=json.dumps(confirm), headers=headers)
    # print r.json()
