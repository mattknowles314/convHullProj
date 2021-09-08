import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import random
from numpy.core.function_base import linspace

s0 = 100
u = math.exp(0.2*math.sqrt(1/52)) #sigma=0.2
n=4
k = 0.005
p1=0.5
p2=1-p1
z = random.uniform(0,100)
alpha1 = 1
alpha2 = 1


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

def Gamma(y, I):
    if y in I:
        return y
    elif y < min(I):
        return min(I)
    elif y > max(I):
        return max(I)

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

def fmin(x, alpha1,alpha2,beta1,beta2,a1,a2,b1,b2,z):
    f1 = (alpha1*x)+beta1 + g1(1)
    f2 = (alpha2*x)+beta2 + g2(1)
    f3 = minhTilder(x,a1,a2,b1,b2,z,alpha1,alpha2,beta1,beta2) 
    return min(f1,f2,f3)

#4.44

'''
layer = n-1
while layer >= 1:
    print("T = ",layer)
    for node in range(0,layer+1):
        print("NODE = ",node, "| BID = ",node_domain(layer,node)[0], "| ASK = ",node_domain(layer,node)[1])
    layer-=1
'''

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

#How do we tie this all together then??

'''
#METHOD FOR THE UPPER 2ND LAYER NODE!!
b1 = node_domain(3,0)[0]
a1 = node_domain(3,0)[1]
b2 = node_domain(3,1)[0]
a2 = node_domain(3,1)[1]

f2 = []
for x in linspace(node_domain(2,0)[0],node_domain(2,0)[1]):
    f2.append(fmin(x,alpha1,alpha2,beta1,beta2,a1,a2,b1,b2,z))

plt.plot(linspace(node_domain(2,0)[0],node_domain(2,0)[1]),f2)
plt.xlabel("Bid-Ask Interval")
plt.ylabel("f(x)")
plt.show()
'''

#METHOD FOR ALL OF LAYER 2
layer2Vals = [[] for x in range(0,3)]

layer =2
for node in range(0,layer+1):
        print("NODE = ",node, "| BID = ",node_domain(layer,node)[0], "| ASK = ",node_domain(layer,node)[1])
        for x in linspace(node_domain(layer,node)[0],node_domain(layer,node)[1]):
            beta1 = 100-j3s[node][0]
            beta2 = 100-j3s[node][1]
            layer2Vals[node].append(fmin(x,alpha1,alpha2,beta1,beta2,node_domain(layer+1,node)[0],node_domain(layer+1,node+1)[0],node_domain(layer+1,node)[1],node_domain(layer+1,node+1)[1],z))
        plt.plot(linspace(node_domain(layer,node)[0],node_domain(layer,node)[1]),layer2Vals[node],label=("Node"+str(node)))
plt.title("f(x) calculated for each node in layer 2")
plt.legend(loc="upper left")
plt.xlabel('Bid-Ask Intervals')
plt.ylabel('f(x)')
plt.show()