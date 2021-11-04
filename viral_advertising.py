#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shares = 5
    likes = shares // 2
    cumulative = likes
    for i in range(n-1):
        shares = likes * 3
        likes = shares // 2
        cumulative += likes
        # print("{} {} {}".format(shares, likes, cumulative)) 
    return cumulative


if __name__ == '__main__':
    n = 5

    result = viralAdvertising(n)
    print(result)