# coding=utf-8


import sys
import time

from config import *


def save_to_log_file(message):
    global LOG_FILE_HANDLE
    LOG_FILE_HANDLE.write(message)


def console(message):
    sys.stdout.write(message + "\n")


def write(message):

    is_msg_data = False

    for msg in MSG_DATA:
        if msg == message:
            is_msg_data = True
            break

    if is_msg_data:
        message = MSG_DATA[message] + "\n"
        sys.stdout.write(message)
        return

    message = time.strftime('%Y-%m-%d %H:%M:%S') + ": " + message + "\n"
    save_to_log_file(message)


def generate_log_file_name():

    file_name = "network-diagnostic-"
    date_str = time.strftime('%Y-%m-%d-%H_%M_%S')

    return file_name + date_str + ".log"


def open_file(file_name):
    global LOG_FILE_HANDLE
    LOG_FILE_HANDLE = open(file_name, "a+")


def close_file():
    global LOG_FILE_HANDLE
    LOG_FILE_HANDLE.close()
    LOG_FILE_HANDLE = None

