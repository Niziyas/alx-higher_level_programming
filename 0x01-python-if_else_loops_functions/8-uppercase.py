#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()
