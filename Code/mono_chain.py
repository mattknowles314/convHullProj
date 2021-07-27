def cross_product(o,a,b):
	return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def mono_conv_hull(S):
	L = []
	if len(S) <= 3:
		print("Error - Need more than 3 points")
	else:
		for i in S:
			while len(L) >= 2 and cross_product(L[-2], L[-1], i) <= 0:
				L.pop()
			L.append(i)
