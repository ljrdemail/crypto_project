# -*- coding: utf-8 -*-
# __author__ = 'lijiarui'
import pytest

from common.excel_utiles import Excel
from conftest import *
from service.api_utils import CommonApiUtils


class TestGetCandlestick:


    def test_get_candlestick(self,get_excel_path,get_uat_url):

        try:
            excel = Excel(get_excel_path)
            testdatalist = excel.get_page_data(page="candlestick")
            for i in testdatalist:
                res = CommonApiUtils.get_candlestick(get_uat_url, i[0], i[1])
                print(res)

        except Exception as e:

            return False

        finally:
            pass





if __name__ == '__main__':
    pytest.main(["-s"])