#!/usr/bin/env python
# Name: mailhandler.py
# Time:9/19/16 11:45 AM
# Author:luo1fly

import smtplib
from email.mime.text import MIMEText
from logging.config import fileConfig
import logging
# import custom modules above


class MailHandler(object):
    def __init__(self, **cfg):
        self.cfg = cfg
        fileConfig('conf/logger.conf')
        self.info_logger = logging.getLogger('infoLogger')
        self.error_logger = logging.getLogger('errorLogger')
        if not self.cfg:
            self.mailto_list = ["", ]
            self.mail_host = ""
            self.mail_user = ""
            self.mail_pass = ""
            self.mail_postfix = ""
        else:
            self.mailto_list = self.cfg['mailto_list']
            self.mail_host = self.cfg['mail_host']
            self.mail_user = self.cfg['mail_user']
            self.mail_pass = self.cfg['mail_pass']
            self.mail_postfix = self.cfg['mail_postfix']

    def send_mail(self, sub, content):
        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEText(content, _charset="utf-8")
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(self.mailto_list)

        send_smtp = smtplib.SMTP()
        send_smtp.connect(self.mail_host)

        try:
            send_smtp.login(self.mail_user, self.mail_pass)
        except smtplib.SMTPAuthenticationError as se:
            self.error_logger.error('%s' % se)
            return False
        else:
            send_smtp.sendmail(me, self.mailto_list, msg.as_string())
            self.info_logger.info('mail send successfully!')
            send_smtp.close()
            return True
