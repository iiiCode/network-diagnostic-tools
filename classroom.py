# coding=utf-8

import log
import json
import urllib2
import softdog
import network

from config import *


"""
每个机构会有N个音乐教室,每个音乐教室会有一个独立的软件狗,包含一个独立的Toekn,
通过该Token,可以查询该音乐教室的ID。
"""


def search_music_classroom_id():

    url = get_server_url() \
          + "/api/classroom/1.0/schools/" \
          + softdog.get_value_by_key("schoolCode") \
          + "/classrooms/current"

    log.write("Request URL: " + url)

    try:
        request = urllib2.Request(url)
        request.add_header("XiaoYeZi-Client-Token", softdog.get_value_by_key("token"))
        request.add_header("Content-Type", "application/json")
        request.add_header("Accept", "application/json")
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        log.write("Send request failed: " + str(e.reason))
        network.network_diagnostic()
        return ""

    result = response.read()
    log.write("Response = " + "\n" + result)

    if response.getcode() == HTTP_CODE_OK:
        #TODO, add try catch
        obj = json.loads(result)
        if obj["request_result"]["message"] == "OK":
            log.write("Search music classroom id success: " + obj["request_result"]["message"])
            return str(obj["classrooms"][0]["id"])
        else:
            log.write("Search music classroom id failed: " + obj["request_result"]["message"])
            return ""
    else:
        log.write("Search music classroom id failed: " + response.getcode())

    return ""


def get_teacher_list():

    classroom_id = search_music_classroom_id()
    if classroom_id == "":
        return

    url = get_server_url() \
          + "/api/classroom/1.0/schools/" \
          + softdog.get_value_by_key("schoolCode") \
          + "/classrooms/" \
          + classroom_id \
          + "/teachers"

    log.write("Request URL: " + url)

    try:
        request = urllib2.Request(url)
        request.add_header("XiaoYeZi-Client-Token", softdog.get_value_by_key("token"))
        request.add_header("Content-Type", "application/json")
        request.add_header("Accept", "application/json")
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        log.write("Send request failed: " + str(e.reason))
        network.network_diagnostic()

    result = response.read()
    log.write("Response = " + "\n" + result)

    if response.getcode() == HTTP_CODE_OK:
        # Need add try catch
        obj = json.loads(result)
        log.write("Get teacher list: " + obj["request_result"]["message"])
    else:
        log.write("Get teacher list: " + response.getcode())


def load_music_classroom_test():
    get_teacher_list()
