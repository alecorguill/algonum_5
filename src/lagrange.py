import numpy as np
import matplotlib.pyplot as plt


def lagrange_i(tab_x, i):
    """
    :param tab_x: array containing all abscissa values
    :param i:
    :return: Polynomial number i of Lagrange given all x values.
    """
    def f(x):
        res = 1
        for k in range(len(tab_x)):
            if k != i:
                res *= (x - tab_x[k]) / (tab_x[i] - tab_x[k])
        return res
    return f


def lagrange(f, b, e, l):
    """
    :param f: function
    :param b: the lower bound of the interval
    :param e: the upper bound of the interval
    :param l: number of subdivisions
    :return: The interpolation of f in the interval [b,e], given the number of
    subdivisions l this interval is divided into.
    """
    tab_x = np.linspace(b, e, l)

    def g(x):
        res = 0
        for i in range(0, l):
            res += f(tab_x[i]) * lagrange_i(tab_x, i)(x)
        return res
    return g


def cube(x):
    return x * x * x

f_1 = lagrange(cube, 0, 10, 50)
x_val = np.linspace(0, 10, 100)
y_val = [f_1(x) for x in x_val]
plt.plot(x_val, y_val)
plt.show()

