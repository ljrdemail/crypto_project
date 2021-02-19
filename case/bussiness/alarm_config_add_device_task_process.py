# -*- coding: utf-8 -*-
# __author__ = 'lijiarui'
from common.func import *
from common.log import log_config
from service.api_utils import CommonApiUtils


@flow
def alarm_config_add_device_task_process(host,instrument_name="ETH_CRO",timeframe="5m",log=None):
    """
    [metro-web]<1.0.0>创建告警配置（enable/disable）-添加设备-创建任务成功
    :param modify_alarm_type:
    :param alarm_type:
    :param host:
    :param log:
    :return:
    """
    uuid_str = ""
    _id = ""
    task_name = ""
    try:

        res=CommonApiUtils.get_candlestick(host,instrument_name,timeframe)
        print(res)
        return True

    except Exception as e:
        log.error(e)
        log.error('traceback.print_exc():', str(traceback.print_exc()))
        return False

    finally:
        log.info("清理数据")




if __name__ == "__main__":
    HOST = {"host": "api.crypto.com"}
    # db_name="ljr_test_1989"
    log = log_config(c_level=logging.INFO, f_level=logging.INFO, out_path=LogUtil.get_log_path(), filename='log')[0]
    param = {"alarm_type": "EVENT_TRAFFIC"}
    HOST.update(param)
    log.info(alarm_config_add_device_task_process(HOST, log))
