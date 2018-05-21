import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
N = [1, 5, 25, 100]
sampling_time = 1000
for n in N:
	X_bar_seq = []
	for i in range(sampling_time):
		X = [np.random.rand() for i in range(n)]
		X_bar = 1/n * np.sum(X)
		X_bar_seq.append(X_bar)
	plt.figure()
	plt.title("distribution of X_bar with n={}".format(n))
	sns.distplot(X_bar_seq,hist=False)
	plt.show()
