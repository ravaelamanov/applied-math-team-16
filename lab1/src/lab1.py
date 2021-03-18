import math
from sample_functions import *
from methods import *

a = -2
b = 2
e = 1e-10
given = (task_func, a, b, e)

print(f"Dichotomy, epsilon = {given[3]}: {dichotomy(*given)}\n")
print(f"Golden ratio, epsilon = {given[3]}: {golden_ratio(*given)}\n")
print(f"Fibonacci, epsilon = {given[3]}: {fibonacci(*given)}\n")
print(f"Parabolic, epsilon = {given[3]}: {parabolic(*given)}\n")
print(f"Brent, epsilon = {given[3]}: {brent(*given)}\n")

