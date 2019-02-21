#Evaluate the joint PDF of X1, X2 given by Px1,x2(x1, x2) = Px1(x1)*Px2(x2)

import numpy as np
import scipy 
import scipy.stats as sp
import matplotlib.pyplot as plt

x_axis = np.linspace(-6, 6, 100)

def gauss_pdf(x):
	return 1 / np.sqrt(2 * np.pi) * np.exp(- x * x / 2.0)
	
pdf_x1 = []
pdf_x2 = []
pdf_x1x2 = []

for i in range (0, 100):
	pdf_x1.append(gauss_pdf(x_axis[i]))
	pdf_x2.append(gauss_pdf(x_axis[i]))
	pdf_x1x2.append(pdf_x1[i] * pdf_x1[i])

plt.plot(x_axis.T, pdf_x1)
plt.plot(x_axis.T, pdf_x2)
plt.plot(x_axis.T, pdf_x1x2)
plt.grid()
plt.legend(["Px1", "Px2", "Px1,x2"])
plt.show()
