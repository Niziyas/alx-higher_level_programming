#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    else:
        first = sentence[0]
        length = len(sentence)
        print("Length: {:d} - First character: {}".format(length, first))
print(multiple_returns(""))
