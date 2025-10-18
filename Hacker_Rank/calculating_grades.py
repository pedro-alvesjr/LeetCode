import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grades = []
    arr1 = [0, 1, 2]
    
    for grade in grades:
        multiple_of_five = ((grade + 4) // 5) * 5
        
        if grade < 38:
            final_grades.append(grade)
        
        elif multiple_of_five - grade in arr1:
            final_grades.append(multiple_of_five)
        
        else:
            final_grades.append(grade)
        
    return final_grades
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
