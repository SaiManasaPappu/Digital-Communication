import numpy as np
import matplotlib.pyplot as plt
from scipy import special

N = int(1e6)
x_axis = np.linspace(0,10,100)
a = np.sqrt(10**(x_axis/10))
s0 = [1, 0]
n1 = np.random.normal(0 ,1, N)
n2 = np.random.normal(0 ,1, N)

def fun(x):
    return 1-0.5*special.erfc(x/2)

def calcprob(A):
    y0x1 = A * s0[0] + n1
    y0x2 = A * s0[1] + n2
    prob=(np.size(np.nonzero(abs(y0x2)<y0x1)) / float(N))
    return prob
    
sim=[]
thry=[]
for i in range(0,100):	
    sim.append(1-calcprob(a[i])) # prob that sent s0 and error occured
    thry.append(1-fun(a[i])**2)  # 1-P(X<A,Y<A) = 1-P(X<A)P(Y<A) = 1-(P(X<A))^2 = 1-(P(Y<A))^2
    
plt.semilogy(x_axis,sim,'r*',label='simulated')
plt.semilogy(x_axis,thry,'-',label='theoretical')
plt.xlabel('SNR in dB')
plt.legend()
plt.grid()
plt.show()
