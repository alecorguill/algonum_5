import numpy as np
import math as ma



def splint(xa, ya, ya2, n, x):
    """
    Given the array xa and ya, wich tabulate a function and given the array ya2, which is the output from spline above
    Given a value of x
    Returns a cubic-spline interpolated value y
    """

    klo = 1
    khi = n
    while (khi - klo > 1):
        k = (khi + klo) >> 1
        if (xa[k] > x):
            khi = k
        else:
            klo = k
    h = xa[khi] - xa[klo]
    if (h == 0.0):
        print "Bad xa input to routine splint"
    a = (xa[klo] - x) / h
    b = (x - xa[klo]) / h
    y = a*ya[klo] + b*ya[khi] + ((a**3 - a)*ya2[klo] + (b**3 - b)*ya2[khi])*(h**2)/6.0
    return y








