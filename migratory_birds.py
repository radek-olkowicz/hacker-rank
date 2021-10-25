#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def def_val():
    return 0

def migratoryBirds(arr):
    dic = defaultdict(def_val)
    for bird in arr:
        dic[bird] += 1
    key, val = sorted(dic.items(), key = lambda k_v: k_v[1], reverse=True)[0]
    answers = []
    for K in dic.keys():
        if(dic[K] == val):
            answers.append(K)
    return(str(min(answers)))

if __name__ == '__main__':
    result = migratoryBirds([1, 4, 4, 4, 5, 3])
    print(result)