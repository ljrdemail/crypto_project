import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(PRO_PATH, "test_dir", "test_get_candlestick.py")


    # 配置运行的 URL
    uat_url = "uat-api.3ona.co"
    prd_url="api.crypto.com"

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 报告路径（不需要修改）
    NEW_REPORT = None

    #测试数据路径
    DATA_LOCATION=os.path.join(PRO_PATH, "data", "cyprto_test_data.xls")
