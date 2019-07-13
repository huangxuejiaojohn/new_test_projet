import unittest
from try_ui.try_baidu import baidu_ui
import HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#加载测试用例
run_case = unittest.TestSuite()
run_case.addTest(unittest.makeSuite(baidu_ui.baidu_ui_case))
#测试用例报告
report_name = "baidureport.html"
fh = open(report_name,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fh,title="百度搜索设置测试报告:",description="百度搜索设置自动化测试报告：")
runner.run(run_case)


########################发送邮件########################################

smtp_service = "smtp.163.com"                    #邮箱服务器地址
emailusername = "huangxuejiaoczhong@163.com"
emailpassword = "huangxuejiao88"                 #设置客户端授权码的密码
sender = "huangxuejiaoczhong@163.com"            #发送者
receiver = ["huangxuejiaoczhong@163.com","2219201098@qq.com"]  #接收者
subject = "关于百度自动化工作事宜"                  #邮件的主题
email_body = "Hi,John!\nwelcome to baidu family!" #邮件内容
email_attachfile = report_name                    #发送邮件附件

########################################################################

msg = MIMEMultipart("mixed")
msg['Subject'] = subject
msg['From'] = "huangxuejiaoczhong@163.com<huangxuejiaoczhong@163.com>"
msg['To'] = ";".join(receiver)  #收件人为多个收件人，通过join将列表转换为以;为间隔的字符串


#构造文件内容
text_plain  = MIMEText(email_body,"plain","utf-8")
msg.attach(text_plain)


#构造文字的附件
sendfile = open(email_attachfile,'rb').read()
text_att = MIMEText(sendfile,"base64","utf-8")
text_att["Content-Type"] = "application/octet-stream"

# 附件可以重命名成aaa.txt，最好用原来文件名
# text_att["Content-Disposition"] = 'attachment; filename="smail.py"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename=email_attachfile)
msg.attach(text_att)


#发送邮件
smtp =smtplib.SMTP()
smtp.connect(smtp_service)
smtp.login(emailusername,emailpassword)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

