import os

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    max_score, min_score = 0, 0
    maximum, minimum = scores[0], scores[0]
    
    for i in range(len(scores)):
        if scores[i] > maximum:
            maximum = scores[i]
            max_score += 1
            
        
        if scores[i] < minimum:
            minimum = scores[i]
            min_score += 1
            
    return [max_score, min_score]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
