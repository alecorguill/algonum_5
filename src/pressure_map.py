# coding=utf8

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import airfoil_file as af
import cubic_spline_interpolation as csi
import length_spline as ls
import simpson as s


def curve_above(f, l, h):
    def c(x):
        return (1 - l) * f(x) + l * 3 * h
    return c


def curve_below(f, l, h):
    def c(x):
        return (1 - l) * f(x) - l * 3 * h
    return c


def spline_array(i_f, e_f):
    c_i = [curve_below(i_f, i, 0.05) for i in np.arange(0, 1, 0.02)]
    c_e = [curve_above(e_f, i, 0.1) for i in np.arange(0, 1, 0.01)]
    return c_i, c_e


def spline_length_array(sps):
    return [ls.length_spline(sps[i], s.simpson, 0, 1, 2000) for i in range(0, len(sps))]


def pixel_val_e(x, y, sps, sps_l):
    n = len(sps)
    i = 0

    while i < n and y > sps[i](x):
        i += 1

    if i == n:
        return 1
    else:
        return sps_l[i]


def pixel_val_i(x, y, sps, sps_l):
    n = len(sps)
    i = 0

    while i < n and y < sps[i](x):
        i += 1

    if i == n:
        return 1
    else:
        return sps_l[i]


def pressure_map(n):
    m = np.zeros((n, n))
    dy = 0.4

    ex, ey, ix, iy = af.load_foil('../HOR20.dat')

    e_n = len(ex)
    i_n = len(ix)

    e_f = csi.cubic_spline_interpolate_f(ex, ey, e_n, 1e30, 1e30)
    i_f = csi.cubic_spline_interpolate_f(ix, iy, i_n, 1e30, 1e30)

    c_i, c_e = spline_array(i_f, e_f)

    c_il = spline_length_array(c_i)
    c_el = spline_length_array(c_e)

    for i in range(0, n):
        xi = float(i) / n

        for j in range(0, n):
            yi = float(j) / n - dy

            if yi > e_f(xi):
                m[n - j - 1, i] = pixel_val_e(xi, yi, c_e, c_el)
            elif yi < i_f(xi):
                m[n - j - 1, i] = pixel_val_i(xi, yi, c_i, c_il)
            else:
                m[n - j - 1, i] = 1

    plt.imshow(m, cmap='hot')
    plt.show()

pressure_map(100)
