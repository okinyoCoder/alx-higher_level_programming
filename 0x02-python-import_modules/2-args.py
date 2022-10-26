#!/usr/bin/python3
import sys
if __name__ = "__main__":
    i = len(sys.argv)
    if i == 1:
        print("{} arguments.".format(i-1))
    elif i == 2:
        print("{} argument:".format(i-1))
        Print("{:d}: {:s}".format(i-1, sys.argv[i]))
    else:
        print("{} argument:".format(i-1))
        for j in range(1, i):
            print("{}: {}".format(i, sys.argv[i]))
