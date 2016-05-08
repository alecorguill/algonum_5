from cubic_spline_interpolation import *
from airfoil_file import *
import length_spline as l
import simpson as s

plt.gca().set_autoscale_on(False)

(ex, ey, ix, iy) = load_foil("../HOR20.dat")

e_n = len(ex)
i_n = len(ix)

e_f = cubic_spline_interpolate_f(ex, ey, e_n, 1e30, 1e30)
i_f = cubic_spline_interpolate_f(ix, iy, i_n, 1e30, 1e30)

print l.length_spline(e_f, s.simpson, 0, 1)
print l.length_spline(i_f, s.simpson, 0, 1)
