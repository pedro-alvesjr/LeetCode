import os


def timeConversion(s):
    time_stamp = s[-2:]
    hh, mm, ss = map(int, s[:-2].split(':'))
    
    if time_stamp == 'PM':
        if hh != 12:
            hh += 12
            
    if time_stamp == 'AM':
        if hh == 12:
            hh = 0
    
    return f'{hh:02}:{mm:02}:{ss:02}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
