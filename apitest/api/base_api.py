#!/usr/bin/env web
# -*- coding: utf-8 -*-
# base_api.py
# auth by wangxg
# date 2020/08/16
# 企业微信接口测试二
import requests


class BaseApi:
    def send_api(self, req: dict):
        # 请求的封装
        return requests.request(**req).json()
