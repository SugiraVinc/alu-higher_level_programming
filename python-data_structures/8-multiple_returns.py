#!/usr/bin/python3
def multiple_returns(sentence):
    val =[]
    length = len(sentence)
    if length < 1:
        val.append(length)
        val.append("None")
    else:
        val.append(length)
        val.append(sentence[0])
    last_char = tuple(val)
    return last_char
