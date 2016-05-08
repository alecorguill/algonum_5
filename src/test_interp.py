# coding=utf8

from cubic_spline_interpolation import *
from airfoil_file import *

plt.gca().set_autoscale_on(False)

(ex, ey, ix, iy) = load_foil("../goe144.dat")

e_n = len(ex)
i_n = len(ix)

e_f = cubic_spline_interpolate_f(ex, ey, e_n, 1e30, 1e30)
i_f = cubic_spline_interpolate_f(ix, iy, i_n, 1e30, 1e30)

ex2 = np.linspace(ex[0], ex[e_n - 1], 10 * e_n)
ey2 = [e_f(x) for x in ex2]
ix2 = np.linspace(ix[0], ix[i_n - 1], 10 * i_n)
iy2 = [i_f(x) for x in ix2]

plt.plot(ex, ey, 'o', ix, iy, 'o', ex2, ey2, '-', ix2, iy2, '-')

plt.xlim([0.0, 1.0])
plt.ylim([-0.02, 0.1])
plt.show()
