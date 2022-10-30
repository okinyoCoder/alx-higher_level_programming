#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return None
    else:
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j+1]
                    my_list[j+1] = temp
        return my_list[n-1]
