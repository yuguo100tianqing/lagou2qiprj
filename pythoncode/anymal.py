#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/06/28
# python实战二

# 1、创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
import yaml


class Animal():
    """动物类，包含动物基本属性"""

    def __init__(self, name="Yoyo", color="white", age=0, sex="female"):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def canRun(self):
        """会跑"""
        Run = self.name + " " + "can run。"
        print(Run)
        return Run

    def canCry(self):
        """会叫"""
        Cry = self.name + " " + "can cry。"
        print(Cry)
        return Cry


# 2、创建子类【猫】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属
# - 添加一个新的属性，毛发=短毛，
# - 添加一个新的方法， 会捉老鼠，
# - 复写父类的‘【会叫】的方法，改成【喵喵叫】
class Cat(Animal):
    """猫的特性"""

    def __init__(self, name="Yoyo", color="white", age=0, sex="female", hair="short"):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def canCry(self):
        """会喵喵叫"""
        Cry = self.name + " " + "can cry as 'Miaomiao~'."
        print(Cry)
        return Cry

    def canCatchMice(self):
        """会抓老鼠"""
        Catch = self.name + " " + "can catch mice."
        print(Catch)
        return Catch


# 创建子类【狗】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发=长毛，
# - 添加一个新的方法， 会看家，
# - 复写父类的【会叫】的方法，改成【汪汪叫】
class Dog(Animal):
    """猫的特性"""

    def __init__(self, name="Yoyo", color="white", age=0, sex="female", hair="long"):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def canCry(self):
        """会汪汪叫"""
        Cry = self.name + " " + "can cry as 'Wangwang~'."
        print(Cry)
        return Cry

    def canMindTheHouse(self):
        """会看家"""
        Mind = self.name + " " + "can mind the house."
        print(Mind)
        return Mind


# 创建一个猫猫实例
# - 调用捉老鼠的方法
# - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
mimi = Cat("Mimi", "yellow", 1)  # 猫咪 名字叫咪咪，黄色，1岁，母猫（默认），短毛（默认）
mimi.canCatchMice()  # 会捉老鼠
# mimi.canCry()
if mimi.sex == "male":
    HisOrHer = "his"
    HeOrShe = "he"
else:
    HisOrHer = "her"
    HeOrShe = "she"

print(
    f"The cat's name is {mimi.name}, {HisOrHer} color is {mimi.color} , it is {mimi.age} years old, it is a {mimi.sex},{HisOrHer} hair is {mimi.hair},{HeOrShe} catched the mouse.")

# 创建一个狗狗实例
# - 调用【会看家】的方法
# - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
doudou = Dog("Doudou", "black", 3, "male")  # 狗狗 名字叫豆豆，黑色，1岁，公狗，长毛（默认）
doudou.canMindTheHouse()  # 会看家
# doudou.canCry()
if doudou.sex == "male":
    HisOrHer = "his"
    HeOrShe = "he"
else:
    HisOrHer = "her"
    HeOrShe = "she"

print(
    f"The dog's name is {doudou.name}, {HisOrHer} color is {doudou.color} , it is {doudou.age} years old, it is a {doudou.sex},{HisOrHer} hair is {doudou.hair}.")

# 4、使用 yaml 来管理实例的属性
try:
    with open("anymal.yml") as f:
        data = yaml.load(f, yaml.FullLoader)
        # print(data["cat"])
        anymal1 = Cat(data["cat"]["name"], data["cat"]["color"], data["cat"]["age"], data["cat"]["sex"])
        anymal1.canCatchMice()  # 会捉老鼠
        # mimi.canCry()
        if anymal1.sex == "male":
            HisOrHer = "his"
            HeOrShe = "he"
        else:
            HisOrHer = "her"
            HeOrShe = "she"

        print(
            f"The cat's name is {anymal1.name}, {HisOrHer} color is {anymal1.color} , it is {anymal1.age} years old, it is a {anymal1.sex},{HisOrHer} hair is {anymal1.hair},{HeOrShe} catched the mouse.")

        anymal2 = Dog(data["dog"]["name"], data["dog"]["color"], data["dog"]["age"], data["dog"]["sex"])
        anymal2.canMindTheHouse()
        if anymal2.sex == "male":
            HisOrHer = "his"
            HeOrShe = "he"
        else:
            HisOrHer = "her"
            HeOrShe = "she"

        print(
            f"The dog's name is {anymal2.name}, {HisOrHer} color is {anymal2.color} , it is {anymal2.age} years old, it is a {anymal2.sex},{HisOrHer} hair is {anymal2.hair}.")

except FileNotFoundError:
    msg = "Sorry,the file " + "anymal.yml" + " doesn't exist."
    print(msg)

# 提交代码到自己的github仓库， 贴到作业贴上
