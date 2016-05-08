# coding=utf8

import derivation as d
import simpson as s
from math import *
import numpy as np


def length_spline(f, f_integr, begin, end):
    """
    Calcule la longueur de la courbe d'une fonction sur un intervalle donné
    :param f: fonction dont on évalue la longueur de la courbe
    :param f_integr: fonction d'intégration
    :param begin: début de l'intervalle
    :param end: fin de l'intervalle
    :return: la longueur de la courbe
    """
    def g(x):
        return sqrt(1 + pow(d.derivate(f)(x), 2))

    return f_integr(g, begin, end)

def semi_cercle(x):
    return np.sqrt(1-x**2)


#print length_spline(semi_cercle,s.simpson, -1, 1-1e-8)
