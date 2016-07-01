"""
Music classroom network diagnostic tools entrance.
Author: Yunchao Chen
Date: 2016-6-29
"""

import log
import classroom

from config import MSG_DATA


def log_init():
    log_file = log.generate_log_file_name()
    log.open_file(log_file)


def log_destroy():
    log.close_file()


def pause_until_meet_enter_key():
    print ""
    raw_input("")


def main():

    log_init()
    log.write("NETWORK_DIAGNOSTIC_START")
    classroom.load_music_classroom_test()
    log.write("NETWORK_DIAGNOSTIC_FINISH")
    pause_until_meet_enter_key()
    log_destroy()


main()
