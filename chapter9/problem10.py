import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')
from problem7d import CI
from problem3c import parametric_boostrap
from problem9 import nonparam_boostrap

def statistic(obs):
	return max(obs)

if __name__ == '__main__':
	n = 50
	obs = stats.uniform.rvs(size=n)
	theta_mle = statistic(obs)
	B = 1000
	dist = stats.uniform(loc=0,scale=theta_mle)
	param_Tboot = parametric_boostrap(dist, n, statistic, iters=B)
	nonparam_Tboot = nonparam_boostrap(obs, statistic, iters=B)
	true_dist_obs = [max(stats.uniform.rvs(size=n, random_state=i)) for i in range(B)]
	plt.subplot(211)
	plt.title("parametric_boostrap")
	sns.distplot(param_Tboot)
	sns.distplot(true_dist_obs)
	plt.subplot(212)
	plt.title('nonparam_boostrap')
	sns.distplot(nonparam_Tboot)
	sns.distplot(true_dist_obs)
	plt.show()
