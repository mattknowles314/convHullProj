import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

s0 = 100
u = math.exp(0.2*math.sqrt(1/52)) #sigma=0.2
n=4
k = 0.005
p1=0.3
p2=1-p1
#Can use np.argmin for Theorem 4.27

def g1(y):
	if y >= 0:
		return y*math.log(y/p1)
	else:
		return float('inf')

def g2(y):
	if y >= 0:
		return y*math.log(y/p2)
	else:
		return float('inf')

def node_domain(layer, node):
    p = s0*(u**(layer-(2*node)))
    bid = (1-k)*p
    ask = (1+k)*p
    return bid, ask

def qmin(x,a1,a2,b1,b2):
    if x >= b1 and x <= b2:
        return (x-b2)/(b1-b2)
    elif x > a2 and x <= a1:
        return (x-a2)/(a1-a2)
    else:
        return 0

def qmax(x,a1,a2,b1,b2):
    if x >= b2 and x < b1:
        return (x-b2)/(b1-b2)
    elif x > a1 and x <= a2:
        return (x-a2)/(a1-a2)
    else:
        return 1

#Qx = Qbarx \ {0,1}

def psi(x,gamma,z):
    return (x-gamma*z)/(1-gamma)
def invPsi(x,gamma,z):
    return (x-(1-gamma)*z)/gamma

def htilder(x,z,gamma,alpha1,alpha2,beta1,beta2):
    return ((alpha1-alpha2)*gamma*z)+(alpha2*x)+(gamma*beta1)+((1-gamma)*beta2)+g1(gamma)+g2(1-gamma)

def minhTilder(x,a1,a2,b1,b2,z,alpha1,alpha2,beta1,beta2):
    H = []
    Q = [y for y in np.linspace(qmin(x,a1,a2,b1,b2),qmax(x,a1,a2,b1,b2)) if y!=0 or y!=1]
    for gamma in Q:
        H.append(htilder(x,z,gamma,alpha1,alpha2,beta1,beta2))
    return min(H)

#4.44


j3s = []
for i in range(n+1):
    j3s.append([node_domain(n,i)[0],node_domain(n,i)[1]])

xVals = []
jVals = []

interval = np.linspace(node_domain(n,0)[0],node_domain(n,n+1)[1])
for x in interval:
    for o in j3s:
        if (x>=o[0]) and (x<=o[1]):
            xVals.append(x)
            jVals.append(100-x)
        else:
            continue

'''
layer = n-1
while layer >= 1:
    print("T = ",layer)
    for node in range(0,layer+1): #layer+2 because of the way range() works
        print("NODE = ",node, "| BID = ",node_domain(layer,node)[0], "| ASK = ",node_domain(layer,node)[1])
    layer-=1
'''