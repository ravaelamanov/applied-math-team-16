import pytest
from methods import *
from sample_functions import *

e_list = [10**(-i) for i in range(1, 31)]
f = [task_func]
a = [-2]
b = [2]
x0 = [0.0]

@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e_list)
@pytest.mark.parametrize("x0", x0)
def test_dichotomy(f, a, b, e, x0):
    output = dichotomy(f, a, b, e)
    assert abs(x0 - output[0]) < e
    assert output[2] == output[1] * 2

@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e_list)
@pytest.mark.parametrize("x0", x0)
def test_golden_ratio(f, a, b, e, x0):
    output = golden_ratio(f, a, b, e)
    assert abs(x0 - output[0]) < e
    assert output[2] == output[1] + 2

@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e_list)
@pytest.mark.parametrize("x0", x0)
def test_fibonacci(f, a, b, e, x0):
    output = fibonacci(f, a, b, e)
    assert abs(x0 - output[0]) < e
    assert output[2] == output[1] + 2

@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e_list)
@pytest.mark.parametrize("x0", x0)
def test_parabolic(f, a, b, e, x0):
    output = parabolic(f, a, b, e)
    assert abs(x0 - output[0]) < e

@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e_list)
@pytest.mark.parametrize("x0", x0)
def test_brent(f, a, b, e, x0):
    output = brent(f, a, b, e)
    assert abs(x0 - output[0]) < e
