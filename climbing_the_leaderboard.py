#!/bin/python3

import math
import os
import random
import re
import sys


from itertools import accumulate

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def count_gt(arr, number): 
    tmp = sum(list(map(lambda x: int(x>number), arr)))
    return tmp

def climbingLeaderboard(ranked, player):
    board = list(set(ranked))
    board.sort(reverse=True)
    ret = []    
    loop = 0
    for pts in player:
        loop += 1
        print(loop)
        if (pts > board[0]):
            ret.append(1)
            break
        if (pts < board[-1]):
            ret.append(R)
        found = False
        L = 0
        R = len(board)

        while not found:
            pos = (R + L) // 2            
            if board[pos] > pts and board[pos+1] < pts:
                found = True
                ret.append(pos)
            elif board[pos] > pts and board[pos+1] > pts:
                L = pos
            elif board[pos] < pts and board[pos+1] < pts:
                R = pos
            # print("pos={}  pts={}    board[pos]={} board[pos+1]={} L={} R={}".format(pos, pts, board[pos], board[pos+1], L, R))
        
    return ret

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
