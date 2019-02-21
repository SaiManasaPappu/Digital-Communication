#Plot Pr(X_cap=1/X=1) with respect to A and compare with Q(x).

import numpy as np
import mpmath as mp
from scipy import special
import matplotlib.pyplot as plt
import subprocess

def coin(x):
	return 2 * np.random.randint(2, size = x) - 1;
	
def probability(A, X, N):
	Y = A * X + N
	x = np.size(np.nonzero(X == 1))
	x_cap = 0.0
	for i in range (0, int(simlen)):
		if X[i] == 1:		# simulation
			if Y[i] < 0:
				x_cap = x_cap + 1
	return x_cap / x
	
simlen = 1e4
N = np.random.normal(0, 1, int(simlen))
X = coin(int(simlen))

x_axis = np.linspace(0, 4.0, 100)	#x_axis = A
Pr_array = []
Qx_array = []

for i in  range (0, 100):
	Pr_array.append(probability(x_axis[i], X, N))
	Qx_array.append(0.5 *special.erfc(x_axis[i] / np.sqrt(2)))
	
#plt.plot(x_axis.T, Pr_array, 'o')	
#plt.plot(x_axis.T, Qx_array)
plt.semilogy(x_axis.T, Pr_array, 'o')	
plt.semilogy(x_axis.T, Qx_array)
plt.grid()
plt.xlabel('$A$')
plt.ylabel('$Pr and Q$')
plt.legend(["Simulation", "Theory"])
plt.show()
