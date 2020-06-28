#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/06/28
# python实战一#作业：创建模块，模块里面创建方法，定义有参数，和无参，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。（实例化）
# 调用girl_frend模块代码

import girl_frend
from girl_frend import *

mygirl = girlfrend()
girl = mygirl.showgirl("yuguo100tianqing")  # 有默认值，传入与默认值不同的值,有返回值
print(girl)
name = "yuguotianqing"
mygirl.send(name)  # 有默认值，传入与默认值不同的值,无返回值
girl = mygirl.showgirl(name)  # 有默认值，传入与默认值不同的值,有返回值
print(girl)
mygirl.lost()  # 有默认值(yoyo)，不传入参数,无返回值
girl = mygirl.showgirl()  # 有默认值(yoyo)，不传入参数,有返回值
print(girl)
exit()
