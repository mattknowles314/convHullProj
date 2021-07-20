'''
This code does some analysis on how quickly the piecewise calculator works.
In the future, I want to generalise this for use on all algorithms that we write.
'''



import time
import os
import matplotlib.pyplot as plt
import statistics as st

times = []

def test_time():
	t0 = time.time()
	os.system("python3 piecewise_hull_calculator.py")
	t1 = time.time()
	times.append(t1-t0)

def plot_times(avg_time): 
	plt.plot(times)
	plt.axhline(avg_time, color='r')
	plt.xlabel('Run')
	plt.ylabel('Time (s)')
	plt.show()

for i in range(0,50):
	test_time()

avg_time = st.mean(times)
sd_time = st.stdev(times)
plot_times(avg_time)
