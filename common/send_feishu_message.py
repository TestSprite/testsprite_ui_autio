# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2023/1/18  18:02
# 文件名：send_dingtalk_message.py
# coding: utf-8

import requests
import json

def feishu_sendmessage(text):
    webhook = 'https://open.feishu.cn/open-apis/bot/v2/hook/bd248396-0f94-4995-9bdf-489992807d11'
    headers = {
    'Content-Type': 'application/json'
    }
    data = {
        "msg_type": "text",
        "content": {
            "text": "<at user_id=\"all\">所有人</at>%s"%text
        }
    }
    post_data = json.dumps(data)
    res = requests.post(url=webhook, data=post_data, headers=headers)

# if __name__ == '__main__':
#     text = ">>环境：测试环境 \n" + ">>类型：%s \n" % "测试报告" + \
#            ">>测试结果：\n"+\
#            "总计执行用例%s \n" % (1 + 1) + \
#            "用例通过数量：%s \n" % (1) + \
#            "用例失败数量：%s \n" % (1)
#     feishu_sendmessage(text)