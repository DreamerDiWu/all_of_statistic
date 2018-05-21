import numpy as np 
import matplotlib.pyplot as plt 
def skewness(X):
	mu_hat = np.mean(X)
	sigma_hat = np.std(X)
	return np.mean((X - mu_hat)**3) / sigma_hat**3

def boostrap(X, boostrap_times, statistic):
	TBoot = []
	for i in range(boostrap_times):
		boostrap_idx = np.random.randint(len(X),size=len(X))
		X_star = [X[boostrap_idx[i]] for i in range(len(X))]
		T_F_hat = statistic(X_star)
		TBoot.append(T_F_hat)
	return TBoot

def IsCovered(interval,true_value):
	if interval[0] <= true_value <= interval[1]:
		return True
	else:
		return False


if __name__ == '__main__':
	Y = np.random.randn(50)
	X = np.e**(Y)
	T_F = np.mean(X)
	true_value = np.e**0.5
	times = 100
	num_norm = 0
	num_percent = 0
	num_pivotal = 0
	for i in range(times):
		B = 100
		TBoot = boostrap(X, B, np.mean)
		se = np.std(TBoot)
		normal = (T_F - 2*se, T_F + 2*se)
		percentile = (np.percentile(TBoot,2.5), np.percentile(TBoot, 97.5))
		pivotal = (2*T_F - np.percentile(TBoot,97.5),
					2*T_F - np.percentile(TBoot,2.5))
		if IsCovered(normal, true_value):
			num_norm += 1
		if IsCovered(percentile, true_value):
			num_percent += 1
		if IsCovered(pivotal, true_value):
			num_pivotal += 1




	print("95% Interval")
	print("normal:", normal)
	print('percentile',percentile)
	print('pivotal:', pivotal)
	print('Coverage:')
	print('true value:', true_value)
	print('TF:',T_F)
	print("normal:", num_norm/times)
	print('percentile',num_percent/times)
	print('pivotal:', num_pivotal/times)
	



