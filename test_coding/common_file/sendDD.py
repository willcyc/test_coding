# coding:utf-8
import json
import requests


def new_req(url, text, title,):
    data = {'msgtype': 'markdown',
            'markdown': {
                'text': text,
                'title': title,
                # 'messageUrl': messageurl
            }}
    data = json.dumps(data).encode(encoding='UTF8')
    print(data)
    head = {"Content-Type": "application/json"}
    response = requests.post(url, data=data, headers=head).json
    print(response)


# 钉钉机器人链接
# url = "https://oapi.dingtalk.com/robot/send?access_token=4c3fe1a2d54d0c51c8d6867c6104cc0e095113f48667e15012b8545043942b49"
# waring_text = "### 请查看接口测试报告"
# new_req(url, waring_text, "接口预警")
