# coding=utf8

import numpy as np


def cubic_spline_interpolate_f(xa, ya, n, yp1, ypn):
    ya2 = spline(xa, ya, n, yp1, ypn)

    def f(x):
        return splint(xa, ya, ya2, n, x)
    return f


def spline(x, y, n, yp1, ypn):
    """
    Given array sx[1..n] and y[1..n] containing a tabulated function, i.e.,yi=f(xi),with x1<x2<...<xN, and given values
    yp1 and ypn for the first derivative of the interpolating function at points 1 and n, respectively, this routine
    returns an array y2[1..n] that contains the second derivatives of the interpolating function at the tabulated points
    xi. If yp1 and/or ypn are equal to 1×10^30 or larger, the routine is signaled to set the corresponding
    boundary condition for a natural spline, with zero second derivative on that boundary.
    :param x:
    :param y:
    :param n:
    :param yp1:
    :param ypn:
    :return:
    """
    # p = 0.0
    # qn = 0.0
    # sig = 0.0
    # un = 0.0

    u = np.zeros(n - 1, np.float)
    y2 = np.zeros(n, np.float)

    if yp1 > 0.99 * (10 ** 30):
        y2[0] = u[0] = 0.0
    else:
        y2[0] = -0.5
        u[0] = (3.0 / (x[1] - x[0])) * ((y[1] - y[0]) / (x[1] - x[0]) - yp1)

    for i in range(1, n - 1):
        sig = (x[i] - x[i - 1]) / (x[i + 1] - x[i - 1])
        p = sig * y2[i - 1] + 2.0
        y2[i] = (sig - 1.0) / p
        u[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i]) - (y[i] - y[i - 1]) / (x[i] - x[i - 1])
        u[i] = (6.0 * u[i] / (x[i + 1] - x[i - 1]) - sig * u[i - 1]) / p

    if ypn > 0.99 * (10 ** 30):
        qn = un = 0.0
    else:
        qn = 0.5
        un = (3.0 / (x[n - 1] - x[n - 2])) * (ypn - (y[n - 1] - y[n - 2]) / (x[n - 1] - x[n - 2]))

    y2[n - 1] = (un - qn * u[n - 2]) / (qn * y2[n - 2] + 1.0)

    for k in range(n - 2, 0, -1):
        y2[k] = y2[k] * y2[k + 1] + u[k]

    return y2


def splint(xa, ya, ya2, n, x):
    """
    Given the array xa and ya, which tabulate a function and given the array ya2, which is the output from spline above
    Given a value of x
    Returns a cubic-spline interpolated value y
    :param xa:
    :param ya:
    :param ya2:
    :param n:
    :param x:
    :return:
    """

    klo = 0
    khi = n - 1
    while khi - klo > 1:
        k = (khi + klo) >> 1
        if xa[k] > x:
            khi = k
        else:
            klo = k
    h = xa[khi] - xa[klo]
    if h == 0.0:
        print "Bad xa input to routine splint"
    a = (xa[khi] - x) / h
    b = (x - xa[klo]) / h
    y = a*ya[klo] + b*ya[khi] + ((a**3 - a)*ya2[klo] + (b**3 - b)*ya2[khi])*(h**2)/6.0
    return y
