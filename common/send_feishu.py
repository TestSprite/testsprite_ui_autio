# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2023/1/18  18:02
# 文件名：send_dingtalk_message.py
# coding: utf-8

# 飞书群中的自定义机器人是通过webhook的形式将你要发送的消息即时发送到群聊中
# 在群聊中添加机器人
# 进入群聊，打开群设置，找到群机器人，并点击添加机器人。选择Custom Bot（自定义机器人）加入群聊。
# 第一步：添加该机器人进群，设置机器人头像、名称和描述，然后点击下一步。
# 第二步：配置webhook，可根据需求选择一种及以上安全设置的方式，也可不选，复制并保存此页面的参数，最后点击完成。
# 注意：一个群总共最多可添加 15 个机器人，可以只添加15个Custom Bot（自定义机器人）。
# 使用机器人发送消息
# 请保管好 webhook 地址。 不要公布在 Github、博客等可公开查阅的网站上。地址泄露后可能被恶意调用发送垃圾信息
# 最基本的发送消息
# -*- coding: utf-8 -*-
import requests
def push_report(web_hook,mobile_list):
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    message_body = {
        "msg_type": "text",
        "content": {
            "text": "<at user_id=\"all\">所有人</at>"
                    "消息推送展示项目：飞书\n" +
                    ">>环境：测试环境 \n" +
                    ">>类型：%s \n" % "消息推送" +
                    ">>测试结果：%s \n" % "通过"
        },
        "at": {
            # 要@的人
            "atMobiles": mobile_list,
            # 是否@所有人
            "isAtAll": False
        }

    }

    ChatRob = requests.post(url=web_hook, json=message_body, headers=header)
    opener = ChatRob.json()
    print("opener:{}".format(opener))
    if opener["StatusMessage"] == "success":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))


if __name__ == '__main__':
    # webhook 来自于 获取机器人webhook：复制webhook 中的那个值
    webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/bd248396-0f94-4995-9bdf-489992807d11"
    # 要@的人的手机号，可以是多个，注意：飞书机器人设置中需要添加这些人，否则不会接收到消息
    mobile_list = ['15213337472']
    push_report(webhook,mobile_list)
