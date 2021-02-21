import os
import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig
from websocket import create_connection
import websocket
# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + os.sep+"test_report"+os.sep


# 定义基本测试环境
@pytest.fixture(autouse=True)
def get_uat_url():
    return RunConfig.uat_url

@pytest.fixture(autouse=True)
def get_prd_url():
    return RunConfig.prd_url

@pytest.fixture(autouse=True)
def get_excel_path():
    return RunConfig.DATA_LOCATION

@pytest.fixture(autouse=True)
def get_ws_url():
    return RunConfig.WS_URL

@pytest.fixture(scope="function")
def ws_connect_close(get_ws_url):
    print("setup() begin")
    websocket.enableTrace(True)  # 打开跟踪，查看日志
    ws = create_connection(get_ws_url)  # 创建连接
    ws.settimeout(10)  # 设置超时时间
    print("setup() end")
    yield ws

    print("teardown() begin")
    ws.close()
    print("teardown() end")


