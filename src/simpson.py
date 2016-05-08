# coding=utf8

import numpy as np


def simpson_div(f, a, b):
    """
    Calcule l'aire sous la courbe d'une fonction et d'un intervalle donnés
    :param f: fonction
    :param a: début de l'intervalle
    :param b: fin de l'intervalle
    :return: aire sous la courbe
    """
    d = b - a
    x_val = np.linspace(a, b, 4)
    y_val = [f(x) for x in x_val]
    return (d / 8.) * (y_val[0] + 3 * y_val[1] + 3 * y_val[2] + y_val[3])


def simpson(f, a, b):
    """

    :param f:
    :param a:
    :param b:
    :return:
    """
    n = 10000
    s = 0.
    l = 1.0 * (b - a) / n
    for i in range(0, n - 1):
        s += simpson_div(f, l * i, l * (i + 1))
    return s

# print simpson(lambda x: 2, 0, 4)
