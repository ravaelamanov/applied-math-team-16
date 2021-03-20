from sample_functions import *
from methods import *
import pandas as pd

a = -2
b = 2
e_list = [10**(-i) for i in range(1, 20)]
method_list = [dichotomy, golden_ratio, fibonacci, parabolic, brent]

data = {
    'Method': [],
    'iter_count': [],
    'f_count': [],
    'e': []
}

for e in e_list:
    given = (task_func, a, b, e)
    for method in method_list:
        out = method(*given)
        data['Method'].append(method.__name__)
        data['iter_count'].append(out[1])
        data['f_count'].append(out[2])
        data['e'].append(e)

df = pd.DataFrame(data)
print(df[df['e'] == 1e-5])
