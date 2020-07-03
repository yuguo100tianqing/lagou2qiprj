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


@pytest.fixture(scope="function", autouse=True)
def startstop():
    print('开始计算')
    yield None
    print('计算结束')


@pytest.fixture()
def calinit():
    cal = Calculator()
    return cal
