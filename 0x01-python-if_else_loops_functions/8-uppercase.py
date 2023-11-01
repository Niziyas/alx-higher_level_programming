#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:  # ASCII values for lowercase letters a-z
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(char), end='')
    print()
