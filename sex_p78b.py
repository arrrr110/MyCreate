import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):

    from_addr = 'aorui123@163.com'
    password = '1987366666'
    smtp_server = 'smtp.163.com'

    msg = MIMEText(body)
    #msg = MIMEText('The body of the email is here', 'plain', 'utf-8')

    msg['Subject'] = 'An Email Alert'
    msg['From'] = 'aorui123@163.com'
    msg['To'] = '454473269@qq.com'

    s = smtplib.SMTP(smtp_server, 25)
    s.login(from_addr, password)
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen('https://isitchristmas.com/'),'html.parser')
while(bsObj.find('a', {'id':'answer'}).attrs['title'] == 'NO'):
    print('It is not Christmas yey.')
    time.sleep(3600)
bsObj = BeautifulSoup(urlopen('https://isitchristmas.com/'),'html.parser')
sendMail('It is Chrisymas!', 'According to https://isitchristmas.com, it is Christmas!')






