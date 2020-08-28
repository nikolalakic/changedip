#! /usr/bin/python3

import requests
import smtplib
import gnupg
import os
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

ip = requests.get('https://api.ipify.org').text
ip = str(ip)
#You edit next line
old_ip = 'Enter your current IP here'
userpath = os.getcwd()
user = getpass.getuser()
gpg = gnupg.GPG(gnupghome=('/home/{}/.gnupg').format(user))
servers = ['disroot.org', 'gmail.com', 'posteo.net', 'yahoo.com', 'live.com']
cockliservers = ['cock.li','airmail.cc','420blaze.it','aaathats3as.com','cumallover.me','goat.si','horsefucker.org','national.shitposting','nigge.rs','tfwno.gf','cock.lu','cock.email','firemail.cc','hitler.rocks','getbackinthe.kitchen','memeware.net','cocaine.ninja','waifu.club','rape.lol','nuke.africa']

password = open('password.txt').read()
password = password.partition('\n')[0]
username = open('email.txt').read()
username = username.partition('\n')[0]
providername = username.split('@',1)[1]

if any(providername in i for i in servers):
    if providername == 'disroot.org':
        server = providername
    elif providername == 'gmail.com':
        server = 'smtp.gmail.com'
    elif providername == posteo.net:
        server = 'posteo.de'
    elif providername == 'startmail.com':
        server = 'smtp.startmail.com'
    elif providername == 'yahoo.com':
        server = 'smtp.mail.yahoo.com'
    elif providername == 'live.com':
        server = 'smtp.live.com'
    else:
        print('Provider not in the list of providers, contact maintainer of this project for adding provider you use to list.')
if any(providername in i for i in cockliservers):
    server = 'mail.cock.li'

if old_ip != ip:
    msg = MIMEMultipart()
    msg['From'] = username
    # You edit next two lines only
    RecipientID = 'example1@email.com' 
    Recipient = 'example1@email.com'
    msg['To'] = Recipient
    msg['Subject'] = 'Device IP address changed!!'
    mailbody = (f'New IP of device is: {ip} , this message will repeat itself in time depending of configured cronjob if you don't change old_ip variable!')
    secretmessage = (str(gpg.encrypt(mailbody, RecipientID, always_trust=True)))
    msg.attach(MIMEText(secretmessage, 'plain'))
    smtpObj = smtplib.SMTP(server, 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(username, password)
    try:
        smtpObj.sendmail(username, Recipient, msg.as_string())
        smtpObj.close()
    except Exception as e:
        print(e)
else:
    pass
exit()
