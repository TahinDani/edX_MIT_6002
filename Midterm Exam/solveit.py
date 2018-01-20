def f(x):
    return x == 0

def g(x):
    return (x + 15)**0.5 + x**0.5 == 15

def h(x):
    return x == 100

def i(x):
    return x == 26

def j(x):
    return x**2 == 9

def k(x):
    return x == -4

def l(x):
    return x**2 + x + 0 == 0

def m(x):
    return x == -80

def n(x):
    return x == 2

def o(x):
    return [1, 2, 3][-x] == 1 and x != 0


def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    x = 0
    while True:
        if test(x):
            return x
        if test(-x):
            return -x
        x += 1

# solutions = 0, 49, 100, 26, 3, -4, 0, -80, 2, 3
functions = [f, g, h, i, j, k, l, m, n, o]
for f in functions:
    print(solveit(f))
