#coding=utf8

import numpy as np
import matplotlib.pyplot as plt


def derivate_func(h):
    def derivate_core(f):
        def g(x):
            return (f(x + h) - f(x)) / h
        return g
    return derivate_core

derivate = derivate_func(10e-5)



'''deriv_square = derivate(lambda x: x * x)

print deriv_square(2)

x_val = np.linspace(0, 10, 100)
y_val = [deriv_square(x) for x in x_val]
plt.plot(x_val, y_val)
plt.show()'''