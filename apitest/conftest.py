#!/usr/bin/env pytest
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/03
# !/usr/bin/env web
# -*- coding: utf-8 -*-
# test_tag.py
# auth by wangxg
# date 2020/08/16
# 企业微信接口测试二

import pytest
from typing import List

from apitest.api.wework import Wework


@pytest.fixture(scope="session")
def token(tmp_path_factory, worker_id):
    wework = Wework()
    yield wework.get_token(tmp_path_factory, worker_id)


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # items 就是所有的测试用例列表，item代表每个测试用例对象
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",  # 注册一个命令行属性
                      default='test',
                      dest='env',
                      help='set your run env'
                      )
    # mygroup.addoption("--env0",  # 注册一个命令行属性
    #                   default='dev',
    #                   dest='env0',
    #                   help='set your run env'
    #                   )
    # mygroup.addoption("--env1",  # 注册一个命令行属性
    #                   default='st',
    #                   dest='env1',
    #                   help='set your run env'
    #                   )

# @pytest.fixture(scope='session', autouse=True)
# def cmdoption(request):
#     myenv = request.config.getoption("--env", default='test')
#     if myenv == 'test':
#         try:
#             print("获取测试环境数据")
#             with open("data/test/test.yml") as f:
#                 datas = yaml.safe_load(f)
#                 print(datas)
#         except FileNotFoundError:
#             print("测试环境数据文件未找到！")
#             datas = "测试环境数据文件未找到！"
#     elif myenv == 'dev':
#         try:
#             print("获取开发环境数据")
#             with open("data/dev/dev.yml") as f:
#                 datas = yaml.safe_load(f)
#                 print(datas)
#         except FileNotFoundError:
#             print("开发环境数据文件未找到！")
#             datas = "开发环境数据文件未找到！"
#     elif myenv == 'st':
#         try:
#             print("获取st环境数据")
#             with open("data/st/st.yml") as f:
#                 datas = yaml.safe_load(f)
#                 print(datas)
#         except FileNotFoundError:
#             print("st环境数据文件未找到！")
#             datas = "st环境数据文件未找到！"
#     return datas
