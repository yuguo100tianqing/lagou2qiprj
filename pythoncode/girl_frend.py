#!/usr/bin/env python
# -*- coding: utf-8 -*-
# girl_frend.py
# auth by yuguotianqing01
# date 2020/06/28
# python实战一#作业：创建模块，模块里面创建方法，定义有参数，和无参，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。
class girlfrend():
    have_girl = False

    def _init_(self):  # 无参数
        self.have_girl = False
        print(f"{have_girl}")

    def send(self, name="yoyo"):  # 有参数，默认为yoyo，无返回值
        self.have_girl = True
        print(f"国家给{name}发女朋友啦！")

    def lost(self, name="yoyo"):  # 有参数，默认为yoyo，无返回值
        self.have_girl = False
        print(f"{name}失恋了，嘤嘤嘤！")

    def showgirl(self, name="yoyo"):  # 有参数，默认为yoyo，有返回值
        if self.have_girl == True:
            return name + "有女朋友，好开心~~~"
        else:
            return name + "是单身狗，嘤嘤嘤~_~"

# mygirl=girlfrend()
# girl=mygirl.showgirl("yuguo100tianqing")#有默认值，传入与默认值不同的值,有返回值
# print(girl)
# name="yuguotianqing"
# mygirl.send(name)#有默认值，传入与默认值不同的值,无返回值
# girl=mygirl.showgirl(name)#有默认值，传入与默认值不同的值,有返回值
# print(girl)
# mygirl.lost()#有默认值(yoyo)，不传入参数,无返回值
# girl=mygirl.showgirl()#有默认值(yoyo)，不传入参数,有返回值
# print(girl)
# exit()
