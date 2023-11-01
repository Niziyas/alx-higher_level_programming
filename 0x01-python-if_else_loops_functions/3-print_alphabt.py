#!/usr/bin/python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end='')
