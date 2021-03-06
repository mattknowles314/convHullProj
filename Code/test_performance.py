'''
This code does some analysis on how quickly different functions work.
In the future, I want to generalise this for use on all algorithms that we write.
'''

import time
import os
import matplotlib.pyplot as plt
import statistics as st
from rouxHull import *
from mono_chain import *
from quickhull2 import *

lengths = []
avg_times_roux = []
avg_times_mono = []
avg_times_quick = []
def test_hull(q,n):
	S = []
	for i in range(1,q):
		p = [i,random.randint(1,200)]
		S.append(p)
	times_roux = []
	times_mono = []
	times_quickhull = []
	for i in range(0,n):	
		t0 = time.time()
		roux_conv_hull(S)
		t1 = time.time()
		mono_conv_hull(S)
		t2 = time.time()
		quickHull(S)
		t3 = time.time()
		times_roux.append(t1-t0)
		times_mono.append(t2-t1)
		times_quickhull.append(t3-t2)
	avg_times_roux.append(st.mean(times_roux))
	avg_times_mono.append(st.mean(times_mono))
	avg_times_quick.append(st.mean(times_quickhull))

for q in range(5,500):
	lengths.append(q)
	test_hull(q,50)

plt.plot(lengths,avg_times_roux, color="blue", label="RouxHull")
plt.plot(lengths,avg_times_mono, color="red", label="Monotone-Chain")
plt.plot(lengths,avg_times_quick, color="green", label="Quickhull")
plt.legend(loc="upper left")
plt.xlabel('Number of Points')
plt.ylabel('Time (s)')
plt.show()