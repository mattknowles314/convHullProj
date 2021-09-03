import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

s0 = 100
u = math.exp(0.2*math.sqrt(1/52)) #sigma=0.2
n=4
k = 0.005

#Can use np.argmin for Theorem 4.27

def node_domain(layer, node):
    p = s0*(u**(layer-(2*node)))
    bid = (1-k)*p
    ask = (1+k)*p
    return bid, ask

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

print(jVals)

'''
layer = n-1
while layer >= 1:
    print("T = ",layer)
    for node in range(0,layer+1): #layer+2 because of the way range() works
        print("NODE = ",node, "| BID = ",node_domain(layer,node)[0], "| ASK = ",node_domain(layer,node)[1])
    layer-=1
'''