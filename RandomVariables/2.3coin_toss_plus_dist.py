#Suppose X belongs to {-1, 1} and Y = AX + N where N tilde N(0, 1)

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
	
simlen = 1e5
N = np.random.normal(0, 1, int(simlen))
X = coin(int(simlen))
A = 4
Y = A * X + N

plt.plot(Y, 'o')
plt.xlabel('$Sample$')
plt.ylabel('$Y$')
plt.show()
