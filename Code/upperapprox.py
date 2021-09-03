from matplotlib import interactive, rcParams
from numpy import *
import math
import csv
import matplotlib.pyplot as plt
from sympy import Interval
from rouxHull import *

#Define constants
T = 52
n = 150
l = n-1
alpha = 0.1
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
		bid.append(round((1-k)*Sv[i-1],12))
		ask.append(round((1+k)*Sv[i-1],12))

intervals = [[] for x in range(len(bid))]
upperApprox = []

for i in range(len(bid)):
	j = 1
	Q = ask[i]-bid[i]
	while j <= n:
		s = bid[i] + (j-1)*Q/(l)
		intervals[i].append(s)
		j+=1

def fhat(x, interval):
	if x in interval:
		return x
	else:
		kl = max(interval, key=lambda y:abs(y-x))
		kp = min(interval, key=lambda y:abs(y-x))
		a = (kl-x)/(kl-kp)
		b = (x-kp)/(kl-kp)
		return a*fhat(kp, interval)+b*fhat(kl, interval)

for j in range(0,len(intervals)):
	for x in linspace(bid[j], ask[j]):
		upperApprox.append(fhat(x, intervals[j]))
	
T = []
for i in range(0,len(upperApprox)):
	x = [i, upperApprox[i]]
	T.append(x)

hull = roux_conv_hull(T)

for i in hull:
	x = i[0]
	y = i[1]
	row = x,y
	csvF = open("hull.csv", "a")
	writer = csv.writer(csvF)
	writer.writerow(row)
	csvF.close()

plt.plot(I, Sv, label="Stock Price")
plt.plot(I, bid, "--r", label="Bid Price")
plt.plot(I, ask, ":g", label="Ask Price")
plt.xlabel("t")
plt.ylabel("Price")
plt.legend(loc="upper right")
plt.show()

