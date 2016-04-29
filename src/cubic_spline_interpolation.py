import numpy as np
import math

def spline(x,y,n,yp1,ypn):
	"""Given array sx[1..n] and y[1..n] containing a tabulated function, i.e.,yi=f(xi),with x1<x2<...<xN, and given values
	yp1 and ypn for the first derivative of the interpolatingfunction at points 1 andn, respectively, this routine returns
	an array y2[1..n] that contains the second derivatives of the interpolating function at the tabulated points xi.
	If yp1 and/or ypn are equal to 1×10^30 or larger, the routine is signaled to set the corresponding boundarycondition for
	a natural spline, with zero second derivative on that boundary."""
	p=0.0
	qn=0.0
	sig=0.0
	un=0.0

	u=np.zeros(n-1,np.float)
	y2=np.zeros(n-1,np.float)

	if (yp1 > 0.99*(10**30)):
		y2[1]=u[1]=0.0
	else
		y2[1] = -0.5
		u[1]=(3.0/(x[2]-x[1]))*((y[2]-y[1])/(x[2]-x[1])-yp1)
	
	for i in range(2,n-1):
		sig=(x[i]-x[i-1])/(x[i+1]-x[i-1])
		p=sig*y2[i-1]+2.0
		y2[i]=(sig-1.0)/p
		u[i]=(y[i+1]-y[i])/(x[i+1]-x[i]) - (y[i]-y[i-1])/(x[i]-x[i-1])
		u[i]=(6.0*u[i]/(x[i+1]-x[i-1])-sig*u[i-1])/p
	
	if (ypn > 0.99*(10**30)):
		qn=un=0.0
	else 
		qn=0.5
		un=(3.0/(x[n]-x[n-1]))*(ypn-(y[n]-y[n-1])/(x[n]-x[n-1]))
	
	y2[n]=(un-qn*u[n-1])/(qn*y2[n-1]+1.0)

	for k in range(n-1,1,-1):
		y2[k]=y2[k]*y2[k+1]+u[k]

	return y2
