import pytest
from lab1.src.methods import *
from lab1.src.sample_functions import *


method_list = [dichotomy, golden_ratio, fibonacci, parabolic, brent]

e = [1e-7]
f = [multimodal1]
a = [-10]
b = [10]
x0 = [[1.0, 3.0]]


@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e)
@pytest.mark.parametrize("x0", x0)
@pytest.mark.parametrize("method", method_list)
@pytest.mark.timeout(3)
def test_multimodal1(f, a, b, e, x0, method):
    output = method(f, a, b, e)
    assert any(abs(x - output[0]) <= e for x in x0)


e = [1e-1]
f = [multimodal2]
a = [-2]
b = [2]
x0 = [[-1.443, 2.72]]


@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e)
@pytest.mark.parametrize("x0", x0)
@pytest.mark.parametrize("method", method_list)
@pytest.mark.timeout(3)
def test_multimodal2(f, a, b, e, x0, method):
    output = method(f, a, b, e)
    assert any(abs(x - output[0]) <= e for x in x0)


e = [1e-5]
f = [multimodal3]
a = [1]
b = [5]
x0 = [[2.26106, 4.35546]]


@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e)
@pytest.mark.parametrize("x0", x0)
@pytest.mark.parametrize("method", method_list)
@pytest.mark.timeout(3)
def test_multimodal3(f, a, b, e, x0, method):
    output = method(f, a, b, e)
    assert any(abs(x - output[0]) <= e for x in x0)
