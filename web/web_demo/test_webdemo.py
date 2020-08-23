#!/usr/bin/env pytest
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/15
# WEB自动化测试demo&telne自动化测试demo
# test_webdemo.py

import telnetlib
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


# 谷歌浏览器demo
class Test_web_chrom:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.close()

    def test_selenium_chrome(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("csdn")
        var = self.driver.find_element_by_css_selector("#su").get_attribute("value")
        print(var)
        self.driver.find_element_by_css_selector("#su").click()
        sleep(3)


# 火狐浏览器demo
class Test_web_firefox:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.close()

    def test_selenium_firefox(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("csdn")
        var = self.driver.find_element_by_css_selector("#su").get_attribute("value")
        print(var)
        self.driver.find_element_by_css_selector("#su").click()
        sleep(3)


# 电信设备demo
class Test_web_dianxindemo:
    def setup_class(self):
        self.CTun = 'telecomadmin'
        self.CTpw = 'nE7jA%5m'
        self.CTaddr = "http://192.168.1.1:8080"
        self.CMun = 'CMCCAdmin'
        self.CMpd = 'aDm8H%MdA'
        self.CMaddr = "http://192.168.1.1"
        self.driver = webdriver.Chrome()
        self.driver.get(self.CTaddr)
        self.driver.implicitly_wait(10)
        print("111")

    def teardown_class(self):
        sleep(10)
        self.driver.close()

    @pytest.mark.run(order=1)
    def test_selenium_dianxin_login_error(self):
        sleep(10)
        self.driver.find_element_by_css_selector("#user_name").clear()
        self.driver.find_element_by_css_selector("#user_name").send_keys('telecomadmin')
        self.driver.find_element_by_css_selector("#password").clear()
        self.driver.find_element_by_css_selector("#password").send_keys('nE7jA%5m1')
        self.driver.find_element_by_css_selector("#login_btn").click()
        # i1=self.driver.find_element_by_css_selector('#panel_content > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1)')
        i2 = self.driver.find_element_by_css_selector("#login_error_hint > font:nth-child(1)").get_attribute(
            'innerHTML')
        print(i2)
        assert i2 == "密码输入错误，请重新输入"

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(name='login')
    def test_selenium_dianxin_login(self):
        sleep(10)
        self.driver.find_element_by_css_selector("#user_name").clear()
        self.driver.find_element_by_css_selector("#user_name").send_keys(self.CTun)
        self.driver.find_element_by_css_selector("#password").clear()
        self.driver.find_element_by_css_selector("#password").send_keys(self.CTpw)
        self.driver.find_element_by_css_selector("#login_btn").click()
        i2 = self.driver.find_element_by_css_selector("#Menu2_Sta_Overview").get_attribute('innerHTML')
        print(i2)
        assert i2 == "状态总览"

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(depends=['login'])
    def test_selenium_dianxin(self, datainit):
        data = datainit
        sleep(10)
        # i2=self.driver.find_element_by_id("Table_base1_1_table").get_attribute('innerHTML')
        # print(i2)
        # sleep(5)
        # var = i.text
        # var2=self.driver.execute_script("return arguments[0].innerHTML",i1)
        # print(var)
        # print(f"{var2}")
        self.driver.find_element_by_css_selector("#Menu1_Network").click()
        selector = Select(self.driver.find_element_by_css_selector("#WanConnectName_select"))
        options = selector.options
        print(options)
        resultlist = []
        for index in range(0, len(options)):
            var3 = options[index].text
            resultlist.append(var3)
        wanlist = []
        for index in range(0, len(options) - 1):
            wanindex = "Wan" + str(index + 1)
            wanlist.append(data["default"][wanindex])
        wanlist.append("新增WAN连接")
        assert resultlist == wanlist


# telnet设备demo
class Test_telnet_demo:
    def setup_class(self):
        try:
            self.session = telnetlib.Telnet()
            self.session.open("10.182.25.181", port=23)
        except:
            print("网络连接失败")

    def teardown_class(self):
        sleep(10)
        self.session.close()

    def test_telnet(self):
        self.session.read_until(b'Login:', timeout=10)
        self.session.write(b'GEPON\n')
        self.session.read_until(b'Password:', timeout=10)
        self.session.write(b'GEPON\n')
        self.session.read_until(b'User>', timeout=10)
        self.session.write(b'EN\n')
        self.session.read_until(b'Password:', timeout=10)
        self.session.write(b'GEPON\n')
        sleep(2)
        result = self.session.read_until()
        print(str(result))
        self.session.close()
        assert b'Admin#' in result


class Test_serial_demo:
    def setup_class(self):
        try:
            self.session = telnetlib.Telnet()
            self.session.open("192.168.1.1", port=23)
        except:
            print("网络连接失败")

    def teardown_class(self):
        sleep(10)
        self.session.close()

    def test_serial(self):
        res = self.session.read_until(b'login:', timeout=10)
        print(res)
        self.session.write(b'admin\n')
        res = self.session.read_until(b'Password:', timeout=10)
        print(res)
        self.session.write(b'nE7jA%5m\n')
        res = self.session.read_until(b'#', timeout=10)
        print(res)
        self.session.write(b'free\n')
        res = self.session.read_until(b'#', timeout=10)
        print(res)
        sleep(2)
        self.session.close()
        assert b'Mem' in res
