# -*- coding: utf-8 -*-
# __author__ = 'Lu Chunwen'
from pre.space_management_utils import get_layer_3_space
from service.ssec_service import SSecService
from service.viper_service import ViperService
from base.ssec_config import SSecKafka
from common.kafka_helper import KafkaHelper
from protoc.common.alarm_pb2 import *
import time


def alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason, run_time=30, **kwargs):
    """
    告警功能测试
    :param alarm_reason:  告警原因
    :param input_topic:  kafka topic
    :param config_id: 配置id
    :param host: 接口地址
    :param alarm_type: 告警类型
    :param log: log输出
    :param run_time: 运行时长
    :return:
    """
    # 测试前清理其他VPS任务以防干扰
    ViperService.delete_all_task(host)
    log.info("clear other vps task")
    log.info("start test")

    # 登录
    SSecService.login(host)
    # 创建任务
    parent_serial_number=get_layer_3_space(host)
    task_name, device_id, success = SSecService.create_alarm_task(host, alarm_type, config_id, log,parent_serial_number=parent_serial_number, **kwargs)
    if not success:
        return False

    # 检测kafka输出
    if not kafka_check(input_topic, alarm_reason, run_time, log):
        SSecService.delete_alarm_created(address=host, task_name=task_name, device_id=device_id)
        return False

    # 测试结束
    log.info("test finish")
    # 删除任务
    print(task_name)
    SSecService.delete_alarm_created(address=host, task_name=task_name, device_id=device_id)

    return True


def kafka_check(input_topic, alarm_reason, run_time, log):
    """
    检测kafka是否能消费vps和ksp告警信息
    :param alarm_reason:  告警原因验证
    :param log:
    :param input_topic:
    :param run_time:
    :return:
    """
    consume_success = False
    # 监听kafka是否成功告警
    kafka = KafkaHelper()
    consumer = kafka.consumer(topics=input_topic, host=SSecKafka.Broker, timeout=run_time * 1000)
    for msg in consumer:
        value = kafka.deserialize(msg)
        log.info(value)
        log.info("receive vps message")
        consume_success = True
        break
    if not consume_success:
        log.error("can not receive vps message")
        return False

    consume_success = False
    # 监听告警信息
    kafka = KafkaHelper()
    consumer = kafka.consumer(topics=SSecKafka.OutputTopic, host=SSecKafka.Broker, timeout=run_time * 1000)
    start = time.time()
    for msg in consumer:
        # 运行超时
        try:
            if time.time() - start >= run_time:
                log.error("can not receive alarm message")
                break
            value = kafka.deserialize(msg, AlarmEvent())
            log.info(value)
            log.info("receive alarm message")
            if len(alarm_reason) > 0 and value["reason"] in alarm_reason:
                consume_success = True
                break
        except Exception as e:
            print(e)
    if not consume_success:
        log.error("can not receive alarm message")
        return False
    return True
