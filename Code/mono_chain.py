#Andrew's Monotone Chain Convex Hull
import matplotlib.pyplot as plt

def cross_product(o,a,b):
	return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def mono_conv_hull(S):
	L = []
	U = []
	if len(S) <= 3:
		print("Error - Need more than 3 points")
	else:
		for i in S:
			while len(L) >= 2 and cross_product(L[-2], L[-1], i) <= 0:
				L.pop()
			L.append(i)
'''
sX = []
sY = []
lX = []
lY = []

for i in S:
	sX.append(i[0])
	sY.append(i[1])
for i in L:
	lX.append(i[0])
	lY.append(i[1])

plt.plot(sX,sY, color="blue", label="f(x)")
plt.plot(lX,lY, '--r', label="CHull(f(x))")
plt.legend(loc="upper left")
plt.show()
'''