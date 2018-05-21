from scipy.stats import norm
import numpy as np 
from matplotlib import pyplot as plt
T = [.1, .5, 1, 1.5, 2, 2.5]

true_probs = []
che_bounds = []
mill_bounds = []

for n in range(1, 10001):
	t =  3*(1/n)**0.5
	prob = 2*(1-norm.cdf(t, loc=0,scale=(1/n)**0.5))
	
	che_bound = 1 / (t**2 * n)
	mill_bound = np.sqrt(2/np.pi)*(1/np.sqrt(n)/t)*np.e**((-n*(t**2))/2)
	true_probs.append(prob)
	che_bounds.append(che_bound)
	mill_bounds.append(mill_bound)

plt.figure()
seq = np.arange(1,10001)
plt.plot(seq,true_probs, label='true_probs')
plt.plot(seq,mill_bounds, label='mill_boundary')
plt.plot(seq,che_bounds, label='chebyshev_boundary')
plt.legend()
plt.show()



