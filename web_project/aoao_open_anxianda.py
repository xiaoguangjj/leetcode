# -*- coding:utf-8 -*-
import os
import sys
import time
import hashlib
import json,urllib2
import requests
import hmac, uuid
from collections import OrderedDict

class O3api(object):

    secret_key = '1bae8ba701fc65ab9f5372c889b67ed5'

    def getticket(self):
        """
        get ticket
        """
        tick = uuid.uuid1()
        ticket = str(tick).upper()
        return ticket

    def get_md5_value(self,data):
        myMd5 = hmac.new(str(self.secret_key), data.encode("utf-8"), hashlib.md5).hexdigest()
        return myMd5

    def get_json_value(self,data):
        json_data = json.dumps(data, ensure_ascii=True, default=str, separators=(',', ':'),
                               sort_keys=True)
        return json_data

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

    # tick = uuid.uuid1()
    # ticket = str(tick).upper()

    param = {

        "access_key": "dbda63a2c423d96f88c5a8fc5c22eac3",
        "cmd": "aoao.o2o.order.find",
        "ticket": "0F1F9139-1375-43BE-99C9-578D3490CE51",
        "time": 1506396365,
        "body": {
            "org_id": "59c220e99982692fcb7bf532",
            "start_date": 20160101,
            "end_date": 20160108,
            "page": 1,
            "limit": 10,
            "detail_mode": 2
        },
        "version": "v3.0",

    }

    spec = {

        "access_key": "dbda63a2c423d96f88c5a8fc5c22eac3",
        "cmd": "aoao.o2o.order.find",
        "ticket": "43480f98-8a0c-42b4-abd1-f1c826a89cc5",
        "time": 1506412148,
        "body": {
            "org_id": "59c220e99982692fcb7bf532"
        },
        "version": "v3.0"

    }

    params = {"access_key":"776633097bc9f3f4a985ecc1a0bcd0f7",
              "body":{"org_id":"59506623998269645c3a899c",
                      "org_order_id":"33333539",
                      "org_order_pushed_at":1506492580,
                      "contract_id":"5989184399826947aef9cf47",
                      "shipping_date":20170927,
                      "shipping_time":"16:14",
                      "goods":[{"name":"江西赣南脐橙8个约200g个（华北猫超）",
                                "price":100,
                                "quantity":2,
                                "specs":"8个/份"}],
                      "total_weight":0,
                      "total_volume":0,
                      "barcode":"33333537",
                      "preserve_mode":"",
                      "note":"",
                      "pickup_code":"",
                      "recv_code":"",
                      "order_amount":200,
                      "pay_type":3,
                      "cod_amount":0,
                      "pay_amount":0,
                      "address_id":"",
                      "consignor":{
                          "name":"易果生鲜昌平路店",
                          "phone":"18298004484",
                          "address":"北京市朝阳区阜通东大街1号院望京SOHOT1商业5层1503",
                          "address_detail":"",
                          "bd_poi":[116.482532,39.996149]},
                      "consignee":{"name":"张荣梅(自动)收",
                                   "phone":"12345678901",
                                   "address":"酒仙桥街道电子城IT产业园103号楼二层",
                                   "address_detail":"",
                                   "bd_poi":[116.504434,39.985479]},
                                    "city_code":"310000"
                      },
              "cmd":"aoao.o2o.order.create",
              "ticket":"EAB3901A-5260-4874-A79B-8E87DA353D69",
              "time":1506498018,
              "version":"v3.0",
              "sign":"6d97275a2b9ebaf5a31039733b10640e"
              }


    #验证md5 算法 有没有问题：用 "123456" 来验证
    datestr = "123456"
    mymd5 = server.get_md5_value(datestr)
    # print "79======sign:", mymd5

    #判断，排序，数据转换 算法 是否正确：用spec数据来验证
    date_json = server.get_json_value(param)
    # print "88========ksort->json_data:",date_json

    sign = server.make_sign(param)
    param["sign"] = sign
    print "sign:",sign
    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    r = requests.post(url,data=json.dumps(param), headers=headers)
    print r.json()
