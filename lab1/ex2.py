#!/usr/bin/python3


def calculate(first, second, operation):
    return operation(first, second)


a = 12
b = 6

print(calculate(a, b, lambda x, y: x + y))
print(calculate(a, b, lambda x, y: x - y))
print(calculate(a, b, lambda x, y: x * y))
print(calculate(a, b, lambda x, y: x / y))
