"""
Read Soft Dog Data. if USE_FAKE_SOFT_DOG_DATA set to True, it will use the FAKE token for the
following check, please Be Careful.

Author: Yunchao Chen
Date: 2016-06-29
"""

import os
import sys
import log
import json
import ctypes

from config import *

SOFT_DOG_DATA = {}


def soft_dog_library_exist():

    if not os.path.exists(SOFT_DOG_LIBRARY):
        log.write("SOFT_DOG_LIBRARY_NOT_FOUND")
        return False

    log.write("SOFT_DOG_LIBRARY_FOUND")

    return True


def __read_soft_dog_data(out_buffer):

    if not soft_dog_library_exist():
        return False

    windll = ctypes.WinDLL(SOFT_DOG_LIBRARY)
    if not windll:
        log.write("LOAD_SOFT_DOG_LIBRARY_FAILED")
        return False
    
    log.write("LOAD_SOFT_DOG_LIBRARY_SUCCESS")

    if not windll.DogRead:
        log.write("SOFT_DOG_READ_METHOD_NOT_EXIST")
        return False

    log.write("SOFT_DOG_READ_METHOD_EXIST")

    data_bytes = ctypes.c_ulong(90)
    read_addr = ctypes.c_ulong(0)
    windll.DogRead.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_char_p]
    windll.DogRead(data_bytes, read_addr, out_buffer)

    return True


def _read_soft_dog_data():

    if USE_FAKE_SOFT_DOG_DATA:
        log.write("USE_FAKE_SOFT_DOG_DATA")
        return FAKE_SOFT_DOG_DATA

    soft_dog_data = ""
    out_buffer = (ctypes.c_char * SOFT_DOG_DATA_SIZE)('\0')

    if __read_soft_dog_data(out_buffer):
        for item in out_buffer:
            if item == '\0':
                break
            soft_dog_data = soft_dog_data + item

    return soft_dog_data


def _parse_school_and_classroom_code():
    code_list = SOFT_DOG_DATA["schoolAndClassroomCode"].split('-')
    SOFT_DOG_DATA["schoolCode"] = code_list[0]
    SOFT_DOG_DATA["classroomCode"] = code_list[1]


def _parse_soft_dog_data(soft_dog_data):

    if soft_dog_data == "":
        log.write("READ_SOFT_DOG_DATA_FAILED")
        log.write("NETWORK_DIAGNOSTIC_FAILED")
        sys.exit()

    soft_dog_data_list = soft_dog_data.split(';')

    SOFT_DOG_DATA["token"] = soft_dog_data
    SOFT_DOG_DATA["version"] = soft_dog_data_list[0]
    SOFT_DOG_DATA["schoolAndClassroomCode"] = soft_dog_data_list[1]
    SOFT_DOG_DATA["studentCount"] = soft_dog_data_list[2]
    SOFT_DOG_DATA["startDate"] = soft_dog_data_list[3]
    SOFT_DOG_DATA["endDate"] = soft_dog_data_list[4]
    SOFT_DOG_DATA["hash"] = soft_dog_data_list[5]

    _parse_school_and_classroom_code()

    log.write(json.dumps(SOFT_DOG_DATA))


def get_value_by_key(key):

    global SOFT_DOG_DATA_HAS_PARSED

    if not SOFT_DOG_DATA_HAS_PARSED:
        _parse_soft_dog_data(_read_soft_dog_data())
        SOFT_DOG_DATA_HAS_PARSED = True

    key_list = ["token", "version", "schoolAndClassroomCode",
                "studentCount", "startDate", "endDate", "hash",
                "schoolCode", "classroomCode"]

    if key not in key_list:
        log.write("Key: " + key + " not correct.")
        return ""

    return SOFT_DOG_DATA[key]
