#!/usr/local/bin/python2.6

import smtplib
import email
import sys
from email.mime.text import MIMEText
from base64 import b64encode

username = ""
passwd = ""

def mail(to, subject, text):
   msg = MIMEText(text)

   msg['From'] = username
   msg['To'] = to
   msg['Subject'] = subject
  
   server = smtplib.SMTP("smtp.gmail.com", 587)
   server.set_debuglevel(1)
   server.ehlo()
   server.starttls()
   server.ehlo()


   try:
       server.login(username, passwd)
   except smtplib.SMTPHeloError as err:
       print("SMTPHeloError Unexpected error: %s" % err)
   except smtplib.SMTPAuthenticationError as err:
       print("SMTPAuthenticationError Unexpected error: %s" % err)
   except smtplib.SMTPException as err:
       print("SMTPException Unexpected error: %s" % err)
   except Exception as err:
    # if login fails, try again using a manual plain login method
       print("Unexpected error: %s" % err)

   server.sendmail(username, to, msg.as_string())
   server.close()
   return 'ok'

def main():
    mail("xxxx@hotmail.com", "hi", "hi", )

if __name__ == "__main__":
    main()
