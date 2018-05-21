import numpy as np 
from matplotlib import pyplot as plt 

def epsilon(n, alpha=0.05):
	return np.sqrt(1/(2*n) * np.log(2/alpha))

def pn(n, p=0.4):
	X = [1 if np.random.rand()<p else 0 for i in range(n)]
	pn = np.mean(X)
	return pn


times = 100
p = 0.4 

# plot coverage versus n

# coverages = []
# for n in range(1,10001,100):
# 	epsilon_n = epsilon(n)
# 	coverage = 0
# 	for t in range(times):
# 		p_n = pn(n)
		
# 		if p_n - epsilon_n < p < p_n + epsilon_n:
# 			coverage += 1
# 	coverages.append(coverage/times)

# plot length versus n

length = []
N = list(range(100, 10001))
for n in N:
	epsilon_n = epsilon(n)
	length.append(2*epsilon_n)
	

plt.figure()
plt.plot(N, length,label='interval length(n)')
expect_length = 0.05
plt.hlines(expect_length,xmin=N[0]*0.9, xmax=N[-1]*1.1,label='expect length')
plt.legend()
for n in N:
	if (2*epsilon(n)) < expect_length:
		expect_n = n
		break
print("n should be {} if want length to be no more than {}".format(expect_n, expect_length))
plt.show()