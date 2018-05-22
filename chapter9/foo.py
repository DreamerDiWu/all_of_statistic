from scipy import stats
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
if __name__ == '__main__':
	a = stats.norm.rvs(size=100)
	sns.distplot(a, label='foo')
	plt.legend()
	plt.show()