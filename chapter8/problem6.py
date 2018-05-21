import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from collections import namedtuple
plt.style.use('ggplot')
CI = namedtuple('CI','low high')
def boostrap(obs, statistic, iters):
	Tboot = []
	for i in range(iters):
		boot_obs = [np.random.choice(obs) for i in range(len(obs))]
		Tboot.append(statistic(boot_obs))
	return Tboot

def statistic_theta(obs):
	return np.exp(np.mean(obs))


if __name__ == '__main__':
	n = 100
	mu = 5
	obs = stats.norm.rvs(size=n,loc=mu)
	theta_hat = statistic_theta(obs)
	theta_boot = boostrap(obs, statistic_theta, 1000)
	boot_se = np.std(theta_boot)
	interval = CI(theta_hat-1.96*boot_se, theta_hat+1.96*boot_se)
	print("95% confidence interval:", interval)

	# compare with true sampling distribution of theta
	theta_samples = []
	for i in range(len(theta_boot)):
		new_obs = stats.norm.rvs(size=n,loc=mu)
		theta_samples.append(statistic_theta(new_obs))
	plt.subplot(221)
	plt.title("boostrap distribution of theta")
	sns.distplot(theta_boot, bins=30)
	plt.subplot(222)
	plt.title("sampling distribution of theta")
	sns.distplot(theta_samples, bins=30)
	plt.show()



