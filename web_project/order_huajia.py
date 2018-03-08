# -*- coding:utf-8 -*-
import os, csv
import sys
import datetime
import time
import utc_time

reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

from model import order
from email_auto import Sendemail

class OrderAxd(object):

    server = None

    file_name = '/data/order_huajia.csv'

    order_list = []

    order_state_dict = {
        '0': '已创建',
        '1': '待发布',
        '20': '已发布',
        '25': '待接单',
        '50': '配送中',
        '100': '已完成',
        '-100': '已关闭',
        '-50': '异常',
    }

    order_biz_mode = {
        '10': '周边送',
        '20': '落地配',
        '30': '同城送',
    }

    order_pay_type = {
        '1': '现金',
        '2': '余额',
        '3': '后付费',
    }
    order_item_type = {
        '1': '美食餐饮',
        '2': '生鲜蔬菜',
        '3': '超市商品',
        '4': '鲜花蛋糕',
        '5': '其他',
    }

    def run(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.server = order.Order()
        self.order_list = []
        self.get_orders(**kwargs)
        self.set_csv()
        # txt = '{0} 商家订单-收到请回复谢谢'.format(self.getYesterday())
        # Sendemail().send_email(self.file_name, txt, ['xiaoguang.jing@cityio.cn'])
        # self.getYesterday()

    def get_orders(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.find_order_all(kwargs)
        # self.get_order_all(kwargs)

    def get_order_all(self,params):
        """

        :param params:
        :return:
        """
        orders = self.server.find(**params)
        # print "65==", orders.__dict__
        # shop = orders.get('shop')
        for order in orders.data:
            consignor_name = ""
            consignor_mobile = ""
            shop_name = ""
            consignor_address = ""
            vendor_name = ""
            done_at = ""
            closed_at = ""
            created_at = ""
            shipping_time = ""
            shop = order.get('shop', None)
            consignor = order.get('consignor', None)
            consignee_name = ""
            consignee_address = ""
            consignee_mobile = ""
            # tms_biz_info = order.get('tms_biz_info', None)[0]
            # tms = tms_biz_info.get('tms',None)
            # vendor_name = tms.get('vendor_name',None)
            consignee = order.get('consignee',None)
            for key,v in order.iteritems():
                if key == 'tms_biz_info':
                    vendor_name = v[0].get('tms').get('vendor_name')

            if order.get('done_at'):
                _done_at_ = str(order.get('done_at')),
                _done_at = "".join(list(_done_at_))
                done_at = utc_time.format_data_str(str(_done_at))
                # done_at = _done_at[0:10]+" "+_done_at[11:19]
            if order.get('closed_at'):
                _closed_at_ = str(order.get('closed_at')),
                _closed_at = "".join(list(_closed_at_))
                closed_at = utc_time.format_data_str(str(_closed_at))
                # closed_at = _closed_at[0:10]+" "+_closed_at[11:19]
            if order.get('created_at'):
                _created_at_ = str(order.get('created_at')),
                _created_at = "".join(list(_created_at_))
                created_at = utc_time.format_data_str(str(_created_at))
                # created_at = _created_at[0:10]+" "+_created_at[11:19]
            if order.get('shipping_time'):
                _shipping_time_ = str(order.get('shipping_time')),
                _shipping_time = "".join(list(_shipping_time_))
                shipping_time = utc_time.format_data_str(str(_shipping_time))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shop:
                shop_name = shop.get('name')
            if consignor:
                consignor_name = consignor.get('name')
                consignor_mobile = consignor.get('mobile')
                consignor_address = consignor.get('address')
            if consignee:
                consignee_name = consignee.get('name')
                consignee_address = consignee.get('address')
                consignee_mobile = consignee.get('mobile')
            _data = [
                str(order.get('id')),
                str(order.get('org_order_id')),
                str(order.get('barcode')),
                self.order_state_dict[str(order.get('state'))].encode('gbk'),
                shop_name.encode('gbk'),
                consignor_address.encode('gbk'),
                vendor_name.encode('gbk'),
                self.order_biz_mode[str(order.get('biz_mode'))].encode('gbk'),
                order.get('distance')/1000.0,
                str(order.get('shipping_fee')/100.0),
                str(order.get('tip_fee')/100.0),
                self.order_pay_type[str(order.get('pay_type'))].encode('gbk'),
                str(consignee_name.encode('gbk')),
                str(consignee_address.encode('gbk')),
                str(consignee_mobile),
                self.order_item_type[str(order.get('item_type'))].encode('gbk'),
                order.get('order_amount')/100.0,
                order.get('extra_services',None).get('payment',None).get('amount', None)/100.0,
                order.get('extra_services',None).get('cod',None).get('amount', None)/100.0,
                str(order.get('note')),
                done_at,
                closed_at,
                created_at,
                shipping_time,
                str(order.get('error_note').encode('gbk')),
                str(order.get('closed_note').encode('gbk')),
            ]
            print "79====", order.get('org_order_id')
            self.order_list.append(_data)
        params['page'] += 1
        if orders.has_more is True:
            return self.find_order_all(params)

    def find_order_all(self, params):
        """

        :param params:
        :return:
        """
        orders = self.server.find(**params)
        # print "65==", orders.__dict__
        # shop = orders.get('shop')
        for order in orders.data:
            consignor_name = ""
            consignor_mobile = ""
            shop_name = ""
            consignor_address = ""
            vendor_name = ""
            done_at = ""
            closed_at = ""
            created_at = ""
            shipping_time = ""
            shop = order.get('shop', None)
            consignor = order.get('consignor', None)
            consignee_name = ""
            consignee_address = ""
            consignee_mobile = ""
            # tms_biz_info = order.get('tms_biz_info', None)[0]
            # tms = tms_biz_info.get('tms',None)
            # vendor_name = tms.get('vendor_name',None)
            consignee = order.get('consignee',None)
            for key,v in order.iteritems():
                if key == 'tms_biz_info':
                    vendor_name = v[0].get('tms').get('vendor_name')

            if order.get('done_at'):
                _done_at_ = str(order.get('done_at')),
                _done_at = "".join(list(_done_at_))
                done_at = utc_time.format_data_str(str(_done_at))
                # done_at = _done_at[0:10]+" "+_done_at[11:19]
            if order.get('closed_at'):
                _closed_at_ = str(order.get('closed_at')),
                _closed_at = "".join(list(_closed_at_))
                closed_at = utc_time.format_data_str(str(_closed_at))
                # closed_at = _closed_at[0:10]+" "+_closed_at[11:19]
            if order.get('created_at'):
                _created_at_ = str(order.get('created_at')),
                _created_at = "".join(list(_created_at_))
                created_at = utc_time.format_data_str(str(_created_at))
                # created_at = _created_at[0:10]+" "+_created_at[11:19]
            if order.get('shipping_time'):
                _shipping_time_ = str(order.get('shipping_time')),
                _shipping_time = "".join(list(_shipping_time_))
                shipping_time = utc_time.format_data_str(str(_shipping_time))
                # shipping_time = _shipping_time[0:10]+" "+_shipping_time[11:19]
            if shop:
                shop_name = shop.get('name')
            if consignor:
                consignor_name = consignor.get('name')
                consignor_mobile = consignor.get('mobile')
                consignor_address = consignor.get('address')
            if consignee:
                consignee_name = consignee.get('name')
                consignee_address = consignee.get('address')
                consignee_mobile = consignee.get('mobile')
            _data = [
                str(order.get('id')),
                str(order.get('org_order_id')),
                str(order.get('barcode')),
                self.order_state_dict[str(order.get('state'))].encode('gbk'),
                shop_name.encode('gbk'),
                consignor_address.encode('gbk'),
                vendor_name.encode('gbk'),
                self.order_biz_mode[str(order.get('biz_mode'))].encode('gbk'),
                order.get('distance')/1000.0,
                str(order.get('shipping_fee')/100.0),
                str(order.get('tip_fee')/100.0),
                self.order_pay_type[str(order.get('pay_type'))].encode('gbk'),
                str(consignee_name.encode('gbk')),
                str(consignee_address.encode('gbk')),
                str(consignee_mobile),
                self.order_item_type[str(order.get('item_type'))].encode('gbk'),
                order.get('order_amount')/100.0,
                order.get('extra_services',None).get('payment',None).get('amount', None)/100.0,
                order.get('extra_services',None).get('cod',None).get('amount', None)/100.0,
                str(order.get('note')),
                done_at,
                closed_at,
                created_at,
                shipping_time,
                str(order.get('error_note').encode('gbk')),
                str(order.get('closed_note').encode('gbk')),
            ]
            print "79====", order.get('org_order_id')
            self.order_list.append(_data)
        params['page'] += 1
        if orders.has_more is True:
            return self.find_order_all(params)

    def utc2local(self,utc_st):
        """UTC时间转本地时间（+8:00"""
        now_stamp = time.time()
        local_time = datetime.datetime.fromtimestamp(now_stamp)
        utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
        offset = local_time - utc_time
        print offset, "177"
        local_st = utc_st + offset
        print local_st, "179"
        return local_st

    def set_csv(self):
        """

        :return:
        """
        csv_file = file(self.file_name, 'wb')
        writer = csv.writer(csv_file)
        _list = ['嗷嗷订单号'.encode('gbk'), '订单编号（商户订单编号）'.encode('gbk'),'条形编码'.encode('gbk'), '订单状态'.encode('gbk'),'店铺名称'.encode('gbk'),'发货地址'.encode('gbk'),'服务商名称'.encode('gbk'),'业务模式'.encode('gbk'),'配送距离(km)'.encode('gbk'), '配送费(元)'.encode('gbk'),'小费(元)'.encode('gbk'),'结算方式'.encode('gbk'),'顾客姓名'.encode('gbk'),'顾客地址'.encode('gbk'),'顾客电话'.encode('gbk'),'商品类型'.encode('gbk'),'订单金额(元)'.encode('gbk'),'代付商家'.encode('gbk'),'代收顾客'.encode('gbk'),'订单备注'.encode('gbk'),'送达时间'.encode('gbk'),'取消时间'.encode('gbk'),'下单时间'.encode('gbk'),'期望送达'.encode('gbk'),'异常原因'.encode('gbk'),'关闭原因'.encode('gbk')]
        writer.writerow(_list)
        print self.order_list
        writer.writerows(self.order_list)
        csv_file.close()
        print '==== set_shop_csv ====: 统计csv生成成功！'

    def getYesterday(self):
        """
        :return:
        """
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=-1)
        yes_time_nyr = yes_time.strftime('%Y%m%d')
        return yes_time_nyr

if __name__ == '__main__':

    axd_server = OrderAxd()
    spec = {
        # 'seller_id': '5a1fbe1f3d65ce56e202de08',
        # 'vendor_id': "5982aad63d65ce390135ba08",
        'seller_id': "5a1fbe1f3d65ce56e202de08",
        'start_date': 20180201,
        'end_date': 20180228,
        'page': 1,
        'limit': 10,
    }
    axd_server.run(**spec)
    # Sendemail().send_email('/data/aa.csv', '花+  骑士运单-收到请回复谢谢', ['zhouyan@cityio.cn','tianyi.li@meishisong.cn','xiaoguang.jing@cityio.cn'])

