import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')

def mixture_of_gaussian(k, mus, sigmas, size, random_state=0, alpha_k=None):
	if not alpha_k:
		rnd = stats.uniform.rvs(size=k, random_state=random_state)
		alpha_k = rnd / sum(rnd)
	k_dists = [stats.norm(loc=mus[i], scale=sigmas[i]) for i in range(k)]
	k_model_prob = np.cumsum(alpha_k)
	data = []
	for j in range(size):		
		# find dist according to probs
		rnd = np.random.rand()
		for kth, prob in enumerate(k_model_prob):
			if rnd < prob:
				cur_dist = k_dists[kth]
				break
		data.append(cur_dist.rvs())
	print("data generated from {} mixed normal:".format(k))
	for i in range(k):
		print("model {} of (mu={},sigma={}) with prob {}"
			.format(i+1, mus[i], sigmas[i], alpha_k[i]))
	return np.array(data), alpha_k

def E_step(data, k_dists, alpha_k):
	ret = []
	for obs in data:
		num = []
		for dist, alpha in zip(k_dists, alpha_k):
			
			num.append(dist.pdf(obs)*alpha)
		num = np.array(num)
		ret.append(num/sum(num))
	return np.array(ret)
	
def M_step(data, E_step_outcome):
	mus, sigmas,alphas = [], [], []
	for k in range(E_step_outcome.shape[1]):
		mu_k = sum(data*E_step_outcome[:,k])/ sum(E_step_outcome[:, k])
		mus.append(mu_k)
		sigma_k = np.sqrt(sum(E_step_outcome[:,k]*(data-mu_k)**2) / sum(E_step_outcome[:,k]))
		sigmas.append(sigma_k)
		alpha_k = sum(E_step_outcome[:,k]) / len(data)
		alphas.append(alpha_k)
	return mus, sigmas, alphas


def EM(data, mus0, sigmas0, alphas0, precision=0.2, max_iterations=100, plot=True):
	k_dists0 = [ stats.norm(loc=mu, scale=sigma) for mu, sigma in zip(mus0, sigmas0)]
	E_step_outcome = E_step(data, k_dists0, alphas0)

	fore_params = np.array([mus0, sigmas0, alphas0])
	iters = 0
	while True:
		iters += 1
		mus_i, sigmas_i, alphas_i = M_step(data, E_step_outcome)
		cur_params = np.array([mus_i, sigmas_i, alphas_i])
		if np.abs(fore_params-cur_params).all() <= precision or iters >= max_iterations:
			break
		else:
			k_dists_i = [stats.norm(mu, sigma) for mu, sigma in zip(mus_i, sigmas_i)]
			E_step_outcome = E_step(data, k_dists_i, alphas_i)
	print("after %d iterations:"%iters)
	print("estimations:")
	print("mus --> estimate:{}, true value:{}".format(mus_i, mus))
	print("sigmas --> estimate:{}, true value:{}".format(sigmas_i, sigmas))
	print("alphas --> estimate:{}， true value:{}".format(alphas_i, alpha_k))

	if plot == True:
		print('generate distribution plot...')
		new_obs, _ = mixture_of_gaussian(len(alpha_k), mus_i, sigmas_i, 
									size=n, random_state=0, alpha_k=alphas_i)
		sns.distplot(data, label="true distribution")
		sns.distplot(new_obs ,label="estimated distribution")
		plt.legend()
		plt.show()

if __name__ == '__main__':
	mus=[-4, 4, 10]
	sigmas=[1, 2, 4]
	n = 1000
	data, alpha_k = mixture_of_gaussian(3, mus,sigmas,size=n, random_state=19)
	# sns.distplot(data)
	# plt.show()

	mus0 = [-3, 5, 8]
	sigmas0 = [1, 1, 3]
	alphas0 = [0.3, 0.3, 0.4]
	EM(data, mus0, sigmas0, alphas0)
	