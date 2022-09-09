#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for i in range(1, len(argv)):
        if (len(argv) - 1) == 0:
            print('0')
        else:
            sum += int(argv[i])
print(sum)
