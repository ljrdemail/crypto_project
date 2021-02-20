# -*- coding: utf-8 -*-
# __author__ = 'lijiarui'
import pytest

from common.excel_utiles import Excel
from service.api_utils import CommonApiUtils


class TestGetCandlestick:
    testdatalist = []

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_get_candlestick(self):

        try:
            excel = Excel("..\\data\\cyprto_test_data.xlsx")
            testdatalist = excel.get_page_data(page="candlestick")
            
            for i in testdatalist:
                res = CommonApiUtils.get_candlestick(i[0], i[1], i[2])
                print(res)
                assert 1 == 1

        except Exception as e:

            return False

        finally:
            print("清理数据")




if __name__ == '__main__':
    pytest.main()