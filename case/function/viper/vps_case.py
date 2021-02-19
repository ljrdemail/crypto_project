# -*- coding:utf-8 -*-
from common.kafka_helper import KafkaHelper
from base.ssec_config import *
from common.func import flow
from common.log import *

kafka = KafkaHelper()
data = {"host": SSecKafka.Broker, "run_time": 10}


def debug(func):
    def wrapper(host, run_time, log):
        try:
            return func(host, run_time, log)
        except Exception as msg:
            print("Timed out!")

    return wrapper


@flow
def vps_head_shoulder(host, run_time, log):
    """
     vps 头肩检测
    :param host: api ip地址
    :param run_time: 运行时长(s)
    :param log:  日志输出
    :return:
    """
    start = time.time()
    consumer = kafka.consumer(topics=SSecKafka.HeadShoulderTopic, host=host)
    for msg in consumer:
        # 超时退出
        if time.time() - start > run_time:
            break
        value = kafka.deserialize(msg)
        log.info(value)


@flow
def output_alarm(host, run_time, log):
    """
    ksp告警结果
    :param host: api ip地址
    :param run_time: 运行时长(s)
    :param log:  日志输出
    :return:
    """
    try:
        start = time.time()
        consumer = kafka.consumer(topics=SSecKafka.OutputTopic, host=host)
        for msg in consumer:
            # 超时退出
            if time.time() - start > run_time:
                break
            value = kafka.deserialize(msg, kafka.get_data_type(SSecKafka.AlarmInfo))
            log.info(value)
        return True
    except Exception as ex:
        log.error(f"\n{str(ex)}\n")
        return False


if __name__ == "__main__":
    lg = get_current_log()
    lg.info(vps_head_shoulder(data, lg))
