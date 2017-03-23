#searching for a function minimum interval with fibonacci method
from math import sqrt


def fibonacci(func, start, end, n):
    for i in range(n):
        l_i = start + (fibonacci_number(n - i - 1) / fibonacci_number(n - i + 1)) * (end - start)
        u_i = start + (fibonacci_number(n - i) / fibonacci_number(n - i + 1)) * (end - start)
        if func(l_i) > func(u_i):
            start = l_i
        else:
            end = u_i
    return [start, end]

def fibonacci_number(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
