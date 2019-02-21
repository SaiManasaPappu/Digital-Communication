# Py(Y|X=1) and Py(Y|X=-1) wrt A

import numpy as np
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt

#probability of error?

#u = 0, sigma = 1

maxrange = 100
A = 4.0
x_axis=np.linspace(-16, 16, maxrange)	#Py

def gauss_pdf(x):
	return 1 / np.sqrt(2 * np.pi) * np.exp(-(x**2) / 2.0)
	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)
	
#shifting graph for different means

plt.plot(x_axis + A, vec_gauss_pdf(x_axis))		#mean = A, variance = 1
plt.plot(x_axis - A, vec_gauss_pdf(x_axis))		#mean = -A, variance = 1
plt.grid()
plt.legend(["Py(Y|X=1)", "Py(Y|X=-1)"])
plt.show()
