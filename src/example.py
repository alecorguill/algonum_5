# coding=utf8

from airfoil_file import *
from linear_interp import *
from cubic_spline_interpolation import *


def cube(x):
    return x * x * x

x_s = np.linspace(0, 20, 4)
y_s = [cube(x) for x in x_s]

l_f = linear_interp(x_s, y_s)
c_f = cubic_spline_interpolate_f(x_s, y_s, 4, 1e30, 1e30)

nx_s = np.linspace(0, 20, 100)
ly_s = [l_f(nx) for nx in nx_s]
cy_s = [c_f(nx) for nx in nx_s]

plt.subplot(121)
plt.plot(x_s, y_s, 'o')
plt.plot(nx_s, ly_s, '-')
plt.title("Linear interpolation")

plt.subplot(122)
plt.plot(x_s, y_s, 'o')
plt.plot(nx_s, cy_s, '-')
plt.title("Cubic Spline interpolation")

plt.show()