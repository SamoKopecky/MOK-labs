#!/usr/bin/python3

a = [13, 45, 1, -10, 273]


def sum_list(input_list):
    list_sum = 0
    while len(input_list) != 0:
        list_sum += input_list.pop()
    return list_sum


print(sum_list(a))
