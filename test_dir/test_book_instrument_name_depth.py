import json
import unittest
from websocket import create_connection
import websocket
from common.excel_utiles import Excel
from conftest import *

def get_data():
    """
    读取参数化文件
    :param get_excel_path:
    :return:
    """
    excel = Excel(RunConfig.DATA_LOCATION)
    testdatalist = excel.get_page_data(page="instrument_depth")
    return testdatalist






def test_send_info(ws_connect_close):
        # 第一步：准备参数
        params = {
            "id": 11,
            "method": "subscribe",
            "params": {
                "channels": ["book.ETH_CRO.150"]
            },
            "nonce": 1587523073344
        }
        expected = {'code': 0}
        # 第二步：发送请求
        ws_connect_close.send(json.dumps(params))
        # 获取结果
        ws_connect_close.recv()
        result2 = ws_connect_close.recv()


        res2 = json.loads(result2)

        # 第三步：断言：

        print("接收结果2：", res2)
        assert expected['code']==res2['code']



if __name__ == '__main__':
    pytest.main(["-s"])

