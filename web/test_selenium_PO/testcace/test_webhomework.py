#!/usr/bin/env web
# -*- coding: utf-8 -*-
# test1.py
# auth by yuguotianqing01
# date 2020/07/15
# WEB自动化测试作业二测试用例
# test_webhomework.py
import pytest

from web.test_selenium_PO.page.main_page import MainPage


class TestWebHw:
    """每个用例执行前要初始化mainpage"""

    def setup(self):
        self.mainpage = MainPage()
        print("开始测试")

    def teardown(self):
        print("结束测试")
        pass

    """测试添加联系人功能，从主页跳转"""

    @pytest.mark.dependency(name='add')
    def test_addcont(self):
        self.mainpage.goto_addcontactpage().add_contact()
        contlist = self.mainpage.goto_contactspage().get_member_list_in()
        assert "王晓晓" in contlist

    """测试删除联系人功能"""

    @pytest.mark.dependency(depends=['add'])
    def test_deladdcont(self):
        contlist = self.mainpage.goto_contactspage().delete_contact().get_member_list_not_in()
        assert "王晓晓" not in contlist

    """测试导入联系人功能"""

    def test_impcont(self):
        self.mainpage.goto_importcontactspage().import_contacts()
        contlist = self.mainpage.goto_contactspage().get_member_list_in()
        assert "阳春白雪" in contlist

    """测试添加联系人功能，从通讯录页面跳转"""

    def test_addcont_from_contacts_page(self):
        self.mainpage.goto_contactspage().goto_addcontactpage().add_contact()
        contlist = self.mainpage.goto_contactspage().get_member_list_in()
        assert "王晓晓" in contlist

    """测试导入联系人功能，从通讯录页面跳转"""

    def test_impcont_from_contacts_page(self):
        self.mainpage.goto_contactspage().goto_importcontactspage().import_contacts()
        contlist = self.mainpage.goto_contactspage().get_member_list_in()
        assert "阳春白雪" in contlist
