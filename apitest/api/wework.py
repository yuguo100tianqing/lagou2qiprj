#!/usr/bin/env web
# -*- coding: utf-8 -*-
# wework.py
# auth by wangxg
# date 2020/08/16
# 企业微信接口测试二
import json

import pytest

from apitest.api.base_api import BaseApi
from filelock import FileLock


class Wework(BaseApi):
    def _token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                'corpid': "ww349bb43ccdb0224d",
                'corpsecret': "vGqhlRNaP-hTTU1ofiGTBeAhlwhtNqFEGmYiK0YJiTI"
            }
        }
        r = self.send_api(data)
        try:
            return r['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    def get_token(self, tmp_path_factory, worker_id):
        if not worker_id:
            # not executing in with multiple workers, just produce the data and let
            # pytest's fixture caching do its job
            return self._token()

        root_tmp_dir = tmp_path_factory.getbasetemp().parent
        print(root_tmp_dir)

        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                data = json.loads(fn.read_text())
            else:
                data = self._token()
                fn.write_text(json.dumps(data))
        return data
