# -*- coding:utf-8 -*-
import os
import sys
import time
import datetime
import hashlib
import json,urllib2
import requests
import hmac, uuid
from collections import OrderedDict
import csv
reload(sys)
sys.setdefaultencoding('utf8')

file_name = '/data/flowerplus_18.csv'
# url = 'https://aoao-open-dev.o3cloud.cn/v3'
url = 'https://aoao-open.o3cloud.cn/v3'
headers = {'content-type': 'application/json'}

class o3_api(object):

    # secret_key = '1bae8ba701fc65ab9f5372c889b67ed5'
    # access_key = "f85b790068b49e13aa64f58580c24a96"
    secret_key = 'de1514119aaa5f7b2eca971348ca242b'# 花+商家的 私钥

    # access_key= "e5622585a2f0a258e6afb6aa47a60d91"
    # secret_key = "9f91e3bdb86cf95bb05cc4e938f5191f"

    version = "v3.0"
    data = {}

    def get_ticket(self):
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

    def get_csv_create_order(self):
        """

        :return:
        """
        csv_file = file(file_name, 'r')
        csv_reader = csv.reader(csv_file)
        # _list = ['订单编号'.encode('gbk'), '商家订单编号'.encode('gbk'), '创建时间'.encode('gbk'), '店铺名称'.encode('gbk'), '配送商圈'.encode('gbk'),'收货人姓名'.encode('gbk'),'收货人联系电话'.encode('gbk'),'收货人地址'.encode('gbk'),'要求送达时间'.encode('gbk'),'服务产品'.encode('gbk'),'订单状态'.encode('gbk')]
        # writer.writerow(_list)
        # writer.writerows(data_res_ll)
        timestamp = int(time.time())
        data = {
            'access_key': self.access_key,
            'cmd': 'aoao.o2o.order.create',
            'version': self.version,
            "ticket": self.get_ticket(),
            "time": timestamp
        }

        for row in csv_reader:

            _date = row[8].encode('utf-8').split("  ")
            shipping_date = int(_date[0].replace('-',''))
            shipping_time = _date[1]
            body = {
                # "org_id": "593f7307998269638c5ee311",#测试
                "org_id": "5a1fbe1f3d65ce56e202de08",#生产
                "contract_id":'5a1fd4c63d65ce56e2051c28',#正式
                # "contract_id" : "593f742c998269638c5ee952",
                "city_code": "110000",
                "goods": [{
                    "name": "花+的鲜花",
                    "specs": "1000.00(元)/盒",
                    "quantity": 1,
                }],
                "seller":{
                    "name":"花+",
                    "seller_type": 2
                },
                "shop": {
                    "name": "花+"
                },
                # "service": {"name": "落地配业务产品"},
                "pay_type": 3,
                "consignor": {
                    "name": "FlowerPlus",
                    "phone": "17710590213",
                    "address": "酒仙桥四街坊甲12号楼白色门",
                },
                "barcode": row[1].encode("utf-8"),
                "org_order_id": row[1].encode("utf-8"),
                "shipping_date": shipping_date,
                # "shipping_date": 20171201,
                "shipping_time": shipping_time,
                "consignee": {
                    "name": row[5],#.decode('gbk').encode('utf-8'),
                    "phone": str(row[6]).decode('gbk').encode('utf-8'),
                    "address": row[7]#.decode('gbk').encode('utf-8')
                }
            }
            data['body'] = body
            data['sign'] = self.make_sign(data)
            r = requests.post(url,data=json.dumps(data), headers=headers)
            data.pop('sign') #如果不清空，下次计算签名会带着 "sign":""，导致签名错误
            print r.json()
            time.sleep(1)

            # exit()
        csv_file.close()
        print '==== set_shop_csv ====: 统计csv生成成功！'

if __name__ == "__main__":

    server = o3_api()
    # access_key = '4b25521b23f968aa40b9995f560e82ac'
    # secret_key = '5817c61ef5339c3265665b718b1c8244'
