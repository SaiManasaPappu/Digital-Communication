import numpy as np
import matplotlib.pyplot as plt  
simlen =100
Ts = 1
num_symbols = 3
bits = 2*np.random.randint(2,size = num_symbols)-1
print bits 

final = [0]*(simlen+(num_symbols-1)*20)  #contains the combined effect of all individual x i's.

x = []
t = np.linspace(0,(num_symbols+5)*Ts,100*(num_symbols+5))
x.append(np.zeros(100*(num_symbols+5)))

for i in range(num_symbols):
	if bits[i] == 1:
		for j in range(100*(num_symbols+5)):
			print j
			x[j] = x[j]+np.sinc(t[j]-i*Ts)

		
	elif bits[i]== -1:
		for j in range(100*(num_symbols+5)):
			print j
			x[j] = x[j]+np.sinc((t[j]-i*Ts) + np.pi)

plt.plot(t, x)
plt.grid()
plt.show()
