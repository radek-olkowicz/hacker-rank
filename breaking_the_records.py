#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    highest = [scores[0]]
    lowest = [scores[0]]
    for item in scores:
        if item > highest[-1]:
            highest.append(item)
        elif item < lowest[-1]:
            lowest.append(item)
    return(len(highest)-1, len(lowest)-1)


    
    return [low, high]

if __name__ == '__main__':
    scores = list(map(int, "10 5 20 20 4 5 2 25 1".split()))

    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
