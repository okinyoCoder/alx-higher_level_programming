#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivionError:
           result = None
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
        return result
