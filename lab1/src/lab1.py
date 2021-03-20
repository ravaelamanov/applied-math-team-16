from sample_functions import *
from methods import *
import pandas as pd

a = -2
b = 2
e_list = [10 ** (-i) for i in range(1, 21)]
method_list = [dichotomy, golden_ratio, fibonacci, parabolic, brent]

data1 = {
    'Method': [],
    'iter_count': [],
    'f_count': [],
    'e': []
}

data2 = {
    'Method': [],
    'a': [],
    'b': [],
    'k': [],
    'e': []
}

for e in e_list:
    given = (task_func, a, b, e)
    for method in method_list:
        out = method(*given)
        data1['Method'].append(method.__name__)
        data1['iter_count'].append(out[1])
        data1['f_count'].append(out[2])
        data1['e'].append(e)

        data2['Method'].extend([method.__name__] * len(out[3]))
        a_list = [interval[0] for interval in out[3]]
        data2['a'].extend(a_list)
        b_list = [interval[1] for interval in out[3]]
        data2['b'].extend(b_list)
        k_list = [(b_list[i - 1] - a_list[i - 1]) / (b_list[i] - a_list[i]) for i in range(0, len(out[3]))]
        k_list[0] = 1
        data2['k'].extend(k_list)
        data2['e'].extend([e] * len(out[3]))

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# print(df2[(df2['e'] == 1e-10) & (df2['Method'] == 'golden_ratio')])
# print(df2[(df2['e'] == 1e-10) & (df2['Method'] == 'fibonacci')])
