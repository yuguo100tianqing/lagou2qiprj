#!/usr/bin/env web
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/15
# WEB自动化测试作业二addcontactpage(添加联系人页面)
# add_contacts_page.py
from selenium.webdriver.common.by import By
from web.test_selenium_PO.page.base_page import BasePage


class AddContactPage(BasePage):
    _base_url = ""
    """
    添加联系人方法
    """

    def add_contact(self):
        self._find(By.ID, 'username', 10).send_keys('王晓晓')
        self._find(By.ID, 'memberAdd_acctid', 10).send_keys('ssdfddf')
        self._find(By.ID, 'memberAdd_phone', 10).send_keys('13000000000')
        self._find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save', 10).click()
