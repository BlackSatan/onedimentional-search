from swenn import swenn
from dichotomy import dichotomy
from fibonacci import fibonacci

A = 7
X0 = 5.5
E = 0.2
DELTA = 0.1


def o_my_work_function(x):
    return x**2 - A * x

interval = swenn(o_my_work_function, X0, DELTA)

print('result swen', interval)

print('result dichotomy', dichotomy(o_my_work_function, interval[0], interval[1], E))

print('result fibonacci', fibonacci(o_my_work_function, interval[0], interval[1], 15))


