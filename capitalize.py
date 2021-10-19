#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve_old(s):
    list_of_words = []
    list_of_spaces = []
    space = ""
    for char in s:
        if(char == " "):
            space += " "
        else:
            if (space != ""):
                list_of_spaces.append(space)
                space = ""
    for name in s.split():
        list_of_words.append(name.capitalize())
    result = ""
    for i in range(len(list_of_spaces)):
        result += list_of_words[i] + list_of_spaces[i]
    result += list_of_words[-1]
    return(result)

def solve(s):
    return(" ".join(name.capitalize() for name in s.split(" ")))


if __name__ == '__main__':
    print(solve("132 456 Wq      m e"))