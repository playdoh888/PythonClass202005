"""
The SMTP AUTH protocol is used for client SMTP email submission
via TCP Port 587 and is DISABLED by default in Office 365 now.

https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission

"""
import smtplib
from email.message import EmailMessage

user = "your Office 365 user ID"
password = 'XXXXXXXX'
smtpsrv = "smtp.office365.com"
smtpserver = smtplib.SMTP(smtpsrv,587)

msg = EmailMessage()

msg['Subject'] = 'Email Testing with Python'
msg['From'] = 'jack.wang@periship.com'
msg['To'] = 'jack.wang888@gmail.com'

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(user, password)
smtpserver.send_message (msg)
smtpserver.close()
