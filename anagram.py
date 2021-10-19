#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    tmp_result = 0

    if len(s) % 2 == 1:
        return -1
    spl = int(len(s)/2)
    left = s[:spl]
    right = s[spl:] 

    for ch in left:
        if ch not in right:
            tmp_result += 1
        else:
            right = right[:right.find(ch)] + right[right.find(ch)+1:]
            print(right + "\n")
    return tmp_result


if __name__ == '__main__':
    #print(anagram("hhpddlnnsjfoyxpciioigvjqzfbpllssuj"))
    #print(anagram("xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj"))
    #print(anagram("dnqaurlplofnrtmh"))
    print(anagram("aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb"))
    print(anagram("lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad"))
    print(anagram("drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe"))
    print(anagram("ubulzt"))
    print(anagram("vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy"))
    print(anagram("xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa"))
    print(anagram("gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv"))