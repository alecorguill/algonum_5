import numpy as np
import matplotlib.pyplot as plt

def f_lambda(l,f,h_max):
    return lambda x: (1-l)*f(x)+l*3*h_max


def airflow(f_top,f_below,n,h_max,h_min):
    x=np.linspace(0,1,100)
    y=[f_top(i) for i in x]
    plt.plot(x,y)
    for i in range(n+1):
        plt.plot(x,[f_lambda(i*1.0/n,f_top,h_max)(j) for j in x])
        plt.plot(x,[f_below(i) for i in x])
    for i in range(n+1):
        plt.plot(x,[f_lambda(i*1.0/n,f_below,h_min)(j) for j in x])
    plt.show()

def air(x):
    return -1.0/5*x*(x-1)

def down(x):
    return 1.0/10*x*(x-1)

airflow(air,down,10,0.1,-0.01)
