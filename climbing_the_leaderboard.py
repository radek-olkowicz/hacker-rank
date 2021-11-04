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
    L = 0
    R = len(board)

    for pts in player:
        if (pts > board[0]):
            ret.append(1)
            continue
        if (pts < board[-1]):
            ret.append(R+1)
            continue
        try:
            ret.append(board.index(pts)+1)
        except ValueError:
            found = False
            while not found:            
                pos = (R + L) // 2            
                if board[pos] >= pts and board[pos+1] <= pts:
                    found = True
                    ret.append(pos+2)
                elif board[pos] > pts and board[pos+1] > pts:
                    L = pos
                elif board[pos] < pts and board[pos+1] < pts:
                    R = pos        
    return ret

if __name__ == '__main__':
    # ranked_count = int(input().strip())
    # player_count = int(input().strip())

    r_input = "100 100 50 40 40 20 10"
    p_input = "5 25 50 120"

    ranked = list(map(int, r_input.rstrip().split()))
    player = list(map(int, p_input.rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    print('\n'.join(map(str, result)))
