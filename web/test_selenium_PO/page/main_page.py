#!/usr/bin/env web
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/15
# WEB自动化测试作业二mainpage(主页)
# main_page.py
from selenium.webdriver.common.by import By
from web.test_selenium_PO.page.add_contact_page import AddContactPage
from web.test_selenium_PO.page.base_page import BasePage
from web.test_selenium_PO.page.contacts_page import ContactsPage
from web.test_selenium_PO.page.import_contacts_page import ImpContactsPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    """
    跳转到添加联系人页面
    """

    def goto_addcontactpage(self):
        self._find(By.XPATH,
                   '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]',
                   10).click()
        return AddContactPage(self._driver)

    """
    跳转到联系人页面
    """

    def goto_contactspage(self):
        self._find(By.CSS_SELECTOR, '#menu_contacts > span', 10).click()
        return ContactsPage(self._driver)

    """
    跳转到导入联系人页面
    """

    def goto_importcontactspage(self):
        self._find(By.XPATH,
                   '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]',
                   10).click()
        return ImpContactsPage(self._driver)
