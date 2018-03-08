# -*- coding:utf-8 -*-
import os, csv
import sys
import logging
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

from model import shipment
# from email_auto import Sendemail
import email_auto

class ShipmentAxd(object):

    server = None

    file_name = '/data/shipment_yjk.csv'

    # log_filename = "logging_axd.log"

    shipment_list = []

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
        self.get_shipments(**kwargs)
        self.set_csv()
        # email_auto.Sendemail().send_email('/data/shipment.csv', '安鲜达  骑士运单-收到请回复谢谢', ['xiaoguang.jing@cityio.cn'])

    def get_shipments(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.find_shipment_all(kwargs)

    def find_shipment_all(self, params):
        """

        :param params:
        :return:
        """
        shipments = self.server.find(**params)
        print shipments.has_more,shipments.result_count,"++++++"
        for shipment in shipments.data:
            courier_name = ""
            courier = shipment.get('courier', None)
            if courier:
                courier_name = courier.get('name')
            _data = [
                str(shipment.get('id')),
                str(shipment.get('org_order_id')),
                courier_name.encode('gbk'),
                self.shipment_state_dict[str(shipment.get('state'))].encode('gbk'),
                str(shipment.get('shipping_date')),
            ]
            # print ".......", shipment.get('org_order_id')
            self.shipment_list.append(_data)
        params['page'] += 1
        if shipments.has_more is True:
            return self.find_shipment_all(params)

    def set_csv(self):
        """

        :return:
        """
        # try:
        csv_file = file(self.file_name, 'wb')
        # except IOError:
        #     os.system('mkdir /data/shipment.csv')
        #     csv_file = file(self.file_name,'wb')
        writer = csv.writer(csv_file)
        _list = ['运单号'.encode('gbk'), '商家订单号'.encode('gbk'), '骑士名称'.encode('gbk'), '状态'.encode('gbk'), '要求送达日期'.encode('gbk')]
        writer.writerow(_list)
        print self.shipment_list, "92==="
        writer.writerows(self.shipment_list)
        csv_file.close()
        print '==== set_shop_csv ====: 统计csv生成成功！'

    def get_yesterday(self):
        """

        :return:
        """
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=-1)
        yes_time_nyr = yes_time.strftime("%Y%m%d")
        return int(yes_time_nyr)

if __name__ == '__main__':

    server = ShipmentAxd()
    params = {
        # 'seller_id': '59506623998269645c3a899c',
        'vendor_id': "58e768363d65ce6662c084d9",
        'seller_id': "5a2f7c0d3d65ce5ede8a0b7c",#youjike
        'start_date': 20180101,
        'end_date': 20180131,
        'page': 1,
        'limit': 20,
    }
    server.run(**params)
    # Sendemail().send_email('/data/aa.csv', '安鲜达  骑士运单-收到请回复谢谢', ['zhouyan@cityio.cn','tianyi.li@meishisong.cn','xiaoguang.jing@cityio.cn'])
    # logging.basicConfig(filename=server.log_filename,filemode='w',level=logging.DEBUG)
    # logging.info(20171120)
    # Sendemail().send_email('/data/shipment.csv', '安鲜达  骑士运单-收到请回复谢谢', ['xiaoguang.jing@cityio.cn'])
