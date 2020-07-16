#!/usr/bin/env web
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/15
# WEB自动化测试作业二basepage
# base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 如果没有传入driver，就初始化driver，否则就直接使用传入的driver
        if driver is None:
            # 初始化浏览器复用参数
            option = Options()
            option.debugger_address = "localhost:9222/"
            # 加载谷歌浏览器
            self._driver = webdriver.Chrome(options=option)
            # 隐式等待10秒
            self._driver.implicitly_wait(10)
        else:
            self._driver = driver
            # 如果_base_url不为空，则调用get方法
        if self._base_url != "":
            self._driver.get(self._base_url)

    # 定义_find方法，为显式等待，WebDriverWait类中until返回的是expected_conditions.presence_of_element_located方法的返回值
    # expected_conditions.presence_of_element_located方法的返回值的返回值为element
    def _find(self, by, value, time):
        return WebDriverWait(self._driver, time).until(expected_conditions.presence_of_element_located((by, value)))

    # 定义_finds方法，为显式等待，WebDriverWait类中until返回的是expected_conditions.presence_of_elements_located方法的返回值
    # expected_conditions.presence_of_elements_located方法的返回值的返回值为element列表
    def _finds(self, by, value, time):
        return WebDriverWait(self._driver, time).until(
            expected_conditions.presence_of_all_elements_located((by, value)))
