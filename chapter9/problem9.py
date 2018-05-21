import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')
from problem7d import CI
from problem3c import parametric_boostrap

def statistic(obs):
	return np.exp(np.mean(obs))

def nonparam_boostrap(obs, statistic, iters):
	Tboot = []
	for _ in range(iters):
		obs_boot = [np.random.choice(obs) for _ in obs]
		Tboot.append(statistic(obs_boot))
	return Tboot

if __name__ == '__main__':
	mu = 5
	n = 1000
	alpha = 0.05
	obs = stats.norm(mu, 1).rvs(size=n)
	theta_mle = statistic(obs)
	se_delta_method = theta_mle / n**0.5
	dist = stats.norm(np.mean(obs), 1)
	B = 1000
	param_Tboot = parametric_boostrap(dist, n, statistic, B)
	nonparam_Tboot = nonparam_boostrap(obs, statistic, B)
	se_param_boot = np.sqrt(np.mean((param_Tboot-theta_mle)**2))
	se_nonparam_boot = np.std(nonparam_Tboot)

	print("%d%% Confidence Interval:" % (100*(1-alpha)))
	print("delta method:", CI(theta_mle, se_delta_method))
	print('parametric boostrap:', CI(theta_mle, se_param_boot))
	print('nonparatric boostrap:', CI(theta_mle, se_nonparam_boot))


	delta_method_obs = stats.norm(theta_mle, se_delta_method).rvs(size=B)
	true_dist_obs = [statistic(stats.norm(mu, 1).rvs(size=n,random_state=i)) 
						for i in range(B)]
	# simulate distributions
	plt.subplot(221)
	plt.title("parametric boostrap")
	sns.distplot(param_Tboot)
	sns.distplot(true_dist_obs)
	plt.subplot(222)
	plt.title("nonparam boostrap")
	sns.distplot(nonparam_Tboot)
	sns.distplot(true_dist_obs)
	plt.subplot(223)
	plt.title("delta method")
	sns.distplot(delta_method_obs)
	sns.distplot(true_dist_obs)
	plt.subplot(224)
	plt.title("true sampling")
	sns.distplot(true_dist_obs)
	plt.show()