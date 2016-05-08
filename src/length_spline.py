# coding=utf8

import derivation as d
import simpson as s
from math import *



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


#print length_spline(, s.simpson, 0, 1)
