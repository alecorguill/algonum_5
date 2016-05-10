import numpy as np
import math as ma
from scipy import misc

#Rectangle Method
def rectangle(f,a,b,n):
  result = 0
  for k in range(n):
    result = result + f(a+k*(b-a)*1.0/n)
  result = result*(b-a)*1.0/n
  return result

"""def f(x):
  return x*x


print(rectangle(f,0,1,10000))"""

#Middle Point Method
