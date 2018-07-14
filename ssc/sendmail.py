#!/usr/bin/env python3
# -*- coding: gb2312 -*-
import smtplib
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可
import time
import random


receiver='ewaimp@icloud.com'
config1 = dict(server='smtp.qq.com',sender = '877135818@qq.com',receiver = receiver,
              username = '877135818@qq.com',password ='fibpzqlinfvfbcgb')
config2 = dict(server='smtp.qq.com',sender = 'ewaimp@21cn.com',receiver = receiver,
              username = 'ewaimp@qq.com',password ='mxxbajinemqtbegd')
config3 = dict(server='smtp.126.com',sender = 'ewaimp@126.com',receiver = receiver,
              username = 'ewaimp@126.com',password ='Sg0211589')

config_dict =[]
config_dict.append(config1)
config_dict.append(config2)
config_dict.append(config3)
random.random

#随机选择一个发送邮箱
config = random.choice(config_dict)

#config = config_dict[1]

# 所使用的用来发送邮件的SMTP服务器
smtpServer=config['server']

# 发件人
sender = config['sender']

# 接收人
receiver = config['receiver']

# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username=config['username']
password=config['password']

# print(config_dict[2])
# exit(0)

# 创建一个实例
def sendMail(mail_title,mail_body):
    print('正在构建邮件参数信息....')
    message=MIMEText(mail_body,'plain','utf-8')  # 邮件正文
    message['From']=sender  # 邮件上显示的发件人
    message['To'] = receiver # 邮件上显示的收件人
    message['Subject']=Header(mail_title,'utf-8')  # 邮件主题
    print('邮件参数构建完成.')
    try:

        smtp=smtplib.SMTP()  # 创建一个连接
        print('正在连接'+config['server']+'....')
        time.sleep(random.randint(1,5))
        smtp.connect(smtpServer)  # 连接发送邮件的服务器
        print('连接完成，正在登陆....')
        smtp.login(username,password)  # 登录服务器
        time.sleep(random.randint(5,10))
        print('登录成功，准备发送邮件.')
        print('正在发送邮件....')
        smtp.sendmail(sender,receiver,message.as_string())  # 填入邮件的相关信息并发送
        print("邮件发送成功.")
        return True
        print('退出邮件.')
        smtp.quit()
    except smtplib.SMTPException as e:
        print("邮件发送失败.")
        print(e)
        return False

#sendMail('随机发送的邮件','随机内容'+config['server'])