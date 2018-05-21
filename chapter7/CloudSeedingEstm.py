import numpy as np 
from matplotlib import pyplot as plt 

def load():
	with open('CloudSeeding.txt') as f:
		dataSet = []
		for line in f.readlines()[1:]:
			dataSet.append(list(map(float, line.strip().split())))
		return np.array(dataSet)

		
if __name__ == '__main__':
	cloud = load()
	X = cloud[:,0]
	Y = cloud[:,1]
	x_hat = np.mean(X)
	y_hat = np.mean(Y)
	theta_hat = x_hat - y_hat
	se_theta = np.sqrt(np.var(X) + np.var(Y))
	# 95% confidence interval
	Cn = (theta_hat-1.96*se_theta, theta_hat+1.96*se_theta)
	print("theta:",theta_hat)
	print( "se(theta):", se_theta) 
	print('95% confidence interval:',Cn)
