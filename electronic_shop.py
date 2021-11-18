#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    max_price = -1
    for k in keyboards:
        for d in drives:
            if k+d <= b and k+d > max_price:
                max_price = k+d
    return max_price


if __name__ == '__main__':
    b = 60
    keyboards = list(map(int, "40 50 60".rstrip().split()))
    drives = list(map(int, "5 8 12".rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)

