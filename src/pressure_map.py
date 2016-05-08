# coding=utf8

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import airfoil_file as af
import cubic_spline_interpolation as csi


def pressure_map(n):
    m = np.zeros((n, n))
    dy = 0.4

    ex, ey, ix, iy = af.load_foil('../HOR20.dat')

    e_n = len(ex)
    i_n = len(ix)

    e_f = csi.cubic_spline_interpolate_f(ex, ey, e_n, 1e30, 1e30)
    i_f = csi.cubic_spline_interpolate_f(ix, iy, i_n, 1e30, 1e30)

    for i in range(0, n):
        xi = float(i) / n
        for j in range(n - int((e_f(xi) + dy) * n + 1), n - int((i_f(xi) + dy) * n)):
            m[j, i] = 1.0

    plt.imshow(m, interpolation='none', cmap='hot')
    plt.show()

#pressure_map(1000)
