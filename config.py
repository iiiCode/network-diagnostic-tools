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

LOG_FILE_NAME = "result.log"

MSG_DATA = {
    "NETWORK_DIAGNOSTIC_START": "网络诊断开始...",
    "NETWORK_DIAGNOSTIC_SUCCESS": "网络诊断结束,诊断正常。",
    "NETWORK_DIAGNOSTIC_FAILED": "网络诊断结束,诊断异常。",

    "BAD_SOFT_DOG_LIBRARY": "加密狗库文(win32dll.dll)件损坏。",
    "SOFT_DOG_LIBRARY_FOUND": "加密狗库文件(win32dll.dll)找到。",
    "SOFT_DOG_LIBRARY_NOT_FOUND": "加密狗库文件(win32dll.dll)未找到。",
    "LOAD_SOFT_DOG_LIBRARY_SUCCESS": "加载加密狗库文件(win32dll.dll)成功。",
    "SOFT_DOG_READ_METHOD_EXIST": "加密狗库文件(win32dll.dll)DogRead方法存在。",
    "SOFT_DOG_READ_METHOD_NOT_EXIST": "加密狗库文件(win32dll.dll)DogRead方法不存在。",
    "LOAD_SOFT_DOG_LIBRARY_FAILED": "加载加密狗库文件(win32dll.dll)失败。",
    "READ_SOFT_DOG_DATA_FAILED": "读取加密狗数据失败,请检查加密狗是否插入,或驱动是否正确安装。",
    "READ_SOFT_DOG_DATA_SUCCESS": "读取加密狗数据成功。",
    "USE_FAKE_SOFT_DOG_DATA": "使用假的加密狗数据做测试。"
}
