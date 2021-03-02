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
@pytest.fixture()
def ws_connect_close(get_ws_url):
    websocket.enableTrace(True)  # 打开跟踪，查看日志
    ws = create_connection(get_ws_url)  # 创建连接
    ws.settimeout(10)  # 设置超时时间
    yield ws
    ws.close()

@pytest.fixture()
def ws_connect_close_long(get_ws_url):
    websocket.enableTrace(True)  # 打开跟踪，查看日志
    ws = websocket.WebSocketApp(get_ws_url)  # 创建连接
    ws.settimeout(10)  # 设置超时时间
    yield ws
    ws.close()

@pytest.fixture()
def get_ws_url():
   return RunConfig.WS_URL


