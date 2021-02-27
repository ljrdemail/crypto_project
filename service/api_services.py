# -*-coding:utf-8 -*-

from base.api_invoke import *

from base.api_config import SSecConst



class CommonApiUtils(object):
    """
    设备管理接口
    """

    @staticmethod
    def get_candlestick(address, instrument_name=1, timeframe=100):
        """
        Retrieves candlesticks over a given period for an instrument

        :param param:
        :param address:
        :param instrument_name: instrument_name
        :param timeframe:period
        :return: list
        """
        query_param={"instrument_name":instrument_name,"timeframe":timeframe}
        res = CommonApis.get_cancle_stick(address, param=query_param)
        return res

