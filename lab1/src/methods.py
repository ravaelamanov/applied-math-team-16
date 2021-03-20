import math


def dichotomy(f, a, b, e):
    delta = e / 2 - e / 5  # TODO: figure out how to choose delta (delta == e/2 requires most iterations) probably should be as min as possible
    iter_count = 0
    while b - a > e:
        iter_count += 1
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        f1 = f(x1)
        f2 = f(x2)
        if f1 < f2:
            b = x2
        elif f1 > f2:
            a = x1
        else:
            a = x1
            b = x2
        # print(a, b)
    f_count = iter_count * 2
    return a + (b - a) / 2, iter_count, f_count


# TODO: endless loop on parameters: a = -3, b = 4, e = 1e-10, f = func_1
def golden_ratio(f, a, b, e):
    k = (3 - math.sqrt(5)) / 2  # golden ration coeff

    def calc_x1(a, b):
        return a + k * (b - a)

    def calc_x2(a, b):
        return b - k * (b - a)

    iter_count = 0

    x1 = calc_x1(a, b)
    x2 = calc_x2(a, b)
    f1 = f(x1)
    f2 = f(x2)
    f_count = 2

    while b - a > e:
        iter_count += 1

        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = calc_x1(a, b)
            f1 = f(x1)
            f_count += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = calc_x2(a, b)
            f2 = f(x2)
            f_count += 1
        # print (a, b)
    return (a + b) / 2, iter_count, f_count


def fibonacci(f, a, b, e):
    def F(n):
        return round(1 / math.sqrt(5) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n))

    def find_n(a, b, e):
        n = 1
        while F(n + 2) <= (b - a) / e:
            n += 1
        return n

    def calc_x1(a, b, n, k):
        return a + F(n - k + 1) / F(n - k + 3) * (b - a)

    def calc_x2(a, b, n, k):
        return a + F(n - k + 2) / F(n - k + 3) * (b - a)

    iter_count = 0

    n = find_n(a, b, e)
    x1 = calc_x1(a, b, n, 1)
    x2 = calc_x2(a, b, n, 1)
    f1 = f(x1)
    f2 = f(x2)
    f_count = 2

    for i in range(2, n + 1):  # TODO: determine number of loops
        iter_count += 1

        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = calc_x1(a, b, n, i)
            f1 = f(x1)
            f_count += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = calc_x2(a, b, n, i)
            f2 = f(x2)
            f_count += 1
        # print (a, b)
    return a + (b - a) / 2, iter_count, f_count


def parabolic(f, a, b, e):
    def calc_u(x1, x2, x3, f1, f2, f3):  # approximating parabola minimum
        return x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / (
                    2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))

    iter_count = 0

    x1 = a
    x3 = b
    x2 = (x1 + x3) / 2  # TODO: how to choose x2 so that f1 > f2 < f3 so that x1 < u < x3
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f_count = 3

    while 1:
        iter_count += 1

        u = calc_u(x1, x2, x3, f1, f2, f3)
        if abs(u - x2) < e:
            break
        fu = f(u)
        f_count += 1

        if fu <= f2:
            if u >= x2:
                x1 = x2
                f1 = f2
            else:
                x3 = x2
                f3 = f2
            x2 = u
            f2 = fu
        else:
            if u >= x2:
                x3 = u
                f3 = fu
            else:
                x1 = u
                f1 = fu
        # print(x1, x3)
    return u, iter_count, f_count


def brent(f, a, c, eps):
    def are_different(x1, x2, x3, f1, f2, f3):
        return x1 != x2 and x1 != x3 and x2 != x3 and f1 != f2 and f1 != f3 and f2 != f3

    def calc_u(x1, x2, x3, f1, f2, f3):  # approximating parabola minimum
        return x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / (
                    2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))

    def sign(x):
        return math.copysign(1, x)

    iter_count = 0

    K = (3 - math.sqrt(5)) / 2
    x = w = v = (a + c) / 2
    fx = fw = fv = f(x)
    f_count = 1
    d = e = c - a
    u = None
    while d > eps:
        iter_count += 1
        g = e
        e = d
        if are_different(x, w, v, fx, fw, fv):
            u = calc_u(x, w, v, fx, fw, fv)
        if u is not None and a + eps <= u <= c - eps and abs(u - x) < g / 2:
            d = abs(u - x)
        else:
            if x < (c - a) / 2:
                u = x + K * (c - x)
                d = c - x
            else:
                u = x - K * (x - a)
                d = x - a
            if abs(u - x) < eps:
                u = x + sign(u - x) * eps
        fu = f(u)
        f_count += 1
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu
        # print(a, c)
    return u, iter_count, f_count
