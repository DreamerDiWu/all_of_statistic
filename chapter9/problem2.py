import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns
plt.style.use('ggplot')

def statistic(X):
	return (min(X) + max(X)) / 2


if __name__ == '__main__':
	a, b = 1, 3
	n = 10
	moments, plugins = [], []
	for _ in range(10000):
		# note: X ~ uniform(loc, loc+scale)
		obs = stats.uniform.rvs(size=n, loc=a, scale=b-a)
		moment_estm = statistic(obs)
		plugin_estm = np.mean(obs)

		moments.append(moment_estm)
		plugins.append(plugin_estm)
	plt.subplot(221)
	plt.title("moment estimation")
	sns.distplot(moments)
	plt.subplot(222)
	plt.title("plug-in estimation")
	sns.distplot(plugins)
	plt.show()

	plugins_mse = (b-a)**2 / (12*n)

	print("MSE of plug-in estimation:", plugins_mse)
	print("MSE of moments estimation:", np.var(moments))
