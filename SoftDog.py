import os
import log
import ctypes

SOFT_DOG_DATA_SIZE = 256
SOFT_DOG_LIBRARY = "win32dll.dll"

SOFT_DOG_DATA = {}
SOFT_DOG_DATA_HAS_PARSED = False


def check_soft_dog_library_exist():

    if not os.path.exists(SOFT_DOG_LIBRARY):
        log.e(SOFT_DOG_LIBRARY + " is not exist.")
        return False

    log.d(SOFT_DOG_LIBRARY + " is exist.")

    return True


def __read_soft_dog_data(out_buffer):

    # TODO
    # Check SOFT_DOG_LIBRARY if is exits.
    if not check_soft_dog_library_exist():
        return False

    windll = ctypes.WinDLL(SOFT_DOG_LIBRARY)
    if not windll:
        log.e("Load soft dog library: " + SOFT_DOG_LIBRARY + " failed!!!")
        return False
    
    log.d("Load soft dog library: " + SOFT_DOG_LIBRARY + " Success.")

    if not windll.DogRead:
        log.e("Can not find function entry: DogRead")
        return False

    data_bytes = ctypes.c_ulong(90)
    read_addr = ctypes.c_ulong(0)
    windll.DogRead.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_char_p]
    windll.DogRead(data_bytes, read_addr, out_buffer)

    return True


def _read_soft_dog_data():
    soft_dog_data = ""
    out_buffer = (ctypes.c_char * SOFT_DOG_DATA_SIZE)('\0')

    if __read_soft_dog_data(out_buffer):
        for item in out_buffer:
            if item == '\0':
                break
            soft_dog_data = soft_dog_data + item

    return soft_dog_data


def _read_fake_soft_dog_data():
    return "v1;HLG-C1;2;20160623;;19233099"


def _parse_school_and_classroom_code():
    code_list = SOFT_DOG_DATA["schoolAndClassroomCode"].split('-')
    SOFT_DOG_DATA["schoolCode"] = code_list[0]
    SOFT_DOG_DATA["classroomCode"] = code_list[1]


def _parse_soft_dog_data(soft_dog_data):

    soft_dog_data_list = soft_dog_data.split(';')

    SOFT_DOG_DATA["token"] = soft_dog_data
    SOFT_DOG_DATA["version"] = soft_dog_data_list[0]
    SOFT_DOG_DATA["schoolAndClassroomCode"] = soft_dog_data_list[1]
    SOFT_DOG_DATA["studentCount"] = soft_dog_data_list[2]
    SOFT_DOG_DATA["startDate"] = soft_dog_data_list[3]
    SOFT_DOG_DATA["endDate"] = soft_dog_data_list[4]
    SOFT_DOG_DATA["hash"] = soft_dog_data_list[5]

    _parse_school_and_classroom_code()


def read_soft_dog_data_by_key(key):

    global SOFT_DOG_DATA_HAS_PARSED

    if not SOFT_DOG_DATA_HAS_PARSED:
        _parse_soft_dog_data(_read_fake_soft_dog_data())
        SOFT_DOG_DATA_HAS_PARSED = True

    key_list = ["token", "version", "schoolAndClassroomCode",
                "studentCount", "startDate", "endDate", "hash",
                "schoolCode", "classroomCode"]

    if key not in key_list:
        log.e("Key: " + key + " not correct.")
        return ""

    return SOFT_DOG_DATA[key]

