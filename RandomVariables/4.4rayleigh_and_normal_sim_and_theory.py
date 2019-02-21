# Y = AX + N where A is Rayleigh with E[A^2] = gamma, N is Normal with (0, 1), X = {-1, 1}  and 0 < gamma < 10 dB.

import numpy as np
import scipy 
import scipy.stats as sp
import matplotlib.pyplot as plt

def snr_normal(snr_db):
	return np.power(10, snr_db / 10)
	
maxrange = 100
g_axis = np.linspace(0, 10, maxrange)

simlen = 1e5
x1 = np.random.normal(0, 1, int(simlen))
x2 = np.random.normal(0, 1, int(simlen))
A = np.sqrt(x1**2 + x2**2)
N = np.random.normal(0, 1, int(simlen))

def probability(gamma):
	Y = np.sqrt(gamma) * A + N
	pr = np.size(np.nonzero(Y < 0)) / simlen 
	return pr
	
def pr_theory(gamma):
	return 0.5 * (1 - np.sqrt(gamma / (gamma + 2.0)))

pr = scipy.vectorize(probability)
pr_t = scipy.vectorize(pr_theory)

plt.plot(g_axis, pr(snr_normal(g_axis)), 'o')
plt.plot(g_axis, pr(snr_normal(g_axis)))
plt.grid()
plt.xlabel('$Gamma$')
plt.ylabel('$P_e$')
plt.legend(["Simulation", "Theory"])
plt.show()
