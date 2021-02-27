# -*-coding:utf-8 -*-
from base.api_config import *
from common.func import Func
import time




class CommonApis(object):
    """
    设备管理API
    """

    @staticmethod

    def get_cancle_stick(host, param):
        """
        get_cancle_stick
        :param host:
        :return:
        """
        time.sleep(1)
        api = Func.api(host, body=param, **SSecConst.GET_CANDLE_STICK)
        return api.get_response()

