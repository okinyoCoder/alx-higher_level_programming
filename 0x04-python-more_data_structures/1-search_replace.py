#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for x in new_list:
        if x == search:
            new_list[new_list.index(search)] = replace
        new_list.append(x)
    return new_list
