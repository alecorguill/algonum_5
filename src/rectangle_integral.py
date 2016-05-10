import numpy as np

def rectangle(f,a,b,n):
    res=0
    for i in range(n):
        res=res+(b-a)*1.0/n*f(a+i*(b-a)*1.0/n)
    return res

"""def f(x):
    return x*x

print(rectangle(f,0,1,1000))"""
