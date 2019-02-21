#Verify that the script in the previous problem generates equiprobable symbols

import numpy as np

#function for generating coin toss
def coin(x):
	return 2 * np.random.randint(2, size = x) - 1	#func generates *1* number, range [0,2),  Z
	
simlen = 1e5
toss_results = coin(int(simlen))

print "Probability of 1 = ", np.size(np.nonzero(toss_results == 1)) / simlen

print "Probability of -1 = ", np.size(np.nonzero(toss_results == -1)) / simlen
