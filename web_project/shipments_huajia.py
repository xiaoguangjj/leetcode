# -*- coding:utf-8 -*-
import os, csv
import sys
import utc_time
import pymongo
import time
from bson import ObjectId
import email_auto

reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

from model import shipment
# from email_auto import Sendemail

biz_mode = {
    '10': '本地生活圈',
    '20': '落地配（无存储',
    '25': '落地配（有存储）',
    '30': '快递',
}

class ShipmentAxd(object):

    server = None

    file_name = '/data/shipment_huajia.csv'

    host = "127.0.0.1"
    port = 27017

    shipment_list = []

    shipment_mongo = {}

    shipment_state_dict = {
        '0': '已创建',
        '5': '已创建',
        '10': '已确认',
        '15': '已分配',
        '16': '待接单',
        '20': '已接单',
        '22': '已到店',
        '24': '已取货',
        '-50': '异常',
        '100': '已完成',
        '-100': '已关闭',
    }

    def run(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.server = shipment.Shipment()
        self.shipment_list = []
        # self.get_shipments(**kwargs)
        self.read_mongdb()
        self.set_csv()
        # email_auto.Sendemail().send_email('/data/shipment.csv', '安鲜达  骑士运单-收到请回复谢谢', ['xiaoguang.jing@cityio.cn'])

    def get_shipments(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.find_shipment_all(kwargs)

    def write_mongodb(self,params):
        """

        :return:
        """

        conn = pymongo.MongoClient(host=self.host,port=self.port)
        db = conn.aoao
        # db.shipment.insert({"name" : "张三"})
        # result = db.shipment.find({"_id": ObjectId('59f704c6421aa96301e7e9bd')})
        # for i in result:
        #     print i,'79'
        # account = db.get_collection(col_shipment)
        # print params[1],params[2],params[23],"83"
        #account.insert({"商家订单号":params["org_order_id"],"运单号":params["id"],"条形编码":params["barcode"],"商家名称":params["seller_name"],"商家联系人":params["consignor_name"],"业务模式":params["biz_mode"],"发货地址":params["consignor_address"],"骑士":params["courier_name"],"骑士手机":params["courier_mobile"],"所属区域":params["area_name"],"配送距离":params["distance"],"运单状态":params["shipment_state"],"订单金额":params["o3_order_amount"],"代付商家":params["payment"],"代收顾客":params["code"],"订单备注":params["delivery_note"],"送达时间":params["done_at"],"取消时间":params["closed_at"],"创建时间":params["created_at"],"期望送达":params["shipping_time"],"接单时间":params["accepted_at"],"到店时间":params["arrived_at"],"取货时间":params["pickup_at"],"异常原因":params["error_note"],"关闭原因":params["closed_note"]})
        # db.shipment.insert({"商家订单号":params[1],"运单号":params[2],"条形编码":params[3],"商家名称":params[4],"商家联系人":params[5],"业务模式":params[6],"发货地址":params[7],"骑士":params[8],"骑士手机":params[9],"所属区域":params[10],"配送距离":params[11],"运单状态":params[12],"订单金额":params[13],"代付商家":params[14],"代收顾客":params[15],"订单备注":params[16],"送达时间":params[17],"取消时间":params[18],"创建时间":params[19],"期望送达":params[20],"接单时间":params[21],"到店时间":params[22],"取货时间":params[23],"异常原因":params[24],"关闭原因":params[25]})
        # db.shipment.insert({"org_order_id":params[0],"id":params[1],"barcode":params[2],"seller_name":params[3],"consignor_name":params[4],"biz_mode":params[5],"consignor_address":params[6],"courier_name":params[7],"courier_mobile":params[8],"area_name":params[9],"distance":params[10],"shipment_state":params[11],"o3_order_amount":params[12],"payment":params[13],"cod":params[14],"delivery_note":params[15],"done_at":params[16],"closed_at":params[17],"created_at":params[18],"shipping_time":params[19],"accepted_at":params[20],"arrived_at":params[21],"pickup_at":params[22],"error_note":params[23],"closed_note":params[24]})
        db.shipment.insert({"org_order_id":params[0],"id":params[1],"barcode":params[2],"seller_name":params[3],"consignor_name":params[4],"biz_mode":params[5],"consignor_address":params[6],"courier_name":params[7],"courier_mobile":params[8],"area_name":params[9],"distance":params[10],"shipment_state":params[11],"o3_order_amount":params[12],"payment":params[13],"cod":params[14],"delivery_note":params[15],"done_at":params[16],"closed_at":params[17],"created_at":params[18],"shipping_time":params[19],"accepted_at":params[20],"arrived_at":params[21],"pickup_at":params[22],"error_note":params[23],"closed_note":params[24]})

    def read_mongdb(self):
        """

        :return:
        """
        conn = pymongo.MongoClient(host=self.host,port=self.port)
        db = conn.aoao
        # print params[1],params[2],params[23],"83"
        for shipment in db.shipment.find():
            # print shipment.get('shipment_state'),"99"
            data = [
                str(shipment.get('org_order_id').encode('gbk')),
                str(shipment.get('id').encode('gbk')),
                str(shipment.get('barcode').encode('gbk')),
                str(shipment.get('seller_name').encode('gbk')),
                str(shipment.get('consignor_name').encode('gbk')),
                str(shipment.get('biz_mode').encode('gbk')),
                str(shipment.get('consignor_address').encode('gbk')),
                str(shipment.get('courier_name').encode('gbk')),
                str(shipment.get('courier_mobile').encode('gbk')),
                str(shipment.get('area_name').encode('gbk')),
                str(shipment.get('distance').encode('gbk')),
                str(shipment.get('shipment_state').encode('gbk')), #运单状态
                str(shipment.get('o3_order_amount').encode('gbk')),  #订单金额
                str(shipment.get('payment').encode('gbk')),
                str(shipment.get('cod').encode('gbk')),
                str(shipment.get('delivery_note').encode('gbk')),
                str(shipment.get('done_at').encode('gbk')),
                str(shipment.get('closed_at').encode('gbk')),
                str(shipment.get('created_at').encode('gbk')),
                str(shipment.get('shipping_time').encode('gbk')), #期望送达
                str(shipment.get('accepted_at').encode('gbk')),
                str(shipment.get('arrived_at').encode('gbk')),
                str(shipment.get('pickup_at').encode('gbk')),
                str(shipment.get('error_note').encode('gbk')),
                str(shipment.get('closed_note').encode('gbk')),
            ]
            self.shipment_list.append(data)
        #account.insert({"商家订单号":params["org_order_id"],"运单号":params["id"],"条形编码":params["barcode"],"商家名称":params["seller_name"],"商家联系人":params["consignor_name"],"业务模式":params["biz_mode"],"发货地址":params["consignor_address"],"骑士":params["courier_name"],"骑士手机":params["courier_mobile"],"所属区域":params["area_name"],"配送距离":params["distance"],"运单状态":params["shipment_state"],"订单金额":params["o3_order_amount"],"代付商家":params["payment"],"代收顾客":params["code"],"订单备注":params["delivery_note"],"送达时间":params["done_at"],"取消时间":params["closed_at"],"创建时间":params["created_at"],"期望送达":params["shipping_time"],"接单时间":params["accepted_at"],"到店时间":params["arrived_at"],"取货时间":params["pickup_at"],"异常原因":params["error_note"],"关闭原因":params["closed_note"]})
        # db.shipment.insert({"商家订单号":params[1],"运单号":params[2],"条形编码":params[3],"商家名称":params[4],"商家联系人":params[5],"业务模式":params[6],"发货地址":params[7],"骑士":params[8],"骑士手机":params[9],"所属区域":params[10],"配送距离":params[11],"运单状态":params[12],"订单金额":params[13],"代付商家":params[14],"代收顾客":params[15],"订单备注":params[16],"送达时间":params[17],"取消时间":params[18],"创建时间":params[19],"期望送达":params[20],"接单时间":params[21],"到店时间":params[22],"取货时间":params[23],"异常原因":params[24],"关闭原因":params[25]})
        # db.shipment.insert({"org_order_id":params[0],"id":params[1],"barcode":params[2],"seller_name":params[3],"consignor_name":params[4],"biz_mode":params[5],"consignor_address":params[6],"courier_name":params[7],"courier_mobile":params[8],"area_name":params[9],"distance":params[10],"shipment_state":params[11],"o3_order_amount":params[12],"payment":params[13],"code":params[14],"delivery_note":params[15],"done_at":params[16],"closed_at":params[17],"created_at":params[18],"shipping_time":params[19],"accepted_at":params[20],"arrived_at":params[21],"pickup_at":params[22],"error_note":params[23],"closed_note":params[24]})
        # self.set_csv()

    def find_shipment_all(self, params):
        """

        :param params:
        :return:
        """
        shipments = self.server.find(**params)
        print shipments.result_count, "142"
        for shipment in shipments.data:
            courier_name = ""
            courier_mobile = ""
            shipping_time = ""
            done_at = ""
            closed_at = ""
            created_at = ""
            accepted_at = ""
            arrived_at = ""
            pickup_at = ""

            courier = shipment.get('courier', None)
            if courier:
                courier_name = courier.get('name')
                courier_mobile = courier.get('mobile')

            if shipment.get('shipping_time'):
                _shipping_time_ = str(shipment.get('shipping_time')),
                _shipping_time = "".join(list(_shipping_time_))
                shipping_time = utc_time.format_data_str(str(_shipping_time))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]

            if shipment.get('shipping_time'):
                _shipping_time_ = str(shipment.get('shipping_time')),
                _shipping_time = "".join(list(_shipping_time_))
                shipping_time = utc_time.format_data_str(str(_shipping_time))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shipment.get('done_at'):
                _done_at_ = str(shipment.get('done_at')),
                _done_at = "".join(list(_done_at_))
                done_at = utc_time.format_data_str(str(_done_at))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shipment.get('closed_at'):
                _closed_at_ = str(shipment.get('closed_at')),
                _closed_at = "".join(list(_closed_at_))
                closed_at = utc_time.format_data_str(str(_closed_at))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shipment.get('created_at'):
                _created_at_ = str(shipment.get('created_at')),
                _created_at = "".join(list(_created_at_))
                created_at = utc_time.format_data_str(str(_created_at))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shipment.get('accepted_at'):
                _accepted_at_ = str(shipment.get('accepted_at')),
                _accepted_at = "".join(list(_accepted_at_))
                accepted_at = utc_time.format_data_str(str(_accepted_at))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shipment.get('arrived_at'):
                _arrived_at_ = str(shipment.get('arrived_at')),
                _arrived_at = "".join(list(_arrived_at_))
                arrived_at = utc_time.format_data_str(str(_arrived_at))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shipment.get('pickup_at'):
                _pickup_at_ = str(shipment.get('pickup_at')),
                _pickup_at = "".join(list(_pickup_at_))
                pickup_at = utc_time.format_data_str(str(_pickup_at))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            _data = [
                str(shipment.get('org_order_id')),
                str(shipment.get('id')),
                str(shipment.get('barcode')),
                str(shipment.get('seller').get('name').encode('gbk')),
                str(shipment.get('consignor_name').encode('gbk')),
                biz_mode[str(shipment.get('biz_mode',None))].encode('gbk'),
                str(shipment.get('consignor_address').encode('gbk')),
                courier_name.encode('gbk'),
                str(courier_mobile),
                str(shipment.get('area').get('name').encode('gbk')),
                shipment.get('distance')/1000.0,
                self.shipment_state_dict[str(shipment.get('state'))].encode('gbk'), #运单状态
                shipment.get('o3_order_amount')/100.0,  #订单金额
                shipment.get('extra_services').get('payment').get('amount')/100.0,
                shipment.get('extra_services').get('cod').get('amount')/100.0,
                shipment.get('delivery_note').encode('gbk'),
                done_at,
                closed_at,
                created_at,
                shipping_time, #期望送达
                accepted_at,
                arrived_at,
                pickup_at,
                # str(shipment.get('consignee_name').encode('gbk')),
                # str(shipment.get('consignee_address').encode('gbk')),
                # str(shipment.get('consignor_name').encode('gbk')),
                # str(shipment.get('extra_services',None).get('cod',None).get('amount',None)),
                # str(shipment.get('extra_services',None).get('payment',None).get('amount',None)),
                str(shipment.get('error_note').encode('gbk')),
                str(shipment.get('closed_note').encode('gbk')),
            ]
            param = (
                str(shipment.get('org_order_id')).encode('utf-8'),
                str(shipment.get('id')).encode("utf-8"),
                str(shipment.get('barcode')).encode("utf-8"),
                str(shipment.get('seller').get('name')).encode('utf-8'),
                str(shipment.get('consignor_name')).encode('utf-8'),
                str(biz_mode[str(shipment.get('biz_mode',None))]).encode('utf-8'),
                str(shipment.get('consignor_address')).encode('utf-8'),
                str(courier_name).encode('utf-8'),
                str(courier_mobile).encode('utf-8'),
                str(shipment.get('area').get('name')).encode('utf-8'),
                str(shipment.get('distance')/1000.0).encode('utf-8'),
                str(self.shipment_state_dict[str(shipment.get('state'))]).encode('utf-8'), #运单状态
                str(shipment.get('o3_order_amount')/100.0).encode('utf-8'),  #订单金额
                str(shipment.get('extra_services').get('payment').get('amount')/100.0).encode('utf-8'),
                str(shipment.get('extra_services').get('cod').get('amount')/100.0).encode('utf-8'),
                str(shipment.get('delivery_note')).encode('utf-8'),
                str(done_at).encode('utf-8'),
                str(closed_at).encode('utf-8'),
                str(created_at).encode('utf-8'),
                str(shipping_time).encode('utf-8'), #期望送达
                str(accepted_at).encode('utf-8'),
                str(arrived_at).encode('utf-8'),
                str(pickup_at).encode('utf-8'),
                str(shipment.get('error_note')).encode('utf-8'),
                str(shipment.get('closed_note')).encode('utf-8'),

            )
            # print ".......", shipment.get('org_order_id')
            self.shipment_list.append(_data)
            self.write_mongodb(param)
            time.sleep(0.5)
        params['page'] += 1
        print 'page:', params['page']
        if shipments.has_more is True:
            return self.find_shipment_all(params)

    def set_csv(self):
        """

        :return:
        """
        csv_file = file(self.file_name, 'wb')
        writer = csv.writer(csv_file)#'运单号'.encode('gbk'),

        _list = ['商家订单号'.encode('gbk'), '运单号'.encode('gbk'),'条形编码'.encode('gbk'), '商家名称'.encode('gbk'),
                  '商家联系人'.encode('gbk'), '业务模式'.encode('gbk'), '发货地址'.encode('gbk'), '骑士'.encode('gbk'),
                  '骑士手机'.encode('gbk'), '所属区域'.encode('gbk'), '配送距离（km）'.encode('gbk'),
                  '运单状态'.encode('gbk'), '订单金额（元）'.encode('gbk'), '代付商家（元）'.encode('gbk'),
                  '代收顾客'.encode('gbk'), '订单备注'.encode('gbk'), '送达时间'.encode('gbk'), '取消时间'.encode('gbk'),
                  '创建时间'.encode('gbk'), '期望送达'.encode('gbk'), '接单时间'.encode('gbk'), '到店时间'.encode('gbk'),
                  '取货时间'.encode('gbk'), '异常原因'.encode('gbk'), '关闭原因'.encode('gbk')]

        writer.writerow(_list)
        # print self.shipment_list,"92==="
        writer.writerows(self.shipment_list)
        csv_file.close()
        print '==== set_shop_csv ====: 统计csv生成成功！'


if __name__ == '__main__':

    server = ShipmentAxd()
    params = {
        # 'seller_id': '59506623998269645c3a899c',
        'vendor_id': "599ff2c53d65ce6bab5754cb",
        'seller_id': "5a1fbe1f3d65ce56e202de08",
        # 'start_date': 20180123,
        # 'end_date': 20180123,
        'start_date': 20180228,
        'end_date': 20180228,
        'page': 1,
        'limit': 100,
    }

    server.run(**params)
    # server.mongodb()
    # Sendemail().send_email('/data/aa.csv', '安鲜达  骑士运单-收到请回复谢谢', ['zhouyan@cityio.cn','tianyi.li@meishisong.cn','xiaoguang.jing@cityio.cn'])
