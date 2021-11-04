#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    wx = list(map(lambda x: ord(x)-97, [ch for ch in word]))
    res = max([h[i] for i in wx]) * len(word)
    return res


if __name__ == '__main__':
    h = list(map(int, "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5".split()))
    word = "abc"

    print(designerPdfViewer(h, word))
