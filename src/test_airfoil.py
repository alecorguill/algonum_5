# coding=utf8

import length_spline as ls
import cubic_spline_interpolation as csi
import airfoil_file as af
import numpy as np
import matplotlib.pyplot as plt;


ex, ey, ix, iy = af.load_foil('../HOR20.dat')

e_n = len(ex)
i_n = len(ix)

e_f = csi.cubic_spline_interpolate_f(ex, ey, e_n, 1e30, 1e30)
i_f = csi.cubic_spline_interpolate_f(ix, iy, i_n, 1e30, 1e30)


def curve_above(f, l, h):
    def c(x):
        return (1 - l) * f(x) + l * 3 * h
    return c


def curve_below(f, l, h):
    def c(x):
        return (1 - l) * f(x) - l * 3 * h
    return c

c_e = [curve_above(e_f, i, 0.1) for i in np.arange(0, 1, 0.075)]
c_i = [curve_below(i_f, i, 0.05) for i in np.arange(0, 1, 0.15)]

for c_ei in c_e:
    c_x = np.linspace(0, 1, 200)
    c_y = [c_ei(i) for i in c_x]
    plt.plot(c_x, c_y, 'k-')

for c_ii in c_i:
    c_x = np.linspace(0, 1, 200)
    c_y = [c_ii(i) for i in c_x]
    plt.plot(c_x, c_y, 'k-')

x_e = np.linspace(0, 1, 200)
x_i = np.linspace(0, 1, 200)
y_e = [e_f(x_ei) for x_ei in x_e]
y_i = [i_f(x_ii) for x_ii in x_i]
plt.plot(x_e, y_e, 'r-', x_i, y_i, 'r-')

plt.show()
