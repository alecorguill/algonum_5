import numpy as np

def rectangle(f,a,b,n):
    res=0
    for i in np.arange(a,b,n):
        res=res+n*f(i)
    return res

"""def f(x):
<<<<<<< HEAD
    return x*x+5*x-2

print(rectangle(f,0,10,0.01))"""
=======
    return x

print(rectangle(f,0,1,1000))"""
>>>>>>> a74fa8eacc0ed72ef276729c3bf6622ef3b1dfd7
