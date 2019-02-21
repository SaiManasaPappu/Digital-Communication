#V = X1^2 + X2^2
import math
import numpy as np
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt

simlen = 1e5
x1 = np.random.normal(0, 1, int(simlen))
x2 = np.random.normal(0, 1, int(simlen))
v = np.power(x1, 2) + np.power(x2, 2)

maxlim = 6.0
maxrange = 100
h = 2 * maxlim / (maxrange - 1)
x_axis = np.linspace(-maxlim, maxlim, maxrange)

cdf = []
pdf = []

for i in range (0, maxrange):
	cdf.append(np.size(np.nonzero(v < x_axis[i])) / simlen)
	
for i in range (0, maxrange - 1):
	pdf.append((cdf[i+1] - cdf[i]) / (x_axis[i+1] - x_axis[i]))
print(-math.log(1-cdf[80])/x_axis[80])	# alpha
print(-math.log(1-cdf[90])/x_axis[90])	# alpha
plt.plot(x_axis.T, cdf)
plt.plot(x_axis[0: maxrange - 1].T, pdf)
plt.grid()
plt.legend(["CDF", "PDF"])
plt.show()
