import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy import special
import math
import random
simlen = 1e6

def non_coh_sim(Eb):
	avg_prob = 0
	phi_len = 100
	for m in range(phi_len):
		phi = random.uniform(0, 2*math.pi)
		s0 = [math.cos(phi) , math.sin(phi) , 0 ,0]
		r = [((np.sqrt(Eb)*s0[j])+np.random.normal(0, 1, int(simlen))) for j in range(4)]  # r is a 4 x simlen array
		pr=0
		r2 = np.square(r)
		for i in range (int(simlen)):
			if r2[0][i] + r2[1][i] < r2[2][i] +r2[3][i] :
				pr=pr+1
		pr= pr/simlen  	#pr= np.size(np.square(r[0])+np.square(r[1]) < np.square(r[2])+np.square(r[3])) /simlen
		avg_prob += pr
	return avg_prob/(1.0*phi_len)
	
def non_coh_thry_err(Eb):
	return 0.5*math.exp(-Eb*0.25)

def coh_thry_err(Eb):
	return 0.5*special.erfc(np.sqrt(Eb)*0.5)
	
def thry_bpsk(Eb):
	return 0.5 *special.erfc(np.sqrt(Eb) / np.sqrt(2))

def thry_qpsk(Eb):
	return 1-(1-0.5*special.erfc(np.sqrt(Eb)/2))**2
	
non_coh_sim_vec = scipy.vectorize(non_coh_sim)
non_coh_thry_vec = scipy.vectorize(non_coh_thry_err)
coh_thry_vec = scipy.vectorize(coh_thry_err)
bpsk_thry_vec = scipy.vectorize(thry_bpsk)
qpsk_thry_vec = scipy.vectorize(thry_qpsk)

x_axis = np.linspace(0, 10, 50)
EB = 10 ** (x_axis / 10)

plt.semilogy(x_axis, qpsk_thry_vec(EB),label='QPSK')
#plt.semilogy(x_axis, non_coh_sim_vec(EB), 'go')
plt.semilogy(x_axis, non_coh_thry_vec(EB),label='non_coh_BFSK')
plt.semilogy(x_axis, coh_thry_vec(EB),label='BFSK')
plt.semilogy(x_axis, bpsk_thry_vec(EB),label='BPSK')

plt.grid()
plt.xlabel('SNR in dB')
plt.ylabel('Theoretical errors')
plt.legend()
plt.show()
