# -*- coding:utf-8 -*-
import sys
import json,urllib2
import csv
reload(sys)
sys.setdefaultencoding('utf8')

file_name = '/data/info.csv'
data =[ ]

def get_csv_create_order():
        """
        :return:
        """
        csv_file = file(file_name, 'r')
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            body = {
                "ID":row[0].decode('gbk').encode('utf-8'),
                "barcode":row[1].decode('gbk').encode('utf-8'),
                "name":row[2].encode('utf-8'),
                "main_class":row[3].encode('utf-8'),
                "sub_class":row[4].encode('utf-8'),
                "price":row[5].decode('gbk').encode('utf-8')
            }
            data.append(body)
        print json.dumps(data)
        csv_file.close()
        print '==== set_shop_csv ====: 统计csv生成成功！'

if __name__ == "__main__":
    get_csv_create_order()