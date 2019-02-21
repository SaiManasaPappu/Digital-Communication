#Plot Pr(X_cap=1/X=1) with respect to A. 

#!/importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
#from scipy.integrate import quad
#import scipy.integrate as spint
import matplotlib.pyplot as plt
import subprocess

#function for generating coin toss

def coin(x):
	return 2 * np.random.randint(2, size = x) - 1;
	
def probability(A, X, N):
	Y = A * X + N

	x = np.size(np.nonzero(X == 1))

	x_cap = 0.0

	for i in range (0, int(simlen)):
		if X[i] == 1:
			if Y[i] < 0:
				x_cap = x_cap + 1

	return x_cap / x				#returning probability
	
simlen = 1e5
N = np.random.normal(0, 1, int(simlen))
X = coin(int(simlen))

x_axis = np.linspace(0, 4.0, 100)	#x_axis = A
pr_array = []

for i in  range (0, 100):
	pr_array.append(probability(x_axis[i], X, N))
	
plt.plot(x_axis.T, pr_array, 'o')
plt.grid()
plt.xlabel('$A$')
plt.ylabel('$Pr$')
plt.show()
