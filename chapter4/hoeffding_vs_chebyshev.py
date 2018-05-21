import numpy as np 
from matplotlib import pyplot as plt 
def hoeffding(n, epsilon=0.01):
	return np.e ** (-(2*n*epsilon))
def chebyshev(n, epsilon=0.01):
	return 1 / (4*n*epsilon)

seq = np.linspace(1000, 10000, 10000)
y1 = [hoeffding(k) for k in seq]
y2 = [chebyshev(k) for k in seq]
plt.figure()
plt.plot(seq, y1, label='hoeffding_bound')
plt.plot(seq, y2, c='red', label='Chebyshev_bound')
plt.legend()
plt.show()

