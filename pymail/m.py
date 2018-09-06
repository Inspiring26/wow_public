import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import traceback

def create_email(email_from, email_to, email_Subject, email_text, annex_path, annex_name):
    # 输入发件人昵称、收件人昵称、主题，正文，附件地址,附件名称生成一封邮件
    #生成一个空的带附件的邮件实例
    message = MIMEMultipart()
    #将正文以text的形式插入邮件中
    message.attach(MIMEText(email_text, 'plain', 'utf-8'))
    #生成发件人名称（这个跟发送的邮件没有关系）
    message['From'] = Header(email_from, 'utf-8')
    #生成收件人名称（这个跟接收的邮件也没有关系）
    message['To'] = Header(email_to, 'utf-8')
    #生成邮件主题
    message['Subject'] = Header(email_Subject, 'utf-8')
    #读取附件的内容
    att1 = MIMEText(open(annex_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    #生成附件的名称
    att1["Content-Disposition"] = 'attachment; filename=' + annex_name
    #将附件内容插入邮件中
    message.attach(att1)
    #返回邮件
    return message

def send_email(sender, password, receiver, msg):
    # 一个输入邮箱、密码、收件人、邮件内容发送邮件的函数
    try:
        #找到你的发送邮箱的服务器地址，已加密的形式发送
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器 465端口
        server.ehlo()
        #登录你的账号
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        #发送邮件
        server.sendmail(sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号（是一个列表）、邮件内容
        print("邮件发送成功")
        server.quit()  # 关闭连接
    except Exception:
        print(traceback.print_exc())
        print("邮件发送失败")

def main():
    print(datetime.datetime.now())
  
    my_email_from = 'huang'
    my_email_to = 'you'
    # 邮件标题
    my_email_Subject = 'user' 
    # 邮件正文
    my_email_text = "good good study, day day up!"
    #附件地址
    # my_annex_path = '/Users/huangyong/Downloads/2.png' #绝对路径可用
    my_annex_path = './2.png'
    #附件名称
    my_annex_name = "jiajia.png"
    # 生成邮件
    my_msg = create_email(my_email_from, my_email_to, my_email_Subject,
                          my_email_text, my_annex_path, my_annex_name)
    my_sender = '1002990258@qq.com'
    my_password = 'steokubigcvkbefe'
    my_receiver = '530870945@qq.com' 
    # 发送邮件
    send_email(my_sender, my_password, my_receiver, my_msg)
    print(datetime.datetime.now())

if __name__ == "__main__":
    main();


