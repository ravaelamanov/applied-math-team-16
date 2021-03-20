import math


def task_func(x):
    return math.exp(math.sin(x)) * x ** 2


def func_1(x):
    return x ** 2 + 2 * x


def multimodal1(x):
    return x ** 4 - 8 * x ** 3 + 22 * x ** 2 - 24 * x + 1


def multimodal2(x):
    return math.sin(x) + math.cos(math.sqrt(2) * x) + math.sin(math.sqrt(3) * x)


def multimodal3(x):
    return 2 + math.cos(x) + math.cos(2 * x - 1 / 2) / 2
