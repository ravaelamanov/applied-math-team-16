import pytest
from lab1.src.methods import *
from lab1.src.sample_functions import *

e_list = [1e-20]
f = [multimodal1]
a = [-10]
b = [10]
x0 = [[1, 3]]
method_list = [dichotomy, golden_ratio, fibonacci, parabolic, brent]


@pytest.mark.parametrize("f", f)
@pytest.mark.parametrize("a", a)
@pytest.mark.parametrize("b", b)
@pytest.mark.parametrize("e", e_list)
@pytest.mark.parametrize("x0", x0)
@pytest.mark.parametrize("method", method_list)
@pytest.mark.timeout(3)
def test_multimodal1(f, a, b, e, x0, method):
    output = method(f, a, b, e)
    assert any(x + e > output[0] or x - e < output[0] for x in x0)
