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
import subprocess

from config import *


def ping(server):

    log.write("EXEC_PING_COMMAND")
    ret = subprocess.call(["ping", "-c 3",  server],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return ret == 0


def ip_check(ip_list):

    for ip in ip_list:
        _ip = str(ip[4][0])

        if _ip.startswith("10.") or \
            _ip.startswith("172.") or \
            _ip.startswith("192.168"):

            return False

    return True


def resolve_baidu_domain():

    log.write("EXEC_RESOLVE_DOMAIN")

    try:
        results = socket.getaddrinfo("www.baidu.com", 80, socket.AF_INET, 0, 0, 0)
    except socket.error, err:
        (errno, error_message) = err
        error_message = "ErrorNo: " + str(errno) + " " + error_message
        log.write(error_message)
        log.write("RESOLVE_BAIDU_DOMAIN_FAILED")
        return False

    ip_list = "BaiDu IPs: "
    for result in results:
        ip_list = ip_list + "[" + result[4][0] + "]"
    log.write(ip_list)

    if not ip_check(results):
        log.write("RESOLVE_BAIDU_DOMAIN_FAILED")
        return False

    log.write("RESOLVE_BAIDU_DOMAIN_SUCCESS")

    return True


def ping_baidu():

    if ping("61.135.169.121"):
        log.write("PING_BAIDU_SUCCESS")
        return True

    log.write("PING_BAIDU_FAILED")
    return False


def ping_gate_way():

    host_name = socket.gethostname()
    log.write("host name: " + host_name)

    local_ip = socket.gethostbyname(host_name)
    log.write("local IP: " + local_ip)

    if local_ip == "127.0.0.1":
        log.write("PC_IP_NOT_CORRECT")
        return False

    dot_pos = local_ip.rfind(".")
    gate_way_ip = local_ip[0:dot_pos+1] + "1"
    log.write("Gate way IP: " + gate_way_ip)

    if ping(gate_way_ip):
        log.write("PING_GATE_WAY_SUCCESS")
        return True

    log.write("PING_GATE_WAY_FAILED")
    return False


def get_ip_provider_info():

    try:
        request = urllib2.Request(IP_PROVIDER)
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        log.write(e.reason)
        log.write("GET_IP_PROVIDER_INFO_FAILED")

    ret = str(response.read()).decode("gb2312")

    lpos = ret.find("center")
    rpos = ret.rfind("center")

    log.write("GET_IP_PROVIDER_INFO_SUCCESS")
    info = ret[lpos+7:rpos-2].encode("utf-8")
    log.write(info)
    log.console(info)


def resolve_server_api_domain():

    log.write("EXEC_RESOLVE_DOMAIN")

    try:
        results = socket.getaddrinfo(get_server_url(), None)
    except Exception, e:
        log.write(str(e))
        log.write("RESOLVE_XIOYEZI_SERVER_API_DOMAIN_FAILED")
        return False

    str = "XiaoYeZi IPs: "
    for result in results:
        str = str + "[" + result[4][0] + "]"

    log.write(str)
    log.write("RESOLVE_XIOYEZI_SERVER_API_DOMAIN_SUCCESS")
    return True


def access_resource_download_api():

    try:
        request = urllib2.Request(RESOURCE_DOWNLOAD_API)
        request.add_header("Content-Type", "application/json")
        request.add_header("Accept", "application/json")
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        log.write(str(e.reason))
        log.write("ACCESS_RESOURCE_DOWNLOAD_API_FAILED")
        return False

    ret = response.read()
    log.write(ret)

    if response.getcode() == HTTP_CODE_OK:

        obj = json.loads(ret)

        if obj["request_result"]["message"] == "OK":
            log.write("ACCESS_RESOURCE_DOWNLOAD_API_SUCCESS")
            return True

    log.write(response.getcode())
    log.write("ACCESS_RESOURCE_DOWNLOAD_API_FAILED")

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
        log.write("ACCESS_GET_CLASSROOM_API_FAILED")
        log.write("Send request failed: " + str(e.reason))
        return False

    result = response.read()
    log.write(result)

    if response.getcode() == HTTP_CODE_OK:
        # TODO, add try catch
        obj = json.loads(result)
        if obj["request_result"]["message"] == "OK":
            log.write("ACCESS_GET_CLASSROOM_API_SUCCESS")
            return True

    log.write("ACCESS_GET_CLASSROOM_API_FAILED")
    return False


def network_diagnostic():

    if not resolve_baidu_domain():
        if ping_baidu():
            log.write("DNS_ERROR")
        else:
            if ping_gate_way():
                log.write("ETHERNET_ERROR")
            else:
                log.write("ROUTER_ERROR")

    else:
        get_ip_provider_info()

        if resolve_server_api_domain():
            if access_resource_download_api():
                if access_get_classroom_api():
                    log.write("NETWORK_DIAGNOSTIC_SUCCESS")
