# coding=utf-8

"""
Music classroom network diagnostic tools config file.
Author: Yunchao Chen
Date: 2016-06-29
"""

# For Soft dog
SOFT_DOG_DATA_SIZE = 128
SOFT_DOG_LIBRARY = "win32dll.dll"
SOFT_DOG_DATA_HAS_PARSED = False

USE_FAKE_SOFT_DOG_DATA = True
FAKE_SOFT_DOG_DATA = "v1;HLG-C1;2;20160623;;19233099"

# For classroom API
API_VERSION = "1.0"

API_LEVEL_DEV = 0
API_LEVEL_PRE = 1
API_LEVEL_PROD = 2

SERVER_URL_LIST = [
    "http://cr-api.dev-cr.xiaoyezi.com",
    "http://cr-api.pre-cr.xiaoyezi.com",
    "http://cr-api.cr.xiaoyezi.com"
]

API_LEVEL = API_LEVEL_DEV

RESOURCE_DOWNLOAD_API = "http://cr-api.cr.xiaoyezi.com/api/classroom/1.0/courses"


def get_server_url():
    return SERVER_URL_LIST[API_LEVEL]


# For HTTP return code
HTTP_CODE_OK = 200

# For music classroom pressure test
MUSIC_CLASSROOM_PRESSURE_TEST = False

# For IP Provider
IP_PROVIDER = "http://1212.ip138.com/ic.asp"


# For Log

LOG_FILE_HANDLE = None

MSG_DATA = {
    "NETWORK_DIAGNOSTIC_START": "网络诊断开始...",
    "NETWORK_DIAGNOSTIC_FINISH": "网络诊断结束。",
    "NETWORK_DIAGNOSTIC_SUCCESS": "网络诊断正常。",
    "NETWORK_DIAGNOSTIC_FAILED": "网络诊断异常。",

    "BAD_SOFT_DOG_LIBRARY": "加密狗库文(win32dll.dll)件损坏。",
    "SOFT_DOG_LIBRARY_FOUND": "加密狗库文件(win32dll.dll)找到。",
    "SOFT_DOG_LIBRARY_NOT_FOUND": "加密狗库文件(win32dll.dll)未找到。",
    "LOAD_SOFT_DOG_LIBRARY_SUCCESS": "加载加密狗库文件(win32dll.dll)成功。",
    "SOFT_DOG_READ_METHOD_EXIST": "加密狗库文件(win32dll.dll)DogRead方法存在。",
    "SOFT_DOG_READ_METHOD_NOT_EXIST": "加密狗库文件(win32dll.dll)DogRead方法不存在。",
    "LOAD_SOFT_DOG_LIBRARY_FAILED": "加载加密狗库文件(win32dll.dll)失败。",
    "READ_SOFT_DOG_DATA_FAILED": "读取加密狗数据失败,请检查加密狗是否插入,或驱动是否正确安装。",
    "READ_SOFT_DOG_DATA_SUCCESS": "读取加密狗数据成功。",
    "USE_FAKE_SOFT_DOG_DATA": "使用假的加密狗数据做测试。",

    "GET_CLASSROOM_ID_SUCCESS": "获取音乐教室ID成功。",
    "GET_CLASSROOM_ID_FAILED": "获取音乐教室ID失败。",
    "GET_CLASSROOM_TEACHER_LIST_SUCCESS": "获取音乐教室教师列表成功。",
    "GET_CLASSROOM_TEACHER_LIST_FAILED" : "获取音乐教室教师列表失败。",

    "RESOLVE_BAIDU_DOMAIN_SUCCESS": "解析百度域名成功。",
    "RESOLVE_BAIDU_DOMAIN_FAILED": "解析百度域名失败。",

    "PING_BAIDU_SUCCESS": "ping百度成功。",
    "PING_BAIDU_FAILED": "ping百度失败。",

    "PC_IP_NOT_CORRECT": "本机获取的IP不正确。",

    "PING_GATE_WAY_SUCCESS": "ping路由器网关成功。",
    "PING_GATE_WAY_FAILED": "ping路由器网关失败。",

    "GET_IP_PROVIDER_INFO_SUCCESS": "获取机构IP供应商信息成功。",
    "GET_IP_PROVIDER_INFO_FAILED": "获取机构IP供应商信息失败。",

    "RESOLVE_XIOYEZI_SERVER_API_DOMAIN_SUCCESS": "解析小叶子服务器API域名成功。",
    "RESOLVE_XIOYEZI_SERVER_API_DOMAIN_FAILED": "解析小叶子服务器API域名失败。",

    "ACCESS_RESOURCE_DOWNLOAD_API_SUCCESS": "访问资源下载API成功。",
    "ACCESS_RESOURCE_DOWNLOAD_API_FAILED": "访问资源下载API失败。",

    "ACCESS_GET_CLASSROOM_API_SUCCESS": "访问获取音乐教室API成功。",
    "ACCESS_GET_CLASSROOM_API_FAILED": "访问获取音乐教室API失败。",

    "DNS_ERROR": "DNS错误,请价差DNS配置。",
    "ETHERNET_ERROR": "公网配置错误,请检查公网配置。",
    "ROUTER_ERROR" : "电脑没有连接路由器,请检查电脑和路由器连线。",

    "EXEC_PING_COMMAND": "正在执行ping命令,请稍等...",
    "EXEC_RESOLVE_DOMAIN": "正在解析域名,请稍等...",

    "SEARCH_CLASSROOM_ID": "正在获取音乐教室ID,请稍等...",
    "SEARCH_TEACHER_LIST": "正在获取教师列表,请稍等..."
}
