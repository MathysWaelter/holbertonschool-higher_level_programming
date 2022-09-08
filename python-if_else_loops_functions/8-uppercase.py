#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if i == ord(c):
            return 1
        else:
            return 0

def uppercase(str):
    for i in str:
        print("{:c}".format(ord(i) if not islower(i) else ord(i) - 32), end='')
    print('')
	