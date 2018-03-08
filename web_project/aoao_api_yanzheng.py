# -*- coding:utf-8 -*-
import os
import sys
import time
import hashlib
import json,urllib2
import requests
import hmac, uuid
from collections import OrderedDict
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

class O3api(object):

    # secret_key = '1bae8ba701fc65ab9f5372c889b67ed5'
    secret_key = '9f91e3bdb86cf95bb05cc4e938f5191f'

    def getticket(self):
        """
        get ticket
        """
        tick = uuid.uuid1()
        ticket = str(tick).upper()
        return ticket

    def get_json_value(self, data):
        json_data = json.dumps(data, ensure_ascii=True, default=str, separators=(',', ':'),
                               sort_keys=True)
        return json_data

    def get_md5_value(self, data):
        myMd5 = hmac.new(str(self.secret_key), data.encode("utf-8"), hashlib.md5).hexdigest()
        return myMd5

    def make_sign(self, data):
        """
        make sign
        """
        json_data = json.dumps(data, ensure_ascii=True, default=str, separators=(',', ':'),
                               sort_keys=True)
        return hmac.new(str(self.secret_key), json_data.encode("utf-8"), hashlib.md5).hexdigest()

if __name__ == "__main__":

    server = O3api()
    # access_key = '4b25521b23f968aa40b9995f560e82ac'
    # secret_key = '5817c61ef5339c3265665b718b1c8244'

    # tick = uuid.uuid1()
    # ticket = str(tick).upper()

    param = {
        'access_key': '4a67981f6e3cadf16ca161202eb7a57b',
        "cmd": "aoao.o2o.order.find",
        "ticket" : "0F1F9139-1375-43BE-99C9-578D3490CE51",
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
    # sign =  "209C86CFB626212E13E56C046C254028"
    spec = {

        "access_key": "dbda63a2c423d96f88c5a8fc5c22eac3",
        # 'access_key' : '4b25521b23f968aa40b9995f560e82ac',
        "cmd": "aoao.o2o.order.find",
        "ticket": "43480f98-8a0c-42b4-abd1-f1c826a89cc5",
        "time": 1506412148,
        "body": {
            "org_id": "59c220e99982692fcb7bf532"
        },
        "version": "v3.0"
    }

    #验证md5 算法 有没有问题：用 "123456" 来验证
    # datestr = "123456"
    # mymd5 = server.get_md5_value(datestr)
    # print "79======sign:", mymd5

    #判断，排序，数据转换 算法 是否正确：用spec数据来验证
    date_json = server.get_json_value(param)
    print "88========ksort->json_data:",date_json

    sign = server.make_sign(param)
    param["sign"] = sign
    print "sign:", sign
    headers = {'content-type': 'application/json'}
    url = 'https://aoao-open-dev.o3cloud.cn/v3'
    r = requests.post(url,data=json.dumps(param), headers=headers)
    print r.json()
