# -*-coding:utf-8 -*-
from base.api_config import *
from common.base import Base
import time




class CommonApis(object):
    """

    """

    @staticmethod

    def get_cancle_stick(host, param):
        """
        get_cancle_stick
        :param host:
        :return:
        """
        time.sleep(1)
        api = Base.api(host, body=param, **SSecConst.GET_CANDLE_STICK)
        return api.get_response()

