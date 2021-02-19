# -*- coding: utf-8 -*-
# __author__ = 'Lu Chunwen'
from case.function.alarm.base_case import *
from common.func import flow
from common.log import get_current_log
from pre.alarm_config_utils import get_exist_alarm_config


@flow
def event_pedestrian_hover(host, log):
    """
    [metro-web]<1.0.0> EVENT_PEDESTRIAN_HOVER(徘徊)告警测试
    """
    alarm_type = "EVENT_PEDESTRIAN_HOVER"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "ksp-input-pach-event"
    alarm_reason = ["hover"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def surveillance(host, log):
    """
    [metro-web]<1.0.0> SURVEILLANCE(布控)告警测试
    """
    alarm_type = "SURVEILLANCE"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "ksp-input-face"
    alarm_reason = ["白名单", "公安失信", "不良失信"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_pedestrian_clothes(host, log):
    """
    [metro-web]<1.0.0> EVENT_PEDESTRIAN_CLOTHES(服装异常)告警测试
    """
    alarm_type = "EVENT_PEDESTRIAN_CLOTHES"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "ksp-input-faceped"
    alarm_reason = ["abnormal clothes"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_traffic(host, log):
    """
    [metro-web]<1.0.0> EVENT_TRAFFIC(人流异常)告警测试
    """
    alarm_type = "EVENT_TRAFFIC"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.crowd.cross.line"
    other = {"direction": "0,1", "polygons": "0,500;1920,500"}
    alarm_reason = ["traffic"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason, **other)
    return res


@flow
def event_pedestrian_stay(host, log):
    """
    [metro-web]<1.0.0> EVENT_PEDESTRIAN_STAY(滞留)告警测试
    """
    alarm_type = "EVENT_PEDESTRIAN_STAY"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.crowd.cross.line"
    alarm_reason = ["retention"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_hurdle_delivery(host, log):
    """
    [metro-web]<1.0.0> EVENT_HURDLE_DELIVERY(隔栏递物)告警测试
    """
    alarm_type = "EVENT_HURDLE_DELIVERY"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.algo"
    other = {"polygons": "0.500,0.000;0.500,0.000;0.500,1.000;0.500,1.000;0.500,0.000"}
    alarm_reason = ["hurdle delivery"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, run_time=300, alarm_reason=alarm_reason,
                              **other)
    return res


@flow
def event_object_stay(host, log):
    """
    [metro-web]<1.0.0> EVENT_OBJECT_STAY(背包滞留)告警测试
    """
    alarm_type = "EVENT_OBJECT_STAY"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.algo"
    alarm_reason = ["object stay"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_crowd(host, log):
    """
    [metro-web]<1.0.0> EVENT_CROWD(人群密度)告警测试
    """
    alarm_type = "EVENT_CROWD"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.crowd.cross.line"
    alarm_reason = ["over crowding"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_human_distract(host, log):
    """
    [metro-web]<1.0.0> EVENT_HUMAN_DISTRACT(分心)告警测试
    """
    alarm_type = "EVENT_HUMAN_DISTRACT"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.algo"
    alarm_reason = ["不通"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_carry_bag_security(host, log):
    """
    [metro-web]<1.0.0> EVENT_CARRY_BAG(带包安检)告警测试
    """
    alarm_type = "EVENT_CARRY_BAG"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "ksp-input-faceped"
    alarm_reason = ["carry bag"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_human_tired(host, log):
    """
    [metro-web]<1.0.0> EVENT_HUMAN_TIRED(人脸疲劳)告警测试
    """
    alarm_type = "EVENT_HUMAN_TIRED"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.algo"
    alarm_reason = ["不通"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_pedestraian_leave(host, log):
    """
    [metro-web]<1.0.0> EVENT_PEDESTRIAN_LEAVE(离岗功能)告警测试
    """
    alarm_type = "EVENT_PEDESTRIAN_LEAVE"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "ksp-input-pach"
    alarm_reason = ["不通"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def material_inspection(host, log):
    """
    [metro-web]<1.0.0> MATERIAL_INSPECTION(金属检测)告警测试
    """
    alarm_type = "MATERIAL_INSPECTION"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "ksp-input-face"
    alarm_reason = ["不通"]
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason)
    return res


@flow
def event_pedestrian_invade(host, log):
    """
    [metro-web]<1.0.0> EVENT_PEDESTRIAN_INVADE(区域入侵)告警测试
    """
    alarm_type = "EVENT_PEDESTRIAN_INVADE"
    config_id = get_exist_alarm_config(host,"",alarm_type)["existAlarmConfigId"]
    input_topic = "stream.features.crowd.cross.line"
    alarm_reason = ["invasion"]
    other = {"polygons": "0,0;600,0;600,600;0,600"}
    res = alarm_function_case(host, alarm_type, config_id, input_topic, log, alarm_reason=alarm_reason, **other)
    return res


if __name__ == '__main__':
     # data = {"host": "10.198.3.14:30080"}
    data = {"host": "172.20.26.54:30080"}
    lg = get_current_log()
    # lg.info(event_hurdle_delivery(data, lg))
    lg.info(event_crowd(data, lg))

