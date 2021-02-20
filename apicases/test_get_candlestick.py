# -*- coding: utf-8 -*-
# __author__ = 'lijiarui'
import pytest

from common.func import *
from common.log import log_config
from service.api_utils import CommonApiUtils


@pytest.mark.parametrize(
    "host, instrument_name, timeframe",
    [("uat-api.3ona.co", "ETH_CRO", "5m")]

)
def test_get_candlestick(host,instrument_name,timeframe,log=None):
    
    try:

        res=CommonApiUtils.get_candlestick(host,instrument_name,timeframe)
        print(res)
        assert 1==1

    except Exception as e:
        log.error(e)
        log.error('traceback.print_exc():', str(traceback.print_exc()))
        return False

    finally:
        log.info("清理数据")




if __name__ == '__main__':
    pytest.main()