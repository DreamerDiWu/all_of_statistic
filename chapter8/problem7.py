import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')
def boostrap(obs, statistic, iters):
	Tboot = []
	for i in range(iters):
		boot_obs = [np.random.choice(obs) for i in range(len(obs))]
		Tboot.append(statistic(boot_obs))
	return Tboot

def statistic_theta(obs):
	return max(obs)

def true_density_func(x, n, theta):
	return n/theta * (x/theta)**(n-1)

if __name__ == '__main__':
	n = 50
	theta = 1
	obs = stats.uniform.rvs(size=50,scale=theta)
	theta_hat = statistic_theta(obs)
	theta_boot = boostrap(obs, statistic_theta, 1000)


	# compare with true distribution of theta

	plt.subplot(221)
	plt.title("boostrap distribution of theta")
	sns.distplot(theta_boot)
	plt.subplot(222)
	plt.title("true distribution of theta")
	x = np.linspace(min(theta_boot), max(theta_boot),10000)
	y = true_density_func(x, n, theta=theta)
	plt.plot(x, y)
	plt.show()



