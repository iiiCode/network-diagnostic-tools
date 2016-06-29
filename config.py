# coding=utf-8

"""
Music classroom network diagnostic tools config file.
Author: Yunchao Chen
Date: 2016-06-29
"""

# For Soft dog
SOFT_DOG_DATA_SIZE = 32
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


# For HTTP return code
HTTP_CODE_OK = 200

# For music classroom pressure test
MUSIC_CLASSROOM_PRESSURE_TEST = False
