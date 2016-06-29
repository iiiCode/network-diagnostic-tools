"""
Music classroom network diagnostic tools entrance.
Author: Yunchao Chen
Date: 2016-6-29
"""

import classroom

TEST_FUNCS = [
    classroom.load_music_classroom_test(),
]


def main():

    for func in TEST_FUNCS:
        func()
