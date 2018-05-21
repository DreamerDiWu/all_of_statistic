import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

def density_function(x):
	return 1/x * (1/(2*np.pi)**0.5) * np.e**(-np.log(x)**2/2)
	
if __name__ == '__main__':
	X = np.random.randn(10000)
	Y = [np.e**xi for xi in X]
	x = np.linspace(min(Y), max(Y), 10000)
	true_y = density_function(x)
	sns.set_style('whitegrid')
	sns.distplot(Y,hist=False,label='simulation')
	plt.plot(x, true_y,label='true density')
	plt.legend()
	plt.show()
