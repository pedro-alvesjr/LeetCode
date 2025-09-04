import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    spaces = n - 2
    hashtags = 1
    
    while hashtags != n:
        print(' ' * spaces, '#' * hashtags)
        spaces -= 1
        hashtags += 1
        
    print('#' * hashtags)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