#优集客
    # access_key = '4a67981f6e3cadf16ca161202eb7a57b'
    # secret_key = '9f91e3bdb86cf95bb05cc4e938f5191f'
    # tick = uuid.uuid1()
    # ticket = str(tick).upper()
    access_key = 'e5622585a2f0a258e6afb6aa47a60d91'

    param = {
        "access_key": "f85b790068b49e13aa64f58580c24a96",
        "cmd": "aoao.o2o.order.find",
        "ticket": "0F1F9139-1375-43BE-99C9-578D3490CE51",
        "time": 1506396365,
        "body": {
            "org_id": "599662ec99826949b79e5097",
            "start_date": 20160101,
            "end_date": 20160108,
            "page": 1,
            "limit": 10,
            "detail_mode": 2
        },
        "version": "v3.0",
    }

    spec = {
        "access_key": "e5622585a2f0a258e6afb6aa47a60d91",
        "cmd": "aoao.o2o.order.find",
        "ticket": "4D089600-3E30-4C85-B4A6-CC87E1F55953",
        "time": 1516797628,
        "body": {
            "org_id": "5a1fbe1f3d65ce56e202de08",
            'org_order_ids': ['F17119998233','F17119846239','F1711934123']
        },
        "version": "v3.0"
    }

    data_ = {
      "access_key": "4a67981f6e3cadf16ca161202eb7a57b",
      "cmd": "aoao.o2o.order.create",
      "ticket": "4D089600-3E30-4C85-B4A6-CC87E1F55953",
      "version": "v3.0",
      "time": 1516797628,
      "sign": "5309f8daf3e340441e432a959dfea362",
      "body": {
        "org_id": "593f7307998269638c5ee311",
        "org_order_id": "8362030364053504",
        "contract_id": "593f742c998269638c5ee952",
        "barcode": "8362030364053504",
        "pay_type": 3,
        "consignor": {
          "name": "eat测试联调门店2",
          "phone": "010-89890298",
          "address": "北京市北京市北京欢乐谷店",
          "bd_poi": [
            "116.501432",
            "39.873859"
          ]
        },
        "consignee": {
          "name": "任慧慧",
          "phone": "134****0714",
          "address": "北京市北京市朝阳区北京欢乐谷123",
          "bd_poi": [
            "116.501434",
            "39.873859"
          ]
        },
        "city_code": "110000"
      }
}
    youjike = {
        "access_key": "4a67981f6e3cadf16ca161202eb7a57b",
        "cmd": "aoao.o2o.order.create",
        "ticket": "12918715-1683-4012-8A1D-1A7C4D645B50",
        "version": "v3.0",
        "time": 1512960133,
        # "sign": "efabdcac8390308000ca6c02e4d78182",
        "body": {
            "org_id": "593f7307998269638c5ee311",
            "org_order_id": "1232026449840128",
            "contract_id": "593f742c998269638c5ee952",
            "barcode": "1232026449840128",
            "pay_type": 3,
            "consignor": {
                "name": "ueater总部",
                "phone": "18912341614",
                "address": "北京市北京市来广营融创动力园",
                "bd_poi": [
                    116.472447,
                    40.023863
                ]
        },
        "consignee": {
        "name": "大兄弟",
        "phone": "13313211423",
        "address": "北京市北京市朝阳区融创动力文化创意产业园B座205",
        "bd_poi": [
            116.472210,
            40.023687
        ]
        },
        "city_code": "110000"
    }
    }

    flower = {
        "access_key": "e5622585a2f0a258e6afb6aa47a60d91",
        "cmd": "aoao.o2o.order.create",
        "version": "v3.0",
        "ticket": "0FB6C279-AB55-D648-52A8-130CD2141C9A",
        "body": {
            "org_id": "5a1fbe1f3d65ce56e202de08",
            "org_order_id": "F17102440346",
            "contract_id": "5a1fd4c63d65ce56e2051c28",
            "shipping_date": "20180127",
            "shipping_time_last": "12:00",
            "goods": [{
                "name": "花＋的鲜花",
                "specs": "盒",
                "quantity": "1",
                "price": "100000"
            }],
            "barcode": "F17102440346",
            "pay_type": 3,
            "consignee": {
                "name": "张曙辉_测试",
                "phone": "15692102486",
                "address": "北京北京市昌平区水关新村16号楼1单元103号",
                "bd_poi": ["116.250047", "40.214881"]
            },
            "consignor": {
                "name": "美SS-昌平东站",
                "phone": "18301696181",
                "address": "北京北京市昌平区昌平南环路草场胡同35-107",
                "bd_poi": ["116.237922", "40.219325"]
            },
            "city_code": "110000",
            "extra_metas": {
                "area_id": "59dc3f4a3d65ce4bf18637de"
            }
        },
            "time": 1516850230,
            # "sign": "9e0739b3baeea863af94966326b3add6"
    }

    test_data = {
          "access_key": "4a67981f6e3cadf16ca161202eb7a57b",
          "cmd": "aoao.o2o.order.create",
          "ticket": "4D089600-3E30-4C85-B4A6-CC87E1F55953",
          "version": "v3.0",
          "time": 1516797628,
          # "sign": "5309f8daf3e340441e432a959dfea362",
          "body": {
            "org_id": "593f7307998269638c5ee311",
            "org_order_id": "8362030364053505",
            "contract_id": "593f742c998269638c5ee952",
            "barcode": "8362030364053505",
            "pay_type": 3,
            "consignor": {
              "name": "eat测试联调门店2",
              "phone": "010-89890298",
              "address": "北京市北京市北京欢乐谷店",
              "bd_poi": [
                "116.501432",
                "39.873859"
              ]
            },
            "consignee": {
              "name": "任慧慧",
              "phone": "134****0714",
              "address": "北京市北京市朝阳区北京欢乐谷123",
              "bd_poi": [
                "116.501434",
                "39.873859"
              ]
            },
            "city_code": "110000"
          }
    }
    #验证md5 算法 有没有问题：用 "123456" 来验证
    # datestr = "123456"
    # mymd5 = server.get_md5_value(json.dumps(youjike))
    # print "79======sign:", mymd5

    #判断，排序，数据转换 算法 是否正确：用spec数据来验证
    date_json = server.get_json_value(spec)
    print "88========ksort->json_data:", date_json

    sign = server.make_sign(spec)
    spec["sign"] = sign
    print "sign:", sign
    headers = {'content-type': 'application/json'}
    # url = 'https://aoao-open-dev.o3cloud.cn/v3'
    url = 'https://aoao-open.o3cloud.cn/v3'
    r = requests.post(url, data=json.dumps(spec), headers=headers)
    print r.json()
    # server.get_csv_create_order()
