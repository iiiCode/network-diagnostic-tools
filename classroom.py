import log
import urllib2
import softdog


API_LEVEL_DEV  = 0
API_LEVEL_PRE  = 1
API_LEVEL_PROD = 2

API_VERSION = "1.0"

SERVER_URL_LIST = [
    "http://cr-api.dev-cr.xiaoyezi.com",
    "http://cr-api.pre-cr.xiaoyezi.com",
    "http://cr-api.cr.xiaoyezi.com"
]

def get_server_url(api_level):

    if api_level < 0 or api_level > 2:
        log.e("API_LEVEL: " + api_level + " not correct.")

    return SERVER_URL_LIST[api_level]


def get_current_classroom_info():

    url = get_server_url(API_LEVEL_DEV) \
          + "/api/classroom/1.0/schools/" \
          + softdog.read_soft_dog_data_by_key("schoolCode") \
          + "/classrooms/current"

    log.d("URL: " + url)

    request = urllib2.Request(url)
    request.add_header("XiaoYeZi-Client-Token", softdog.read_soft_dog_data_by_key("token"))
    request.add_header("Content-Type", "application/json")
    request.add_header("Accept", "application/json")
    response = urllib2.urlopen(request)

    if response.getcode() == 200:
        log.e("Get current classroom info success.")
        log.d(response.read())
    else:
        log.e("Get current classroom info failed, return code: " + response.getcode())

    return response.read()


get_current_classroom_info()