import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from collections import namedtuple
plt.style.use('ggplot')

def empirical_cdf(obs, X):
	return np.array([np.sum(obs <= x) / len(obs) for x in X])

def error(n, alpha):
	return np.sqrt(0.5/n*np.log(2/alpha))

def confidence_band(empirical, error):
	"""
	empirical is a seq of value of empirical function 
	"""
	L = empirical - error
	L[L < 0] = 0
	U = empirical + error
	U[U > 1] = 1
	return (L, U)

def Coverage(dist, size=100, iters=100):
	correct = 0
	for i in range(iters):
		obs = dist.rvs(size=size)
		x = np.linspace(-3, 3, 1000)
		ECDF = empirical_cdf(obs, x)
		L, U = confidence_band(ECDF, error(size, 0.05))
		c = sum(1 for i in range(len(x)) if not (L[i] <= dist.cdf(x[i]) <= U[i]))
		correct += 1 if c == 0 else 0
	return correct / iters

if __name__ == '__main__':
	n = 100

	obs = stats.norm.rvs(size=n)
	err = error(100, 0.05)
	x = np.linspace(-3, 3, 10000)
	emp_cdf = empirical_cdf(obs, x)
	true_cdf = stats.norm.cdf(x)
	CB = confidence_band(emp_cdf, err)
	
	plt.plot(x, emp_cdf, c='blue', label="empirical cdf")
	plt.plot(x, CB[0], label="lower bound",ls='-.')
	plt.plot(x, CB[1], label="upper bound",ls='--')
	plt.plot(x, true_cdf, label="true cdf")
	plt.legend()
	plt.show()

	coverage = Coverage(stats.norm)
	print("after {} iterations with {} obs\nthe coverage of confidence band is {}"
		.format(*Coverage.__defaults__, coverage))


