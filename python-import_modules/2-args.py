#!/usr/bin/python3
from sys import argv
if (len(argv) - 1) == 0:
    print('0 arguments.')
else:
    print("{} {}:".format(len(argv) - 1,
          "argument" if len(argv) - 1 == 1 else "arguments"))
for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
