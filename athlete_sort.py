#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    arr.append(list(map(int, "10 2 5".rstrip().split())))
    arr.append(list(map(int, "7 1 0".rstrip().split())))
    arr.append(list(map(int, "9 9 9".rstrip().split())))
    arr.append(list(map(int, "1 23 12".rstrip().split())))
    arr.append(list(map(int, "6 5 9".rstrip().split())))
    k = 1

    for row in sorted(arr, key=lambda data: data[k]):
        print(" ".join(map(str, row)))
    
