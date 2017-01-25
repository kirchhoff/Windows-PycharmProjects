#coding=utf-8
import socket
socket.setdefaulttimeout(10.0)
import urllib

import time
import smtplib
from email.mime.text import MIMEText
import os
from contextlib import closing
mailto_list=["twd123@qq.com"]
# 发送邮件函数
def send_mail(to_list, sub, context):
    '''''
to_list: 发送给谁
sub: 主题
context: 内容
send_mail("xxx@126.com","sub","context")
    '''
    # 定义发送列表

    # 设置服务器名称、用户名、密码以及邮件后缀
    mail_host = "smtp.163.com"
    mail_user = "wdkirchhoff"
    mail_pass = "twd306579198"
    mail_postfix="163.com"

    me = mail_user + "<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(context)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        send_smtp = smtplib.SMTP()
        send_smtp.connect(mail_host)
        send_smtp.login(mail_user, mail_pass)
        send_smtp.sendmail(me, to_list, msg.as_string())
        send_smtp.close()
        return True
    except Exception, e:
        print(str(e))
        return False


def checkhtml(str):
    if "拟录取名单" in str:
    #if "开展2016年" in str:
        return True
    return False

url = "http://grawww.nju.edu.cn/" #网页地址



while True:
    t = time.time()
    try:
        with closing(urllib.urlopen(url)) as page:
            content = page.read()
            if checkhtml(content) == False:

                print time.time()-t,",",time.asctime(time.localtime(time.time())).split(" ")[-2]

                time.sleep(10)
            else:
                break
    except IOError,e:
        print "timeout"


print '''

#######################################################

                    出新信息了!!!

#######################################################

'''
if (True == send_mail(mailto_list,"wang有更新!","研究生院网有更新!")):
    print ("发送成功")


#
# fp.write(content) #写入数据
#
# fp.close() #关闭文件
