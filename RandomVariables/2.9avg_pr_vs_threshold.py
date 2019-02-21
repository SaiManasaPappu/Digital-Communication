#Now consider a threshold lambda > 0 and find the average probability of error. Plot this with respect to lambda.

import numpy as np
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt

def Q(x):
	return 0.5 * scipy.special.erfc(x / np.sqrt(2))
	
l = np.linspace(0, 10, 100)	#lambda
A = 4.0

avg_pr = []

for i in range (0, 100):
	avg_pr.append((Q(A-l[i]) + Q(A+l[i])) / 2)

plt.plot(l, avg_pr)
plt.xlabel('$Lambda$')
plt.ylabel('Avg error')
plt.show()
