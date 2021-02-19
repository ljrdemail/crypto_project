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


def get_item_by_key(obj, key, result=None):
    if isinstance(obj, dict):
        for k in obj:
            if key == k:
                if isinstance(result, list):
                    if isinstance(obj[k], list):
                        result.extend(obj[k])
                    else:
                        result.append(obj[k])
                elif result is None:
                    result = obj[k]
                else:
                    result = list((result,))
                    result.append(obj[k])
            else:
                if isinstance(obj[k], dict) or isinstance(obj[k], list):
                    result = get_item_by_key(obj[k], key, result)
    elif isinstance(obj, list):
        for i in obj:
            if isinstance(i, dict) or isinstance(i, list):
                result = get_item_by_key(i, key, result)
    return result[0] if isinstance(result, list) and len(result) == 1 else result


def replace_inspect_getargspec(func):
    """
        解决cython中inspect判断编译so后method失败的问题(不修改源码，脚本中替换原函数)
    :param func:
    :return:
    """
    from inspect import getargs, ArgSpec
    args, varargs, varkw = getargs(func.func_code)
    return ArgSpec(args, varargs, varkw, func.func_defaults)


# inspect.getargspec = replace_inspect_getargspec


def flow(func):
    setattr(func, "__entry__", func.__name__)
    setattr(func, "__description__", (getattr(func, "__doc__", "") or "用例函数没有填写注释!").replace("\n", "#"))
    func_input_args = inspect.getfullargspec(func)
    arg_name_list = list(func_input_args.args)
    default_value_list = \
        [None] * (len(func_input_args.args or tuple()) - len(func_input_args.defaults or tuple())) \
        + list(func_input_args.defaults or tuple())
    setattr(func, "__input_config__", [
        {
            "key": k,
            "type": "text",
            "require": not v,
            "default": v or "",
            "description": "",
            "options": []
        } for k, v in zip(arg_name_list, default_value_list) if "log" != k])

    @functools.wraps(func)
    def wrap(config, log):
        if not isinstance(config, dict):
            try:
                config = json.loads(config)
            except:
                config = eval(config)
            log = log_config(filename=log, fix=True)[0]
        s_t = time.time()
        log.critical('脚本开始时间：%s' % str(round(time.time() - s_t, 2)) + 's')
        Func.log = log
        Func.log_msg_flag = False
        config['log'] = log
        if 'log_level' in config:
            if config['log_level'].upper() in LOG_LEVEL:
                log.level = LOG_LEVEL[config['log_level'].upper()]
        if 'protocol' in config:
            Func.protocol = config['protocol']
        params = {}
        for key in inspect.getfullargspec(func).args:
            if key in config:
                params[key] = config[key]
        try:
            r = func(**params)
            if isinstance(r, list):
                response = []
                for elem in r:
                    if elem[1]:
                        response.append({"title": func.__doc__ + elem[0],
                                         "result": "Pass",
                                         "detail": '\n'.join(elem[2:]),
                                         "exec_time": str(round(time.time() - s_t, 2)) + 's'})
                    else:
                        response.append({"title": func.__doc__ + elem[0],
                                         "result": "Fail",
                                         "detail": '\n'.join(elem[2:]),
                                         "exec_time": str(round(time.time() - s_t, 2)) + 's'})
                return response
            else:
                result_dict = {"name": func.__name__, "title": func.__doc__, "result": "Fail",
                               "exec_time": str(round(time.time() - s_t, 2)) + 's'}
                log.critical('脚本耗时：%s' % str(round(time.time() - s_t, 2)) + 's')
                if r is True:
                    result_dict["result"] = "Pass"
                elif not type(r) is bool:
                    result_dict["reason"] = str(r)

                return [result_dict]
        except:
            e = str(traceback.format_exc())
            log.error(e)
            log.critical('脚本耗时：%s' % str(round(time.time() - s_t, 2)) + 's')
            return [{"title": func.__doc__, "result": "Fail", "reason": e,
                     "exec_time": str(round(time.time() - s_t, 2)) + 's'}]

    return wrap


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
        _api = WrapperApi(*args, log=cls.log, log_msg_flag=cls.log_msg_flag, protocol=protocol, **kwargs)
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
