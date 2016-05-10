import numpy as np

def trapeze(f ,a ,b ,n):

	res = 0.0
	for i in np.arange(a,b,n):
		res += ((f(i) + f(i+n))/2)*n

	return n

def fctn(x):

	return x**2 + 5*x - 2

print trapeze(fctn,0,10,0.01);
