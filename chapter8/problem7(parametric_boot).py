import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')
def boostrap(cdf, n, statistic, iters):
	Tboot = []
	for i in range(iters):
		boot_obs = cdf.rvs(size=n)
		Tboot.append(statistic(boot_obs))
	return Tboot

def statistic_theta(obs):
	return max(obs)

def true_density_func(x, n, theta):
	return n/theta * (x/theta)**(n-1)

if __name__ == '__main__':
	n = 50
	theta = 1
	obs = stats.uniform.rvs(size=n,scale=theta)
	theta_hat = statistic_theta(obs)
	estm_df = stats.uniform(scale=theta_hat)
	theta_boot = boostrap(estm_df, n, statistic_theta, 1000)


	# compare with true distribution of theta

	plt.subplot(221)
	plt.title("parametric boostrap distribution of theta")
	sns.distplot(theta_boot, kde=False)
	plt.subplot(222)
	plt.title("true distribution of theta")
	x = np.linspace(0, theta,10000)
	y = true_density_func(x, n, theta=theta)
	plt.plot(x, y)
	plt.show()



