# -*- coding: utf-8 -*-
# __author__ = 'lijiarui'
import pytest

from common.excel_utiles import Excel
from conftest import *
from service.api_utils import CommonApiUtils


def get_data():
    """
    读取参数化文件
    :param get_excel_path:
    :return:
    """
    excel = Excel(RunConfig.DATA_LOCATION)
    testdatalist = excel.get_page_data(page="candlestick")
    return testdatalist


@pytest.mark.parametrize("address,instrument_name,timeframe,errorcode",
                         get_data()
                         )
def test_get_candlestick(address, instrument_name, timeframe, errorcode):
    res = CommonApiUtils.get_candlestick(address, instrument_name, timeframe)
    if res  and res["code"] == int(0):
        assert res["code"] == int(errorcode)
        assert res["result"]["instrument_name"] == instrument_name
        assert res["result"]["interval"] == timeframe
    else:
        assert res["code"] == int(errorcode)


if __name__ == '__main__':
    pytest.main(["-s"])
