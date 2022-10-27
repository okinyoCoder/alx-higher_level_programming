#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for n in my_string:
        while n != 'c' or n != 'C':
            new_string += n
    return new_string
