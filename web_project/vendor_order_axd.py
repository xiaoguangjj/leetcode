# -*- coding:utf-8 -*-
import os, csv
import sys
import time
import utc_time

reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

from model import vendor_order
# from email_auto import Sendemail


class VendorAxd(object):

    server = None

    file_name = '/data/vendor_order.csv'

    vendor_list = []
    count = ["日期：20171011".encode('gbk'),"总订单数：204单".encode('gbk'),'']
    vendor_state_dict = {
        '0': '已创建',
        '5': '已创建',
        '10': '已确认',
        '15': '已分配',
        '16': '待接单',
        '20': '已接单',
        '22': '已到店',
        '25': '已确认',
        '24': '已取货',
        '-50': '异常',
        '100': '已完成',
        '-100': '已关闭',
    }
    biz_mode = {
        '10': '本地生活圈',
        '20': '落地配（无存储',
        '25': '落地配（有存储）',
        '30': '快递',
    }
    pay_type = {
        '1' : '现金',
        '2' : '余额',
        '3': '后付费',
    }
    seller_type = {
        '1':'美食餐饮',
        '2':'生鲜蔬菜',
        '3':'超市商品',
        '4':'鲜花蛋糕',
        '5':'其他',
    }

    def run(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.server = vendor_order.Vendor()
        self.vendor_list = []
        self.get_vendors(**kwargs)
        self.set_csv()
        # Sendemail().send_email('/data/aa.csv', '花+  骑士运单-收到请回复谢谢', ['xiaoguang.jing@cityio.cn'])

    def get_vendors(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.find_vendor_all(kwargs)

    def find_vendor_all(self, params):
        """

        :param params:
        :return:
        """
        vendors = self.server.find(**params)

        for vendor in vendors.data:
            area_info_name = ""
            seller_name = ""
            shop_name = ""
            delivery_stock_name = ""
            estimate_distance = ""
            consignor_address = ""
            consignee_name = ""
            consignee_address = ""
            shipping_fee = ""
            tip_fee = ""
            pay_type = ""
            item_type = ""
            order_amount = ""
            note = ""
            done_at = ""
            error_at = ""
            created_at = ""
            shipping_time = ""
            error_note = ""
            closed_note = ""
            is_direct_contracted = ""
            seller = vendor.get('seller', None)
            shop = vendor.get('shop', None)
            consignee = vendor.get('consignee', None)
            consignor = vendor.get('consignor', None)
            area_info = vendor.get('area_info', None)
            delivery_stock = vendor.get('delivery_stock', None)
            seller_order = vendor.get('seller_order', None)

            seller_order_state = ""

            if seller:
                seller_name = seller.get('name')
            if shop:
                shop_name = shop.get('name')
            if area_info:
                area_info_name = area_info.get('name')
            if delivery_stock:
                delivery_stock_name = delivery_stock.get('name')
            if seller_order:
                estimate_distance = seller_order.get('distance')
                shipping_fee = seller_order.get('shipping_fee')
                tip_fee = seller_order.get('tip_fee')
                pay_type = seller_order.get('pay_type')
                seller_order_state = seller_order.get('state')
                item_type = seller_order.get('item_type')
                order_amount = seller_order.get('order_amount')
                note = seller_order.get('note')
                error_note = seller_order.get('error_note')
                closed_note = seller_order.get('closed_note')
            if consignor:
                consignor_address = consignor.get('address')
                print consignor_address,'139===================================='
            else:
                print consignor,'142===================================='

            if consignee:
                consignee_name = consignee.get('name')
                consignee_address = consignee.get('address')
                print consignor_address,'146===================================='
            else:
                print consignor,'148===================================='

            if vendor.get('done_at'):
                _done_at_ = str(vendor.get('done_at')),
                _done_at = "".join(list(_done_at_))
                done_at = utc_time.format_data_str(str(_done_at))
            if vendor.get('closed_at'):
                _closed_at_ = str(vendor.get('closed_at'))
                _closed_at = "".join(list(_closed_at_))
                error_at = utc_time.format_data_str(str(_closed_at))
            if vendor.get('created_at'):
                _created_at_ = str(vendor.get('created_at'))
                _created_at = "".join(list(_created_at_))
                created_at = utc_time.format_data_str(str(_created_at))
            # if vendor.get('plan_shipping_time'):
            #     _shipping_time_ = str(vendor.get('plan_shipping_time'))
            #     _shipping_time = "".join(list(_shipping_time_))
            #     shipping_time = utc_time.format_data_str(str(_shipping_time))

            if vendor.get('is_direct_contracted') is True:
                is_direct_contracted = "直营"
            else:
                is_direct_contracted = "加盟"
            # _count = [
            #     # str(vendors.result_count),
            # ]
            _data = [
                str(vendor.get('id')),
                str(vendor.get('org_order_id')),
                str(vendor.get('barcode')),
                vendor.get('seller_order', None).get('seller',None).get('name',None).encode('gbk'),
                seller_name.encode('gbk'),
                # shop_name.encode('gbk'),
                self.biz_mode[str(vendor.get('biz_mode',None))].encode('gbk'),
                is_direct_contracted.encode('gbk'),
                area_info_name.encode('gbk'),
                delivery_stock_name.encode('gbk'),
                estimate_distance/1000.0,
                # vendor.get('consignor',None).get('address_detail',None),
                # vendor.get('consignee',None).get('name',None),
                # vendor.get('consignee',None).get('address_detail',None),
                consignor_address.encode('gbk'),
                consignee_name.encode('gbk'),
                consignee_address.encode('gbk'),
                shipping_fee/100.0,
                tip_fee/100.0,
                self.pay_type[str(pay_type)].encode('gbk'),
                self.vendor_state_dict[str(seller_order_state)].encode('gbk'),
                self.seller_type[str(item_type)].encode('gbk'),
                order_amount/100.0,
                # vendor.get('extra_services',None).get('payment',None).get('amount', None)/100.0,
                '',
                '',
                # vendor.get('extra_services',0).get('payment',0).get('amount', 0)/100.0,
                # vendor.get('extra_services',0).get('cod',0).get('amount', 0)/100.0,
                note.encode('gbk'),
                done_at,
                error_at,
                created_at,
                str(vendor.get('plan_shipping_time')),
                error_note.encode('gbk'),
                closed_note.encode('gbk'),
            ]

            # print ".......", shipment.get('org_order_id')
            self.vendor_list.append(_data)
            # self.count.append(_count)
        params['page'] += 1
        if vendors.has_more is True:
            return self.find_vendor_all(params)

    def set_csv(self):
        """

        :return:
        """
        csv_file = file(self.file_name, 'wb')
        writer = csv.writer(csv_file)
        _title = ['订单明细'.encode('gbk')]
        writer.writerow(_title)
        writer.writerow(self.count)
        _list = ['服务商订单编号'.encode('gbk'), '订单编号（商户订单编号）'.encode('gbk'), '条形编码'.encode('gbk'),'商家名称'.encode('gbk'), '商家联系人'.encode('gbk'),'业务模式'.encode('gbk'),'订单类型'.encode('gbk'),'配送区域'.encode('gbk'),'配送站'.encode('gbk'),'配送距离(km)'.encode('gbk'),'发货地址'.encode('gbk'),'顾客姓名'.encode('gbk'),'顾客地址'.encode('gbk'),'配送费(元)'.encode('gbk'),'小费(元)'.encode('gbk'),'结算方式'.encode('gbk'),'服务商订单状态'.encode('gbk'),'商品类型'.encode('gbk'),'订单金额(元)'.encode('gbk'),'代付商家（元）'.encode('gbk'),'代收顾客（元）'.encode('gbk'),'订单备注'.encode('gbk'),'送达时间'.encode('gbk'),'取消时间'.encode('gbk'),'下单时间'.encode('gbk'),'期望送达'.encode('gbk'),'异常原因'.encode('gbk'),'关闭原因'.encode('gbk')]
        writer.writerow(_list)
        print self.vendor_list,"92==="
        writer.writerows(self.vendor_list)
        csv_file.close()
        print '==== set_shop_csv ====: 统计csv生成成功！'

if __name__ == '__main__':

    server = VendorAxd()
    params = {
        # 'seller_id': '59506623998269645c3a899c',
        'vendor_id': "5982aad63d65ce390135ba08",
        'seller_id': "598bacfe3d65ce1285999871",
        'start_date': 20171011,
        'end_date': 20171011,
        'page': 1,
        'limit': 20,
    }
    server.run(**params)
    # Sendemail().send_email('/data/aa.csv', '花+  骑士运单-收到请回复谢谢', ['zhouyan@cityio.cn','tianyi.li@meishisong.cn','xiaoguang.jing@cityio.cn'])
