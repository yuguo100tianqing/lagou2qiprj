#!/usr/bin/env pytest
# -*- coding: utf-8 -*-
# test_sample.py
# auth by yuguotianqing01
# date 2020/07/01
# pytest1
import pytest


def func(x):
    return x * 2 + 1


# def setup_module():
#     print("初始化模块")
#
# def teardown_module():
#     print("模块测试完成")

# def setup_function():
#     print("初始化函数")
#
#
# def teardown_function():
#     print("函数测试完成")
#
#
# def test_a():
#     assert 1 == 1

# 放在类里面
# def setup_class(self):
#     print("初始化类")
#
# def teardown_class(self):
#     print("类测试完成")
#
# def setup(self):
#     self.cal = Calculator()
#     print("初始化计算器")
#
# def teardown(self):
#     print("测试完成")

@pytest.fixture()
def login():
    print("login......")
    return 'miaomiao'


@pytest.mark.flaky(reruns=5, reruns_delay=1)
def test_answer(login):
    print(f"{login}")
    assert func(2) == 5


def test_answer2():
    assert func(3) == 6


if __name__ == '__main__':
    pytest.main(['test_sample.py'])
