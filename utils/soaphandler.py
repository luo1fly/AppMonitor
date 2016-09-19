#!/usr/bin/env python
# Name: soaphandler.py
# Time:9/19/16 9:46 AM
# Author:luo1fly

from suds.wsse import Security, UsernameToken
from suds.client import Client
from suds import WebFault
from logging.config import fileConfig
import logging
from utils.mailhandler import MailHandler
# import custom modules above


class SoapHandler(object):
    """
    模拟soap对webservice的请求过程
    """
    def __init__(self, *args, **kwargs):
        """
        初始化请求客户端
        :param kwargs: api字典对象
        """
        fileConfig('conf/logger.conf')
        self.info_logger = logging.getLogger('infoLogger')
        self.error_logger = logging.getLogger('errorLogger')
        self.app_name = args[0]
        self.url = kwargs['url']
        try:
            self.client = Client(self.url)
        except Exception as e:
            # print('send mail')
            self.error_logger.error('%s: %s' % (self.app_name, e.args[0]))
            self.client = None
        self.user = kwargs['user']
        self.password = kwargs['password']
        self.ports = kwargs['ports']
        self.method = kwargs['method']
        self.requests = kwargs['requests']

    def pass_security_cert(self):
        """
        https接口需要安全验证
        :return: 通过返回true，没有连接信息或者验证失败返回false
        """
        if not self.client:
            return False
        else:
            security = Security()
            token = UsernameToken(self.user, self.password)
            security.tokens.append(token)
            try:
                self.client.set_options(wsse=security)
            except AttributeError as e:
                # print('need a log')
                self.error_logger.error('%s: %s' % (self.app_name, e.args[0]))
                MailHandler().send_mail(e.args[0], self.url)
                return False
            else:
                return True

    def request(self):
        """
        :return: 请求接口，将正常结果返回，异常记录日志并发送邮件给运维人员
        """
        try:
            result = self.client.service[self.ports][self.method](self.requests)
        except WebFault as e:
            # print('need a log')
            self.error_logger.error('%s: %s' % (self.app_name, e.args[0]))
            # print('send a mail')
            MailHandler().send_mail(e.args[0], self.url)
        else:
            self.info_logger.info('%s: %s' % (self.app_name, result))
            return result

    def close(self):
        del self
