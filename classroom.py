import log
import json
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


def check_request_result(response):

    obj = json.loads(response)
    message = obj["request_result"]["message"]

    if message == "OK":
        log.e("Get current classroom info success.")
    else:
        log.e("Get current classroom info failed: " + message)


def check_get_current_classroom_info():

    api_level = API_LEVEL_DEV

    url = get_server_url(api_level) \
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
        log.e("Can communicate with Server: " + get_server_url(api_level))
        check_request_result(response.read())
    else:
        log.e("Get current classroom info failed, return code: " + response.getcode())


check_get_current_classroom_info()