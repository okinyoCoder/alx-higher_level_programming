#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    m = len(argv)
    if n == 1:
        print(0)
    else:
        sum = 0
        for i in range(1, m):
            sum+=int(argv)
        print("{}".format(sum))
