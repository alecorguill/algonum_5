import numpy as np
import matplotlib.pyplot as plt



def lagrange_i(tab_x,i):
    """
    :param tab_x: array containing all abscissa values
    :param i:
    :return: Polynomial number i of Lagrange given all x values.
    """
    def f(x):
        res=1
        for k in range(len(tab_x)):
            if(k != i):
                res *= (x-tab_x[k]) / (tab_x[i]-tab_x[k])
        return res
    return f



def lagrange(f,b,e,l):
    """
    :param f: function
    :param b: the lower bound of the interval
    :param e: the upper bound of the interval
    :param l: number of subdivisions
    :return: The interpolation of f in the interval [b,e], given the number of
    subdivisions l this interval is divided into.
    """
    tab_x=np.linspace(b,e,l)
    def g(x):
        res=0
        for i in range(l):
            res += f(tab_x[i])*lagrange_i(tab_x,i)
        return res
    return f
f_1 = lagrange(np.exp,0,10,100000)
tab_x = np.arange(0,10,0.1)
tab_y = [f_1(x) for x in tab_x]
print(tab_y)
plt.plot(tab_x,tab_y)
plt.show()

