#5.3 , 5.4
import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy import special

def SNR_conv(SNR):
	return np.sqrt(10 ** (SNR / 10))
def err(x):
	return 0.5*special.erfc(x/2)
simlen = 1e4
n1 = np.random.normal(0, 1, int(simlen))
n2 = np.random.normal(0, 1, int(simlen))
#N1 = np.random.normal(0, 1, int(simlen))
#N2 = np.random.normal(0, 1, int(simlen))

s0 = [1, 0]
s1 = [0, 1]

def probability(A):
	y0x1 = A * s0[0] + n1
	y0x2 = A * s0[1] + n2
	#y1x1 = A * s1[0] + N1
	#y1x2 = A * s1[1] + N2

	pr = np.size(np.nonzero(y0x1 < y0x2)) / simlen
	return pr

x_axis = np.linspace(0, 10, 100)

pr_vec = scipy.vectorize(probability)
thry_vec = scipy.vectorize(err)

#plt.plot(x_axis, pr_vec(SNR_conv(x_axis)), 'go')
#plt.plot(x_axis, thry_vec(SNR_conv(x_axis)), 'g-')
plt.semilogy(x_axis, pr_vec(SNR_conv(x_axis)), 'go')
plt.semilogy(x_axis, thry_vec(SNR_conv(x_axis)), 'g-')
plt.grid()
plt.xlabel('$SNR_dB$')
plt.ylabel('$P_error$')
plt.show()
