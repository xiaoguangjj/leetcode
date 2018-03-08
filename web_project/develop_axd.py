# -*- coding:utf-8 -*-
import os
import sys
from bson import ObjectId

reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

from model import develop

class Develop(object):

    server = None

    def __init__(self):
        """

        :return:
        """
        pass


    def run(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.server = develop.Develop()
        self.develop_list = []
        self.get_develops(**kwargs)

    def get_develops(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        # self.find_develop_all(kwargs)
        #开发者详情接口
        self.get_develop_all(kwargs)
        # self.update_develop_all(kwargs)
        # self.create_develop_all(kwargs)

    def create_develop_all(self,params):
        develops = self.server.create(**params)
        print develops,#创造开发者

    def get_develop_all(self,params):
        """

        :param params:
        :return:
        """
        develops = self.server.get(**params)
        print develops,"开发者" #打印开发者详情接口

    def update_develop_all(self,params):
        """

        :param params:
        :return:
        """
        develops = self.server.update(**params)
        print develops, "79=========="

    def find_develop_all(self, params):
        """

        :param params:
        :return:
        """
        develops = self.server.find(**params)
        for develop in develops.data:
            _data = [
                str(develop.get('id')),
                str(develop.get('org_id')),
                str(develop.get('access_key')),
                str(develop.get('secret_key')),
                str(develop.get('hook_url')),
                self.develop_state_dict[str(develop.get('state'))].encode('gbk'),
                str(develop.get('callback_timeout')),
            ]
            # print ".......", shipment.get('org_order_id')
            print _data, "77======"
            self.develop_list.append(_data)
        # params['page'] += 1
        if develops.has_more is True:
            return self.find_develop_all(params)

    # def dev_update(self):
    #     seaguard_client = aoao_seaguard_client(app_code='aoao_admin')
    #
    #     spec = {
    #         'org_id': '582aa5003d65ce2f979aade1',
    #         'hook_url': '',
    #         'events': [],
    #     }
    #     params = {
    #         "dev_id": "58c7ab749982694a3c231c5a"
    #     }
    #     # result = winterfell_client.common_dev_info.update(params, **spec)
    #     print result
    #     assert False


if __name__ == '__main__':

    server = Develop()

    spec_create = {
        'org_id': '5978480999826931309aacc1',
        'org_type': 2,
        'operator_id': '59c88a6a9f3028207ba1b999',
        'state': 100,
        'live_mode': True,
    }

    spec_info = {
        'dev_id': '59b272a69982690cd2f21958',
    }

    spec_update = {
        'dev_id': '59b272a69982690cd2f21958',
    }

    spec_update_param = {
        'org_id': '5978480999826931309aacc1',
        'operator_id': '59b272a69982690cd2f21958',
    }

    get_develop_info = {
        'org_id': '59f2b3d33d65ce5a3d2eee20',
        # 'page': 1,
        # 'limit': 2,
    }

    # server.dev_update()

    #开发者信息创建接口
    # server.run(**spec_create)

    #开发者详情接口
    # server.run(**spec_info)

    #开发者信息编辑接口
    # server.run(spec_update, **spec_update_param)

    #获取开发者信息
    server.run(**get_develop_info)
    # Sendemail().send_email('/data/aa.csv', '花+  骑士运单-收到请回复谢谢', ['zhouyan@cityio.cn','tianyi.li@meishisong.cn','xiaoguang.jing@cityio.cn'])
