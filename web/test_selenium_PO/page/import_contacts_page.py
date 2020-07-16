#!/usr/bin/env web
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/15
# WEB自动化测试作业二importcontactspage(导入联系人页面)
# import_contacts_page.py
from selenium.webdriver.common.by import By
from web.test_selenium_PO.page.base_page import BasePage


class ImpContactsPage(BasePage):
    _base_url = ""
    """
    导入联系人方法
    """

    def import_contacts(self):
        self._find(By.CSS_SELECTOR, "#js_upload_file_input", 10).send_keys(
            "E:/pythonclass/pythonprj/web/test_selenium_PO/data/importdata.xlsx")
        self._find(By.CSS_SELECTOR, '#submit_csv', 10).click()
        self._find(By.CSS_SELECTOR, '#reloadContact', 10).click()
    # return ContactsPage(self._driver)
