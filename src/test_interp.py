# coding=utf8

from cubic_spline_interpolation import *
from airfoil_file import *
from linear_interp import *

plt.gca().set_autoscale_on(False)

(ex, ey, ix, iy) = load_foil("../HOR20.dat")

e_n = len(ex)
i_n = len(ix)

e_f = cubic_spline_interpolate_f(ex, ey, e_n, 1e30, 1e30)
i_f = cubic_spline_interpolate_f(ix, iy, i_n, 1e30, 1e30)

# e_f = linear_interp(ex, ey)
# i_f = linear_interp(ix, iy)

ex2 = np.linspace(ex[0], ex[e_n - 1], 5 * e_n)
ey2 = [e_f(x) for x in ex2]
ix2 = np.linspace(ix[0], ix[i_n - 1], 5 * i_n)
iy2 = [i_f(x) for x in ix2]

# p1, = plt.plot(ex, ey, 'o')
p1, = plt.plot(ex2, ey2, '-')
# p2, = plt.plot(ix, iy, 'o')
p2, = plt.plot(ix2, iy2, '-')

plt.xlim([0.0, 1.0])
plt.ylim([-0.2, 0.4])
plt.legend([p1, p2], ["extrados", "intrados"])
plt.title("Interpolated airfold curve")
plt.show()
