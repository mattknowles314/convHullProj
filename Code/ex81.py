from xuFuncs import *
import math
import random
import matplotlib.pyplot as plt
from rouxHull import *

#Define constants
T = 52
n = 20
alpha = 0,1
k = 0.005
I = [x for x in range(0,(T+1))]
sig = 0.2
p = 0.45
Sv = []
f = round((1/52)**0.5,12)

bid = []
ask = []

#Stock price function
def S(sigma, sVal, p):
	prob = random.uniform(0,1)
	if prob <= p:
		return sVal*math.exp(sigma*math.sqrt(1/52))
	else:
		return sVal*math.exp(-1*sigma*math.sqrt(1/52))

for i in I:
	if i == 0:
		Sv.append(100)
		bid.append(100)
		ask.append(100)
	else:
		Sv.append(S(sig, Sv[i-1], p))
		bid.append(round((1+k)*Sv[i-1],12))
		ask.append(round((1-k)*Sv[i-1],12))

plt.plot(I, Sv)
plt.plot(I, bid, "--r")
plt.plot(I, ask, ":g")
plt.show()
