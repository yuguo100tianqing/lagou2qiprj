#!/usr/bin/env web
# -*- coding: utf-8 -*-
# test_WeWork.py
# auth by wangxg
# date 2020/08/15
# 企业微信接口测试
import requests


class TestWeworkAccess:
    def setup(self):
        params = {
            "corpid": "ww349bb43ccdb0224d",
            "corpsecret": "vGqhlRNaP-hTTU1ofiGTBeAhlwhtNqFEGmYiK0YJiTI"
        }
        self.s = requests.Session()
        res = self.s.get(url=" https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        # 将token放入会话对象中
        self.s.params.update({"access_token": res.json()['access_token']})

    """
    添加成员
    """

    def test_Add(self):
        data = {
            "userid": "meiqi",
            "name": "美琪",
            "alias": "Miki",
            "mobile": "+86 13800001234",
            "department": [2],
            "order": [2],
            "position": "经理",
            "gender": "2",
            "email": "meiqi@daozhang.com",
            "is_leader_in_dept": [1],
            "enable": 1,
            "telephone": "020-123456",
            "address": "广州市海珠区新港中路",
            "main_department": 1
        }
        res = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create", json=data)
        self.s.params.update({"userid": "meiqi"})
        print(res.json())
        res2 = self.s.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get")
        assert res2.json()['name'] == "美琪"
        print("222")
        print(res2.json())
        print("111")

    """
    查看成员
    """

    def test_Get(self):
        self.s.params.update({"userid": "meiqi"})
        res = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get")
        print(res.json())
        assert res.json()['name'] == "美琪"

    """
    更新成员
    """

    def test_Update(self):
        data = {
            "userid": "meiqi",
            "name": "美琪琪",
            "alias": "Miki",
            "mobile": "+86 138000012346",
            "position": "秘书",
            "email": "meiqiqi@daozhang.com",
        }
        res = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update", json=data)
        print(res.json())
        self.s.params.update({"userid": "meiqi"})
        res = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get")
        print(res.json())
        assert res.json()['name'] == "美琪琪"

    """
    删除成员
    """

    def test_Delete(self):
        self.s.params.update({"userid": "meiqi"})
        res = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete")
        print(res.json())
        assert res.json()["errcode"] == 0
