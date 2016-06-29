# coding=utf-8

"""
Music classroom network diagnostic module.
Author: Yunchao Chen
Date: 2016-06-29
"""

import os
import log
import json
import socket
import urllib2
import softdog

from config import *


def resolve_baidu_domain():

    try:
        results = socket.getaddrinfo("www.baidu.com", None)

        for result in results:
            print result

    except Exception, e:
        print e
        return False

    return True


def ping_baidu():

    #TODO only for Unix-like OS
    ret = os.system("ping -c 3 61.135.169.121")

    return ret == 0


def ping_gate_way():

    host_name = socket.gethostname()
    local_ip = socket.gethostbyname(host_name)

    if local_ip == "127.0.0.1":
        return False

    print local_ip
    dot_pos = local_ip.rfind(".")
    gate_way_ip = local_ip[0:dot_pos+1] + "1"

    # TODO only for Unix-like OS
    ret = os.system("ping -c 3 " + gate_way_ip)

    return ret == 0


def get_ip_provider_info():

    try:
        request = urllib2.Request(IP_PROVIDER)
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        log.write(e.reason)
        return ""

    ret = str(response.read()).decode("gb2312")

    lpos = ret.find("center")
    rpos = ret.rfind("center")

    return ret[lpos+7:rpos-2]


def resolve_api_domain():

    try:
        results = socket.getaddrinfo(get_server_url(), None)

        for result in results:
            print result

    except Exception, e:
        print e
        return False

    return True


def access_download_api():

    try:
        request = urllib2.Request(RESOURCE_DOWNLOAD_API)
        request.add_header("Content-Type", "application/json")
        request.add_header("Accept", "application/json")
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        log.write(e.reason)
        return False

    ret = response.read()
    log.write(ret)

    if response.getcode() == HTTP_CODE_OK:

        obj = json.loads(ret)

        if obj["request_result"]["message"] == "OK":
            return True

    log.write(response.getcode())

    return False


def access_get_classroom_api():

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
        return False

    result = response.read()
    log.write(result)

    if response.getcode() == HTTP_CODE_OK:
        # TODO, add try catch
        obj = json.loads(result)
        if obj["request_result"]["message"] == "OK":
            return True

    return False


def network_diagnostic():

    if not resolve_baidu_domain():
        if ping_baidu():
            log.write("DNS问题")
        else:
            if ping_gate_way():
                log.write("外网设置问题。")
            else:
                log.write("路由器连接问题。")

    else:
        get_ip_provider_info()

        if not resolve_api_domain():
            log.write("API域名DNS问题。")
        else:
            if not access_download_api():
                log.write("访问我们服务有问题")
            else:
                if not access_get_classroom_api():
                    log.write("访问获取教室API有问题。")
                else:
                    log.write("访问获取教室API正常。")
                    log.write("网络诊断正常。")


network_diagnostic()