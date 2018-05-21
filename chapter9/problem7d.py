import numpy as np 
from scipy import stats 

from problem3c import parametric_boostrap

def statistic(obs):
	return sum(obs)/len(obs)


def CI(estimator, se, alpha=0.10):
	z_alpha = stats.norm.ppf(1-alpha/2)
	return (estimator-z_alpha*se, estimator+z_alpha*se)

if __name__ == '__main__':
	n1, n2 = 200, 200
	X1, X2 = 160, 148
	p1_mle, p2_mle = X1/n1, X2/n2
	psai_mle = p1_mle - p2_mle
	se_delta_method = np.sqrt(p1_mle*(1-p1_mle)/n1 + p2_mle*(1-p2_mle)/n2)
	iters = 1000
	Tboot1 = parametric_boostrap(stats.bernoulli(p=p1_mle), n1, statistic, iters )
	Tboot2 = parametric_boostrap(stats.bernoulli(p=p2_mle), n2, statistic, iters )
	Tboot = Tboot1 - Tboot2
	se_param_boostrap = np.sqrt(np.mean((Tboot-psai_mle)**2))
	CI_delta_method = CI(psai_mle, se_delta_method)
	CI_param_boostrap = CI(psai_mle, se_param_boostrap)

	print("90% confidence interval:")
	print("delta method:", CI_delta_method)
	print('parametric boostrap method:', CI_param_boostrap)
