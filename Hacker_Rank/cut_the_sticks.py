import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    final_result = []
    
    while arr:
        final_result.append(len(arr))
        
        smallest_stick = min(arr)
            
        for i in range(len(arr)):
            arr[i] = arr[i] - smallest_stick
        
        arr = [x for x in arr if x != 0]
        
    return final_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
