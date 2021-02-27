# -*- coding: utf-8 -*-
# __author__ = 'zhouqiang'

import functools
import logging
import inspect
import traceback
import json
import time
from .api import Api as WrapperApi
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
        _api = WrapperApi(*args, log=cls.log, log_msg_flag=cls.log_msg_flag, protocol=protocol,verify=False, **kwargs)
        return _api

class LogUtil:
    RESULT_DIR = 'result'
    LOG_DIR = 'log'

    @staticmethod
    def get_base_dir_realpath():
        """
        获得当前py文件所在目录的目录
        :return:
        """
        current_dir = os.path.dirname(os.path.realpath(__file__))
        base_dir = "{}/..".format(current_dir)  # 上级目录
        path = os.path.realpath(base_dir)
        return path

    @staticmethod
    def get_log_path():
        """
        获得日志文件夹的路径
        :return:
        """
        return os.path.join(LogUtil.get_gateway_path(), LogUtil.RESULT_DIR, LogUtil.LOG_DIR)

    @staticmethod
    def get_gateway_path():
        """
        获得gateway路径
        :return:
        """
        return os.path.join(LogUtil.get_base_dir_realpath())
