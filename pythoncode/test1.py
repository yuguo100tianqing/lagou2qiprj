#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/06/28
# python实战一#作业：创建模块，模块里面创建方法，定义有参数，和无参，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。（实例化）
# 调用girl_frend模块代码


from pythoncode.girl_frend import girlfrend

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
ssa = ['ww', 'xx', 'yy']
print(ssa[-1])

ssb = 'E:\\pythonclass\\HGAutoTest\\HGWebAuto\\pages\\base_page\\base_page.py'
print(ssb)
ssbl = ssb.split("\\")
print(ssbl)
del ssbl[-3:-1]
del ssbl[-1]
ssc = "/".join(ssbl)
print(ssc)
exit()

# data1=input("请输入数字：")
# data = int(data1)
# while True:
#     if data%2 == 1:
#         if data ==1:
#             break
#         data = data*3+1
#         print(data)
#     elif data%2 == 0:
#         data = data/2
#         print(data)
# exit()
