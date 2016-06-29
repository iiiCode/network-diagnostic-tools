"""
Music classroom network diagnostic tools entrance.
Author: Yunchao Chen
Date: 2016-6-29
"""

import log
import classroom


def main():

    log.write("NETWORK_DIAGNOSTIC_START")
    classroom.load_music_classroom_test()
    log.write("NETWORK_DIAGNOSTIC_FINISH")


main()
