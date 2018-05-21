import numpy as np 
from scipy.stats import norm 


def example1(N):
	""" 
	h(x) = x**3 
	I is h(x) integral from 0 to 1 which equals 0.25
	"""
	X = np.random.rand(N)
	I_estm = np.mean(X**3)
	s_square = np.var(X**3) *N / (N-1)
	std_error = np.sqrt(s_square/N) 
	print("simulation estimate:", I_estm)
	print("std error of estimate:", std_error)

def example2(N, x):
	"""
	I is normal distribution integral from -inf to x
	"""

	X = np.random.randn(N)
	I_estm = np.mean([0 if s>=x else 1 for s in X])
	print("simulation estimate:", I_estm)
	print("true value: ", norm.cdf(x))

if __name__ == '__main__':
	N = 100000
	example2(N, 2)