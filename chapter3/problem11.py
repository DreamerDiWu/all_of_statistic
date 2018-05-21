import numpy as np 
import matplotlib.pyplot as plt 
n = 10000

# E(X_n) = 0, V(X_n) = n
Y = np.sign(np.random.rand(n) - 0.5)
X_n = np.cumsum(Y)
# X = [(i+1)*np.random.randn(1) for i in range(n)]
plt.figure()

plt.plot(X_n)
plt.show()