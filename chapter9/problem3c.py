import numpy as np 
from scipy import stats 


data = [3.23, -2.50, 1.88, -0.68, 4.43, 0.17,
		1.03, -0.07, -0.01, 0.76, 1.76, 3.18,
		0.33, -0.31, 0.30, -0.61, 1.52, 5.43,
		1.54, 2.28, 0.42, 2.33, -1.03, 4.00,
		0.39]


def tao(obs):
	z95 = stats.norm.ppf(0.95)
	mu = np.mean(obs)
	sigma = np.std(obs)
	return mu + z95*sigma

def parametric_boostrap(dist, n, statistic, iters):
	Tboot = []
	for i in range(iters):
		obs = dist.rvs(size=n, random_state=i)
		Tboot.append(statistic(obs))
	return np.array(Tboot)

if __name__ == '__main__':
	n = len(data)
	z95 = stats.norm.ppf(0.95)
	mu_mle = np.mean(data)
	sigma_mle = np.std(data)
	tao_mle = tao(data)
	se_delta_method = (sigma_mle/(n**0.5)) * np.sqrt(1+z95**2/2)

	dist = stats.norm(loc=mu_mle,scale=sigma_mle)
	Tboot = parametric_boostrap(dist, n, tao, 1000)
	se_param_boostrap = np.sqrt(np.mean((Tboot-tao_mle)**2))


	print("maximum likelyhood estimate of 'tao':", tao_mle)
	print("delta method standard error of 'tao':", se_delta_method)
	print("parametric boostrap standard error of 'tao", se_param_boostrap)
