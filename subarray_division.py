#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    tmp_res = 0
    for i in range(len(s)-m+1):
        if(sum(s[i:i+m]) == d):
            tmp_res += 1
    return tmp_res

if __name__ == '__main__':
    n = 6
    s = [1, 1, 1, 1, 1, 1]
    d = 3
    m = 2

    result = birthday(s, d, m)
    print(result)