import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
def inverse_exp(X, beta):
	return -beta*np.log(1-X)
if __name__ == '__main__':
	# simulate distribution of EXP(beta)
	X = np.random.rand(1000)
	beta = 1
	Y = inverse_exp(X,beta)
	plt.scatter(Y, X)
	plt.title("simulated exponetial cdf of beta={}".format(beta))

