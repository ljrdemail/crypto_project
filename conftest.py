import os
import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"


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



