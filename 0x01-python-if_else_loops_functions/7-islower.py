#!/usr/bin/python3
user_choice = input("enter a letter: ")
if user_choice.islower():
    print(f'{user_choice} is lower')
else:
    print(f'{user_choice} is upper')
