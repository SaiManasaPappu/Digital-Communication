import numpy as np
import matplotlib.pyplot as plt

simlen = 1e3
Eb=5
s = np.array([[1,0],[0,1],[-1,0],[0,-1]])

y = [((Eb*s[i][j])+np.random.normal(0, 1, int(simlen)))for i in range(4) for j in range(2) ]
# y = [s0x,s0y,s1x,s1y,s2x,s2y,s3x,s3y]
 
for i in range(4):
	plt.scatter(y[2*i], y[2*i+1]) 
plt.grid()
plt.legend(["s0", "s1","s2","s3"])
plt.show()
