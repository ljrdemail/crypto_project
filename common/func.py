# -*- coding: utf-8 -*-
# __author__ = 'zhouqiang'


import logging
import sys
from .api_utils import Api as WrapperApi
from .log import log_config, LOG_LEVEL
import os
LOG_LEVEL = {'CRITICAL': 50, 'ERROR': 40, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10}


class Func:
    log = log_config(c_level=logging.WARNING, f_level=None)[0]
    log_msg_flag = False
    protocol = 'https'

    @classmethod
    def api(cls, *args, **kwargs):
        protocol = cls.protocol
        if kwargs.get('gateway_protocol'):
            protocol = kwargs.get('gateway_protocol')
            del kwargs['gateway_protocol']
        _api = WrapperApi(*args, log=cls.log, log_msg_flag=cls.log_msg_flag, protocol=protocol,verify=True, **kwargs)
        return _api

    @staticmethod
    def printErr(userInfo="", bPrint=True):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        msg = "异常类型：%s, 在 %s 的第 %d 行；%s"%(exc_type, fname, exc_tb.tb_lineno, exc_obj)
        if userInfo:
            msg = msg + "\n" + userInfo
        if bPrint:
            print(msg)
        return msg

