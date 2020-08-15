# from mitmproxy import http
#
# def request(flow: http.HTTPFlow):
#     # redirect to different host
#     if "quote.json" in flow.request.url:
#         with open("E:\pythonclass\pythonprj\Mock\mock2.json") as f:
#             flow.response = http.HTTPResponse.make(
#                 200, f.read(),
#             )

import json
from pprint import pprint

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # redirect to different host
    if "quote.json" in flow.request.url and "x=" in flow.request.url:
        ## 先接收到返回信息
        data = json.loads(flow.response.content)
        with open("E:\pythonclass\pythonprj\Mock\mock2.json", "w+") as f:
            json.dump(data, f)
        print("=============修改前的信息========start====================")
        pprint(data)
        print("=============修改前的信息========end======================")
        ## 中间做一些修改
        data["data"]["items"][0]["quote"]["name"] = data["data"]["items"][0]["quote"]["name"]
        data["data"]["items"][1]["quote"]["name"] += data["data"]["items"][1]["quote"]["name"]
        data["data"]["items"][2]["quote"]["name"] = ""
        data["data"]["items"][3]["quote"]["name"] = data["data"]["items"][3]["quote"]["name"] + "HMS"
        ## 修改返回信息的字段
        print("*******************修改后的信息******start******************")
        pprint(data)
        print("*******************修改后的信息******end********************")
        flow.response.text = json.dumps(data)
