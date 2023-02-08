#!/usr/bin/python3
''' module My list '''

class Mylist(list):
    ''' class Mylist '''

    def print_sorted(self):
        ''' prints the list, but sorted (ascending sort) '''
        print(sorted(self))
