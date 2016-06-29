# coding=utf-8


import sys
import time

from config import MSG_DATA
from config import LOG_FILE_NAME


def save_to_log_file(message):
    fp = open(LOG_FILE_NAME, "a+")
    fp.write(message)
    fp.close()


def write(message):

    is_msg_data = False

    for msg in MSG_DATA:
        if msg == message:
            is_msg_data = True
            break


    if is_msg_data:
        message = MSG_DATA[message]

    message = time.strftime('%Y-%m-%d %H:%M:%S') + ": " + message + "\n"

    if is_msg_data:
        sys.stdout.write(message)

    save_to_log_file(message)
