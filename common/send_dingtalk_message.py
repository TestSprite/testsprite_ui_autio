# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2023/1/18  18:02
# 文件名：send_dingtalk_message.py
# coding: utf-8
import requests, json

# step1: 打开群设置 --> 打开智能群助手
# step2: 选择添加机器人，选择自定义机器人
# step3：给机器人命名，自定义关键字【这个必须要在发送消息里包含】，点击完成
# step4: 打开机器人获取dingtalk access_token 链接，用于发消息
# 发送钉钉消息
def send_dingtalk_message(url, content, mobile_list):
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            # 要发送的内容【支持markdown】【！注意：content内容要包含机器人自定义关键字，不然消息不会发送出去，这个案例中是test字段】
            "content": content
        },
        "at": {
            # 要@的人
            "atMobiles": mobile_list,
            # 是否@所有人
            "isAtAll": False
        }
    }
    r = requests.post(url,headers=headers,data=json.dumps(data))
    print(r.text)
    return r.text


if __name__ == "__main__":
    # 获取dingtalk token url
    access_token = 'https://oapi.dingtalk.com/robot/send?access_token=169b52506e4326a43d842918a481776722078fc49ff0b58926fc6da2452e2850'
    # 钉钉消息内容，注意{测试日报}是自定义的关键字，需要在钉钉机器人设置中添加，这样才能接收到消息
    content = F"通知\n----测试日报----\n新增缺陷项目名称：数据工厂\n今日新增缺陷数：4\n今日关闭缺陷数：2\n今日修复缺陷数：2\n待解决缺陷数：2\n总缺陷数：10\n"
    # 要@的人的手机号，可以是多个，注意：钉钉机器人设置中需要添加这些人，否则不会接收到消息
    mobile_list = ['15213337472']
    # 发送钉钉消息
    send_dingtalk_message(access_token, content, mobile_list)