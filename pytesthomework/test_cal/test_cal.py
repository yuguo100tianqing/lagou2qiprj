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
# test_cal.py

import pytest
import yaml

try:
    with open("./cal.yml", encoding='UTF-8') as f:
        data = yaml.safe_load(f)
    print(data)
    print("111")
except FileNotFoundError:
    print("测试数据文件未找到！")


class TestCal:
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    @pytest.mark.parametrize(['a', 'b', 'value'], data['mul'])
    def test_mul(self, calinit, a, b, value):
        assert value == calinit.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['mul'])
    @pytest.mark.parametrize(['a', 'b', 'value'], data['dev'])
    def test_dev(self, calinit, a, b, value):
        assert value == calinit.dev(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    @pytest.mark.parametrize(['a', 'b', 'value'], data['add'])
    def check_add(self, calinit, a, b, value, cmdoption):
        print(f"{cmdoption['host']}")
        assert value == calinit.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['add'])
    @pytest.mark.parametrize(['a', 'b', 'value'], data['sub'])
    def check_sub(self, calinit, a, b, value):
        assert value == calinit.sub(a, b)
