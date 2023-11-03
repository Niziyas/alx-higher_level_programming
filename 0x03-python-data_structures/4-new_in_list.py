#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        print(my_list)
        return my_list
new_in_list(my_list=[1, 2, 3, 4, 5],idx=3,element=9)
