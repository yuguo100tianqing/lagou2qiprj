#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_sample.py
# auth by yuguotianqing01
# date 2020/07/01
# pytest1

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
