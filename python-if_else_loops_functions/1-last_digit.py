#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = repr(number)
last_digitstr = digit[-1]
last_digit = int(last_digitstr)

last_digit = -last_digit if digit[0] == '-' else last_digit

if number:
    print(f'Last digit of {number} is {last_digit} ', end='')
    if last_digit > 5:
        print('and is greater than 5')
    elif last_digit == 0:
        print('and is 0')
    else:
        print('and is less than 6 and not 0')
