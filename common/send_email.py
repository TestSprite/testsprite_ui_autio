# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2023/1/18  15:43
# 文件名：send_email.py
import smtplib
#用邮箱实现带附件邮件发送
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from tkinter import filedialog

from uoffer_webui.email.send_file import get_files
from uoffer_webui.email.zipfile_test import do_zip_compress


class AttachmentEmailSender(object):

    def __init__(self):
        self.smtp_host = "smtp.163.com"    #发送邮件的smtp服务器(从QQ邮箱中取得)
        self.smtp_user = "15213337472@163.com"   #用于登录smtp服务器的用户名，也就是发送者的邮箱
        self.smtp_pwd = "XNQVGSUDBNKXAJWB"    #授权码，和用户名user一起，用于登录smtp，非邮箱密码，可以使用Foxmail生成
        self.smtp_port = 465        #smtp服务器SSL端口号，默认是465
        self.sender = "15213337472@163.com"

    def sendeamil(self,tolist,subject,body,lasteamil_path):
        """
        发送邮件
        :param tolist:收件人的邮箱列表
        :param subject: 邮件标题
        :param body: 邮件内容
        :param lasteamil_path: 邮件附件所在路径
        :return:
        """
        #创建一个带附件的实例
        message = MIMEMultipart()
        message['Form'] = Header(self.sender,'utf-8')               #发件人
        message['To'] = Header(",".join(tolist),'utf-8')            #收件人列表
        message['Subject'] = Header(subject,'utf-8')                #邮件标题

        #邮件正文内容
        message.attach(MIMEText(body,'html','utf-8') )   #邮件内容，格式，编码

        #获取最新的email路径，如果存在说明有报错，构造附件，发送email路径下的excel文件
        att1 = MIMEApplication(open(lasteamil_path,'rb').read())
        att1['Content-Type'] = 'application/octet-stream'
        #这里的filename可以任意写，写什么邮件就显示什么名字
        att1.add_header('Content-Disposition','attachment', filename="测试报告.zip")
        message.attach(att1)
        # ---附件部分---
        # lasteamil_path=filedialog.askdirectory()
        # files = get_files(lasteamil_path)
        # for each in files:
        #     part = MIMEApplication(open(each, 'rb').read())
        #     part.add_header('Content-Disposition', 'attachment', filename=each.split('\\')[-1])
        #     message.attach(part)

        try:
            smtpSSLClient = smtplib.SMTP_SSL(self.smtp_host,self.smtp_port)   #实例化一个SMTP_SSL对象
            loginRes = smtpSSLClient.login(self.smtp_user,self.smtp_pwd)    #登录smtp服务器
            print("登录结果：loginRes=",loginRes)
            if loginRes and loginRes[0] == 235:
                print("登陆成功，code = ",loginRes[0])
                smtpSSLClient.sendmail(self.sender,tolist,message.as_string())
                print(f"mail has been send successful. message:{message.as_string()}")
            else:
                print("登录失败，code=",loginRes[0])
        except Exception as e:
            print("邮件发送失败，Exception：e=",e)
if __name__ == "__main__":
    emailSenderClient=AttachmentEmailSender()
    file_path = 'D:\重庆工程学院\教学课件\课件\\4.自动化测试\\UI和接口自动化\\WebUI\\uoffer\html'
    do_zip_compress(file_path)
    lasteamil_path ='D:\重庆工程学院\教学课件\课件\\4.自动化测试\\UI和接口自动化\\WebUI\\uoffer\html.zip'
    content = '测试报告如附件所示'
    tolist = "liwanlunzq@163.com"  # 收件人邮箱
    local = time.localtime()
    time1 = time.strftime("%Y-%m-%d %H:%M:%S",local)
    subject = '测试报告通知' + time1
    emailSenderClient.sendeamil(tolist, subject, content,lasteamil_path)