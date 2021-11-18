#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    tmp = 0
    valleys = 0
    deep = False
    direction = list(map(lambda ch: 1 if ch=="U" else -1, path))
    for dir in direction:
        tmp += dir

        if tmp < 0:
            if not deep:
                deep = True
                valleys += 1
        else:
            deep = False
    return valleys

if __name__ == '__main__':

    steps = 8
    path = "UDDDUDUU"
    print(countingValleys(steps, path))