import random
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import Interval


alpha1 = random.uniform(0.0, 10.0)
alpha2 = random.uniform(0.0, 10.0)
beta1 = random.uniform(0.0, 10.0)
beta2 = random.uniform(0.0, 10.0)

def g1(y,p1):
	if y >= 0:
		return y*math.log(y/p1)
	else:
		return float('inf')

def g2(y,p2):
	if y >= 0:
		return y*math.log(y/p2)
	else:
		return float('inf')

def f1(y, alpha1, beta1):
	if y >= b1 and y <= a1:
		return alpha1*y + beta1
	else:
		return float('inf')

def f2(y, alpha2, beta2):
	if y >= b2 and y <= a2:
		alpha2*y + beta2
	else:
		return float('inf')

def domainF(a1,a2,b1,b2):
	return np.linspace(min(b1,b2), max(a1,a2))

def qmin(x,a1,a2,b1,b2):
	if x >= b1 and x < b2:
		return (x-b2)/(b1-b2)
	elif x >= b2 and x <= a2:
		return 0
	else:
		return (x-a2)/(a1-a2)

def qmax(x,a1,a2,b1,b2):
	if x >= b2 and x < b1:
		return (x-b2)/(b1-b2)
	elif x >= b1 and x <= a1:
		return 0
	else:
		return (x-a2)/(a1-a2)

def Qbar(x,a1,a2,b1,b2):
	return np.linspace(qmin(x,a1,a2,b1,b2), qmax(x,a1,a2,b1,b2))

def Qx(Qbar):
	Q = []
	for i in Qbar:
		if i > 0 and i < 1:
			Q.append(i)
	return Q

def psi(x,gamma,z):
	return (x-gamma*z)/(1-gamma)
def invPsi(x,gamma,z):
	return (x-(1-gamma)*z)/gamma

def bigZ(a1,a2,b1,b2):
	return np.linspace(max(b1, invPsi(x,gamma,a2)),min(a1,invPsi(x,gamma,b2)))

def ky(alpha1, alpha2, beta1, beta2, p1, p2, y):
	return (p1*math.exp(-1*(beta1+alpha1*y)))/(p1*math.exp(-1*beta1)+p2*math.exp(-1*beta2))

def Gamma(gamma, I):
	if gamma in I:
		return gamma
	elif gamma < min(I):
		return min(I)
	elif gamma > max(I):
		return max(I)

def hbar(g):
	return 0