import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    N = -1
    if(v1 != v2):
        N  = (x2 - x1) / (v1 - v2)
    if ((N < 0) or (N!=int(N))):
        return "NO"
    return "YES"

if __name__ == '__main__':
    result = kangaroo(43, 2, 70, 2)
    print(result)


