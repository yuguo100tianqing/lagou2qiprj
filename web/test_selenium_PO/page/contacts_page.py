#!/usr/bin/env web
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/15
# WEB自动化测试作业二contactspage(通讯录页面)
# contacts_page.py

from selenium.webdriver.common.by import By
from web.test_selenium_PO.page.add_contact_page import AddContactPage
from web.test_selenium_PO.page.base_page import BasePage
from web.test_selenium_PO.page.import_contacts_page import ImpContactsPage


class ContactsPage(BasePage):
    _base_url = ""
    """
    跳转到添加联系人页面
    """

    def goto_addcontactpage(self):
        elements = self._finds(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_add_member', 10)
        elements[2].click()
        return AddContactPage(self._driver)

    """
    跳转到导入联系人页面
    """

    def goto_importcontactspage(self):
        self._finds(By.CSS_SELECTOR, '.ww_btn_PartDropdown_left', 10)[2].click()
        elements = self._finds(By.CSS_SELECTOR, '.qui_dropdownMenu_itemLink.ww_dropdownMenu_itemLink.js_import_member',
                               10)
        print(elements)
        elements[2].click()
        return ImpContactsPage(self._driver)

    """
    删除联系人方法
    """

    def delete_contact(self):
        self._find(By.CSS_SELECTOR,
                   '#member_list > tr:nth-child(2) > td.js_checkbox_container.member_colRight_memberTable_td.member_colRight_memberTable_td_Checkbox',
                   10).click()
        self._find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_delete', 10).click()
        self._finds(By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue', 10)[1].click()

        return ContactsPage(self._driver)

    """
    获取联系人列表
    """

    def get_member_list_in(self):
        self._driver.refresh()
        # 获取人员列表中的所有姓名
        getlist_elements = self._finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)', 10)
        print(len(getlist_elements))
        memlist = []
        for i in range(len(getlist_elements)):
            memlist.append(getlist_elements[i].text)
        return memlist

    def get_member_list_not_in(self):
        self._driver.refresh()
        # 获取人员列表中的所有姓名
        getlist_elements = self._finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)', 10)
        print(len(getlist_elements))
        memlist = []
        for i in range(len(getlist_elements)):
            memlist.append(getlist_elements[i].text)
        return memlist
