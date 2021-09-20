import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

s0 = 100
u = math.exp(0.2*math.sqrt(1/52)) #sigma=0.2
n=3
k = 0.005
p1=0.3
p2=1-p1

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

def kappa(y):
    return (p1*math.exp(-1*(beta1+alpha1*y)))/((p1*math.exp(-1*(beta1+alpha1*y))+(p2*math.exp(-1*(beta2+alpha2*y)))))

def qmin(x,a1,a2,b1,b2):
    if x >= b1 and x <= b2:
        return (x-b2)/(b1-b2)
    elif x > a2 and x <= a1:
        return (x-a2)/(a1-a2)
    else:
        return 0

def uF(i,j,k,a1,a2,b1,b2):
    if (i == k == 1) and (j==1 or j==2):
        return b2
    elif (i == 1) and (j==1 or j==2) and (k==2):
        return a1
    elif (i == 2 ) and (j == 1 or j == 2) and (k == 1):
        return a2
    elif (i == k == 2) and (j==1 or j==2):
        return b1

def qmax(x,a1,a2,b1,b2):
    if x >= b2 and x < b1:
        return (x-b2)/(b1-b2)
    elif x > a1 and x <= a2:
        return (x-a2)/(a1-a2)
    else:
        return 1

def bigZ(b1,a1,b2,a2,gamma):
    return np.linspace(max(b1,invPsi(x,gamma,a2)),min(a1,invPsi(x,gamma,b2)),num=100)

def psi(x,gamma,z):
    return (x-gamma*z)/(1-gamma)
def invPsi(x,gamma,z):
    return (x-(1-gamma)*z)/gamma

def htilder(x,z,gamma,alpha1,alpha2,beta1,beta2,a1):
    #prop 4.16
    return (alpha1-alpha2)*gamma*z+alpha2*x + gamma*beta1 +(1-gamma)*beta2
    #return gamma*((alpha1-alpha2)*z+(beta1-beta2)) +alpha1*(x-z) + alpha2*z+beta2+g1(gamma)+g2(1-gamma) 

def minhTilder(x,a1,a2,b1,b2,alpha1,alpha2,beta1,beta2, i,j):
    #4.82
    G = []
    H = []
    Q = [y for y in np.linspace(qmin(x,a1,a2,b1,b2),qmax(x,a1,a2,b1,b2)) if y!=0 or y!=1]
    
    if (i==1 or i==2) and (j==1 or j==2):
        G.append(Gamma(kappa(uF(i,j,1,a1,a2,b1,b2)),Q))
        G.append(Gamma(kappa(uF(i,j,2,a1,a2,b1,b2)),Q))
        for gamma in G:
            z = max(bigZ(b1,a1,b2,a2,gamma))
            H.append(htilder(x,z,gamma,alpha1,alpha2,beta1,beta2,a1))          
    elif j==3:
        G.append(Gamma(kappa(a1),Q))
        G.append(Gamma(kappa(a2),Q))
    else:
        G.append(Gamma(kappa(0),np.linspace(qmin(x,a1,a2,b1,b2),qmax(x,a1,a2,b1,b2))))
        for gamma in G:
            z = min(bigZ(b1,a1,b2,a2,gamma))
            H.append(htilder(x,z,gamma,alpha1,alpha2,beta1,beta2,a1))    

    return min(H)

def fmin(x, alpha1,alpha2,beta1,beta2,a1,a2,b1,b2,i,j):
    f1 = (alpha1*x)+beta1 + g1(1)
    f2 = (alpha2*x)+beta2 + g2(1)
    f3 = minhTilder(x,a1,a2,b1,b2,alpha1,alpha2,beta1,beta2,i,j) 
    return min(f1,f2,f3)

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
interval = np.linspace(node_domain(n,n+1)[1], node_domain(n,0)[0])
for x in interval:
    for o in j3s:
        if (x>=o[0]) and (x<=o[1]):
            xVals.append(x)
            jVals.append(100-x)
        else:
            continue

