#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    l = len(arr)
    bigger_than_zero = 0
    smaller_than_zero = 0
    same_as_zero = 0

    for n in arr:
        if n > 0:
            bigger_than_zero += 1
        elif n < 0:
            smaller_than_zero += 1
        else:
            same_as_zero += 1

    ratio_bigger = bigger_than_zero / l
    ratio_smaller = smaller_than_zero / l
    ratio_same = same_as_zero / l
    
    print(f'{ratio_bigger:.6f}')
    print(f'{ratio_smaller:.6f}')
    print(f'{ratio_same:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
