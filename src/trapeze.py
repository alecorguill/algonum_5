import numpy as np

def trapeze(f ,a ,b ,n):
	"""
	Calcule l'aire sous la courbe d'une fonction avec un intervalle donné
	en utilisant la méthode des trapèzes
	:param f: fonction
	:param a: début de l'intervalle
	:param b: fin de l'intervalle
	:return: aire sous la courbe
	"""

	res = 0.0
	for i in np.arange(a,b,n):
		res += ((f(i) + f(i+n))/2)*n

	return res
