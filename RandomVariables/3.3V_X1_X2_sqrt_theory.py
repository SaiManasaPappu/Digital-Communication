#V = X1^2 + X2^2 + theory

import numpy as np
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt

def F_A(x):
	return x>0 and 1.0 - np.exp(-0.5 * x**2) or 0
	
def P_A(x):
	return x>0 and x * np.exp(-0.5 * x**2) or 0

simlen = 1e5
x1 = np.random.normal(0, 1, int(simlen))
x2 = np.random.normal(0, 1, int(simlen))
v = np.sqrt(np.power(x1, 2) + np.power(x2, 2))

maxlim = 6.0
maxrange = 100
h = 2 * maxlim / (maxrange - 1)
x_axis = np.linspace(-maxlim, maxlim, maxrange)

cdf = []
pdf = []
cdf_theory =[]
pdf_theory = []
for i in range (0, maxrange):
	cdf.append(np.size(np.nonzero(v < x_axis[i])) / simlen)
	cdf_theory.append(F_A(x_axis[i]))
	pdf_theory.append(P_A(x_axis[i]))
for i in range (0, maxrange - 1):
	pdf.append((cdf[i+1] - cdf[i]) / h)
	
plt.plot(x_axis.T, cdf, 'ro')
plt.plot(x_axis[0: maxrange - 1].T, pdf,'bo')
plt.plot(x_axis.T, cdf_theory,'r-')
plt.plot(x_axis.T, pdf_theory,'b-')
plt.grid()
plt.legend(["CDF_sim", "PDF_sim", "CDF_thry", "PDF_thry"])
plt.show()
