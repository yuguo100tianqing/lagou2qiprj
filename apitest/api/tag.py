#!/usr/bin/env web
# -*- coding: utf-8 -*-
# tag.py
# auth by wangxg
# date 2020/08/16
# 企业微信接口测试二

from apitest.api.base_api import BaseApi


class Tag(BaseApi):

    def add_tag(self, tagname, tagid, token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }
        r = self.send_api(data)
        return r

    def update_tag(self, tagid, tagname, token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
            "json": {
                "tagid": tagid,
                "tagname": tagname
            }
        }
        r = self.send_api(data)
        return r

    def del_tag(self, tagid, token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}",
            "params": {
                "tagid": tagid
            }
        }
        r = self.send_api(data)
        return r

    def get_tag(self, tagid, token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}",
            "params": {
                "tagid": tagid
            }
        }
        r = self.send_api(data)
        return r

    def get_taglist(self, token):
        data = {"method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"}
        res = self.send_api(data)
        return res['taglist']
