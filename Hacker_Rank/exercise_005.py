import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    
    minList = arr[:]
    maxList = arr[:]
    minResult, maxResult = 0, 0
    
    minList.pop(len(arr) - 1)
    maxList.pop(0)
    
    for num in minList:
        minResult += num
        
    for num in maxList:
        maxResult += num
        
    print(minResult, maxResult)
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
