import numpy as np

def rectangle(f,a,b,n):
    res=0
    for i in np.arange(a,b,n):
        res=res+n*f(i)
    return res

"""def f(x):
    return x*x+5*x-2

print(rectangle(f,0,10,0.01))"""

