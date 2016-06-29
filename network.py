# coding=utf-8

"""
Music classroom network diagnostic module.
Author: Yunchao Chen
Date: 2016-06-29
"""

import log


def resolve_baidu_domain():
    return True


def ping_baidu():
    return True


def ping_gate_way():
    return True


def get_operator_info():
    return True


def resolve_api_domain():
    return True


def access_download_api():
    return True


def access_get_classroom_api():
    return True


def network_diagnostic():

    if not resolve_baidu_domain():
        if ping_baidu():
            log.e("DNS error.")
        else:
            if ping_gate_way():
                log.e("外网设置问题。")
            else:
                log.e("路由器连接问题。")

    else:
        get_operator_info()

        if not resolve_api_domain():
            log.e("API域名DNS问题。")
        else:
            if not access_download_api():
                log.e("访问我们服务有问题")
            else:
                if not access_get_classroom_api():
                    log.e("访问获取教室API有问题。")
                else:
                    log.e("访问获取教室API正常。")
                    log.e("网络诊断正常。")


