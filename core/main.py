#!/usr/bin/env python
# Name: main.py
# Time:9/19/16 9:45 AM
# Author:luo1fly


from utils.soaphandler import SoapHandler
# import custom modules above


def call(name, body):
    """
    :param name: 接口应用的名字
    :param body: 请求体
    :return:
    """
    name_lst = [name, ]
    sh = SoapHandler(*name_lst, **body)
    if sh.pass_security_cert():
        sh.request()
    sh.close()

