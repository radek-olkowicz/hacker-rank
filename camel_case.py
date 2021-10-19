#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    tmp_result = 1
    for ch in s:
        if ch == ch.upper():
            tmp_result += 1
    return tmp_result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #    s = input()

    result = camelcase("abcDupaDupa")
    print(result)
