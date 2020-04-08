#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/18 15:59
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header


class base_email:
    def __init__(self):
        # 用于邮件传输的。
        self.smtpserver = 'smtpw.263xmail.com'
        self.username = 'youfayang@dixintong.com'
        self.password = 'xxxxx'
        self.sender = 'XXX@163.com'
        self.receiver = ['2655872941@qq.com', '1798986784@qq.com']
        subject = '自动化测试报告'
        self.subject = Header(subject, 'utf-8').encode()

    def set_mail(self):
        self.msg = MIMEMultipart('mixed')
        self.msg['Subject'] = self.subject
        self.msg['From'] = ";".join(self.receiver)
        # self.msg['To'] = ";".join(self.receiver)
        # self.msg['Date']='2012-3-16'

    # 构造文字内容
    def set_plain(self, text):
        text_plain = MIMEText(text, 'plain', 'utf-8')
        self.msg.attach(text_plain)

    # 构造图片链接
    def set_image(self, imagefile):
        sendimagefile = open(imagefile, 'rb').read()
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image["Content-Disposition"] = 'attachment; filename="testimage.png"'
        self.msg.attach(image)

    # 构造html
    def set_html(self, htmlfile):
        ss = open(htmlfile, 'rb').read()
        html = """{}""".format(ss.decode('utf-8'))
        text_html = MIMEText(html, 'html', 'utf-8')
        text_html["Content-Disposition"] = 'attachment; filename="testResult.html"'
        self.msg.attach(text_html)

    # 构造附件
    def set_fujian(self, filep):
        sendfile = open(filep, 'rb').read()
        text_att = MIMEText(sendfile, 'base64', 'utf-8')
        text_att["Content-Type"] = 'application/octet-stream'
        text_att.add_header('Content-Disposition', 'attachment', filename='testlog.log')
        self.msg.attach(text_att)

    def run_mail(self, fp=None, filep=None):
        self.set_mail()
        test = "这是一个测试报告！"
        self.set_plain(test)
        self.set_html(fp)
        self.set_fujian(filep)
        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
        smtp.quit()


if __name__ == '__main__':
    base_email().run_mail()
