#!/usr/bin/env pytest
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/03
# pytset实战一
# 1、补全计算器（加减乘除）的测试用例
# 2、使用数据驱动完成测试用例的自动生成
# 3、conftest.py中创建fixture 完成setup和teardown
# 4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
# conftest.py

import pytest
import yaml
from pytesthomework.test_cal.cal import *
from typing import List

@pytest.fixture(scope="function", autouse=True)
def startstop():
    print('开始计算')
    yield None
    print('计算结束')


@pytest.fixture()
def calinit():
    cal = Calculator()
    return cal


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


@pytest.fixture(scope='session', autouse=True)
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        try:
            print("获取测试环境数据")
            with open("data/test/test.yml") as f:
                datas = yaml.safe_load(f)
                print(datas)
        except FileNotFoundError:
            print("测试环境数据文件未找到！")
            datas = "测试环境数据文件未找到！"
    elif myenv == 'dev':
        try:
            print("获取开发环境数据")
            with open("data/dev/dev.yml") as f:
                datas = yaml.safe_load(f)
                print(datas)
        except FileNotFoundError:
            print("开发环境数据文件未找到！")
            datas = "开发环境数据文件未找到！"
    elif myenv == 'st':
        try:
            print("获取st环境数据")
            with open("data/st/st.yml") as f:
                datas = yaml.safe_load(f)
                print(datas)
        except FileNotFoundError:
            print("st环境数据文件未找到！")
            datas = "st环境数据文件未找到！"
    return datas
