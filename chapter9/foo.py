from scipy import stats
if __name__ == '__main__':
	dist = stats.bernoulli(p=0.5)
	print(dist.rvs(20))