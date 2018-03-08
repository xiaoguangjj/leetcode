# -*- coding:utf-8 -*-
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

from shuttle.config import load_runtime_cfg
from client import client as _seaguard_client
from winterfell import WinterfellClient


@pytest.fixture(scope='session')
def app_config():
    config = load_runtime_cfg('SHUTTLE_APP_CFG', os.path.join(TEST_DIR, '..', 'seaguard.example.yml'))
    config.from_yaml_file(os.path.join(TEST_DIR, 'seaguard_test.yml'), True)
    return config


@pytest.fixture(scope='session')
def winterfell_client():
    config = app_config()
    winterfell_cfg = config.get('winterfell')
    if not winterfell_cfg:
        winterfell_cfg = {
            'endpoint': 'tcp://127.0.0.1:9292',
            'namespace': 'winterfell'
        }
    client = WinterfellClient(winterfell_cfg['endpoint'], winterfell_cfg['namespace'])
    return client


@pytest.fixture(scope='session')
def app_registry():
    winterfell = winterfell_client()
    appstore_registry = winterfell.appstore_registry
    results = appstore_registry.find()
    if not results:
        return
    key_records = {}
    for record in results:
        keys = appstore_registry.find_keys(id=record.id)
        if not keys:
            continue
        for key in keys:
            key_records[key['access_key']] = {
                'app_id': record['id'],
                'app_code': record['app_code'],
                'name': record['name'],
                'state': record['st ate'],
                'secret_key': key['secret_key'],
                'access_key': key['access_key'],
            }
    return key_records


@pytest.fixture(scope='session')
def seaguard_client():
    app_keys = app_registry()
    cfg = app_config()
    ios_keys = filter(lambda x: x['app_code'] == "aoao_ios", app_keys.values())[0]
    access_key = ios_keys['access_key']
    secret_key = ios_keys['secret_key']
    _seaguard_client.HTTP_API_GATEWAY = cfg['seaguard_http_gw']
    client = _seaguard_client.Client(access_key, secret_key)
    client.mock_app_id = ios_keys['app_id']
    return client


def aoao_seaguard_client(app_code="aoao_ios"):
    app_keys = app_registry()
    cfg = app_config()
    keys = filter(lambda x: x['app_code'] == app_code, app_keys.values())[0]
    access_key = keys['access_key']
    secret_key = keys['secret_key']
    _seaguard_client.HTTP_API_GATEWAY = cfg['seaguard_http_gw']
    client = _seaguard_client.Client(access_key, secret_key)
    client.mock_app_id = keys['app_id']
    return client
