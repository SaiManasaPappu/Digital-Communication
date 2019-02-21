import numpy as np
import matplotlib.pyplot as plt

#function for generating coin toss

def coin(x):
	return 2 * np.random.randint(2, size = x) - 1;
	
simlen = 1e5
N = np.random.normal(0, 1, int(simlen))
X = coin(int(simlen))
A = 5
Y = A * X + N

plt.plot(Y, 'o')
plt.xlabel('$Sample$')
plt.ylabel('$Y$')
plt.show()
