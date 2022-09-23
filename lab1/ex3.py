#!/usr/bin/python3

a = 12
b = 6


def compare(first, second):
    if first < second:
        return -1
    if first == second:
        return 0
    if first > second:
        return 1


print(compare(a, b))
