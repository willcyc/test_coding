import os
import glob
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def search_all_files_return_by_time_reversed(path, reverse=True):
    return sorted(glob.glob(os.path.join(path, '*')), key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=reverse)


def Send_Mail(title, path):
    # 第三方 SMTP 服务
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    mail_user = "zhaobaode@mysteel.com"  # 用户名
    mail_pass = "Asd@2016"  # 口令

    sender = 'zhaobaode@mysteel.com'
    # receivers = ['zhaobaode@mysteel.com', 'shizb@mysteel.com', 'chengyc@mysteel.com', 'baolinzhong@mysteel.com','renchangjiang@mysteel.com','longp@mysteel.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = ['chengyc@mysteel.com']

    f1 = search_all_files_return_by_time_reversed(path)
    print(f1[0])
    # 处理异常报告
    with open(f1[0], encoding='UTF-8') as f:
        res = f.read()
        if r'status": "失败"' in res:
            res = r'异常'
        else:
            res = r'正常'
        f.close()
    msg = MIMEMultipart('mixed')
    msg['Subject'] = f'【{res}】'+title
    msg['From'] = Header("测试服务器", 'utf-8')
    msg['To'] = Header("相关负责人", 'utf-8')
    text_html = MIMEText(u"具体内容,请查看附件！", _subtype='html', _charset='utf-8')
    msg.attach(text_html)
    # 添加附件
    sendfile = open(f1[0], 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="ui_report.html"'
    msg.attach(att)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        print(title+"邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
