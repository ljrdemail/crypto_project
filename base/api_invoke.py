# -*-coding:utf-8 -*-
from base.api_config import *
from common.func import Func





class CommonApis(object):
    """
    设备管理API
    """

    @staticmethod
    # @verify_login
    def get_cancle_stick(host, param):
        """
        获取设备列表
        :param body:
        :param host:
        :param header:
        :return:
        """
        api = Func.api(host, body=param, **SSecConst.GET_CANDLE_STICK)
        return api.get_response()

