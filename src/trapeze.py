import numpy as np

def trapeze(f ,a ,b ,n):

	res = 0.0
	for i in np.arange(a,b,n):
		res += ((f(i) + f(i+n))/2)*n

	return res
