#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for i in range(len(str)):
        if (str[i] >= 'a' and str[i] <= 'z'):
            upper = upper = + chr((ord(str[i]) - 32))
            print("{:c}".format(upper), end='')
        else:
            upper = upper + str[i]
            print("{:c}".format(upper), end='')
