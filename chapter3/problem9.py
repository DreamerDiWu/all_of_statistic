import numpy as np 
from scipy.stats import cauchy, norm
import matplotlib.pyplot as plt 
if __name__ == '__main__':
	X_bar_norm = []
	X_bar_cauchy = []
	for i in range(1,10001):
		x1 = cauchy.rvs(size=i)
		x2 = norm.rvs(size=i)
		X_bar_cauchy.append(np.mean(x1))
		X_bar_norm.append(np.mean(x2))
	plt.subplot(211)
	x = np.arange(1,10001)
	plt.title('normal mean')
	plt.scatter(x, X_bar_norm,c='red',marker='x',label='normal mean')
	plt.subplot(212)
	plt.title("cauchy mean")
	plt.scatter(x, X_bar_cauchy,label='cauchy mean')
	plt.show()