#Generalisation: All cases for C

def alphaCase(alpha1, alpha2, a1,a2,b1,b2):
    '''
    Returns C case as defined on page 107 of the thesis.
    '''
    if (alpha1 < alpha2):
        if a1 < b2:
            return [1,1]
        elif (a1 > b2):
            return [1,2]
        elif (a1 == b2):
            return [1,3]
    elif alpha1 > alpha2:
        if b1 < a2:
            return [2,1]
        elif b1 > a2:
            return [2,2]
        elif b1 == a2:
            return [2,3]
    else:
        return [0,0]   

#METHOD FOR ALL OF LAYER 2
#WHY ARENT THEY CURVING??!


layer2Vals = [[] for x in range(0,3)]

layer = 2
for node in range(0,layer+1):
        for x in linspace(node_domain(layer,node)[0],node_domain(layer,node)[1],num=100):
            beta1 = 100-j3s[node][0]
            beta2 = 100-j3s[node+1][0]
            
            alpha1 = ((100-j3s[node][1])-(100-j3s[node][0]))/(j3s[node][1]-j3s[node][0])
            alpha2 = ((100-j3s[node+1][1])-(100-j3s[node+1][0]))/(j3s[node+1][1]-j3s[node+1][0])
            
            i = alphaCase(alpha1,alpha2,node_domain(layer+1,node)[0],node_domain(layer+1,node+1)[0],node_domain(layer+1,node)[1],node_domain(layer+1,node+1)[1])[0]
            j = alphaCase(alpha1,alpha2,node_domain(layer+1,node)[0],node_domain(layer+1,node+1)[0],node_domain(layer+1,node)[1],node_domain(layer+1,node+1)[1])[1]
            layer2Vals[node].append(fmin(x,alpha1,alpha2,beta1,beta2,node_domain(layer+1,node)[0],node_domain(layer+1,node+1)[0],node_domain(layer+1,node)[1],node_domain(layer+1,node+1)[1],i,j))
        plt.plot(np.linspace(node_domain(layer,node)[0],node_domain(layer,node)[1],num=100),layer2Vals[node],label=("Node"+str(node)))

plt.legend(loc="lower left")
plt.xlabel('x')
plt.ylabel('f(x)')
#plt.show()   

layer1Vals = [[] for x in range(0,2)]

layer = 1
for node in range(0,layer+1):
        for x in linspace(node_domain(layer,node)[0],node_domain(layer,node)[1]):
            beta1 = layer2Vals[node][0]
            beta2 = layer2Vals[node+1][0]

            alpha1 = ((-layer2Vals[node][1])+layer2Vals[node][0])/(layer2Vals[node][1]-layer2Vals[node][0])
            alpha2 = ((-layer2Vals[node+1][1])+layer2Vals[node+1][0])/(layer2Vals[node+1][1]-layer2Vals[node+1][0])
            
            i = alphaCase(alpha1,alpha2,node_domain(layer+1,node)[0],node_domain(layer+1,node+1)[0],node_domain(layer+1,node)[1],node_domain(layer+1,node+1)[1])[0]
            j = alphaCase(alpha1,alpha2,node_domain(layer+1,node)[0],node_domain(layer+1,node+1)[0],node_domain(layer+1,node)[1],node_domain(layer+1,node+1)[1])[1]

            layer1Vals[node].append(fmin(x,alpha1,alpha2,beta1,beta2,node_domain(layer+1,node)[0],node_domain(layer+1,node+1)[0],node_domain(layer+1,node)[1],node_domain(layer+1,node+1)[1],i,j))
        plt.plot(linspace(node_domain(layer,node)[0],node_domain(layer,node)[1]),layer1Vals[node],label=("Node"+str(node)))

plt.title("f(x) calculated for each node in layer 1")
plt.legend(loc="lower left")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()