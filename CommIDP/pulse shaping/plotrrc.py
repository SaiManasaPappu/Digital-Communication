import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
from scipy import special
from scipy.fftpack import fft, ifft

#   http://www.satbroadcasts.com/DVB-S_Bitrate_and_Bandwidth_Calculator.html
 
symrate = 27500.0
symdur = 1/symrate
poi_per_sym = 100
k = 10.0/symdur



#zero_zero = np.sinc(k*(n-symdur*0.125)) #time domain
#zero_one = np.sinc(k*(n-symdur*0.375)) 
#one_zero = np.sinc(k*(n-symdur*0.625))
#one_one = np.sinc(k*(n-symdur*0.875))

h=[]



f = np.linspace(-1e4,1e4,int(poi_per_sym))
Ts = 1e-2 # what values should be taken  ?
fn = 1/(2*Ts)
alpha = 0.35

def func(x,alpha):
	if abs(x) < fn*(1-alpha) :
		return 1
	elif abs(x) > fn*(1+alpha) :
		return 0
	else:
		return np.sqrt(0.5+0.5*(math.sin((math.pi/(2*fn))*((fn-abs(x))/alpha))))
		
def genh(alpha):
	for i in range(0,int(poi_per_sym)):
		h.append(func(f[i],alpha))
	
	
genh(alpha)

noof_symbols = 30

n = np.linspace(0,noof_symbols*symdur,noof_symbols*poi_per_sym)

xbinary = np.random.randint(2, size = 2*noof_symbols)
xtime = np.zeros(noof_symbols*poi_per_sym)

for i in range(0,noof_symbols):
	if xbinary[2*i] == 0 and xbinary[2*i + 1] == 0 :
		xtime = xtime + np.sinc(k*(n-(i+1)*symdur*0.125))
	elif xbinary[2*i] == 0 and xbinary[2*i + 1] == 1 :
		xtime = xtime + np.sinc(k*(n-(i+1)*symdur*0.375))
	elif xbinary[2*i] == 1 and xbinary[2*i + 1] == 0 :
		xtime = xtime + np.sinc(k*(n-(i+1)*symdur*0.625))
	elif xbinary[2*i] == 1 and xbinary[2*i + 1] == 1 :
		xtime = xtime + np.sinc(k*(n-(i+1)*symdur*0.875))

xtime_with_noise = xtime + np.random.normal(0,1,len(xtime))
xfft = fft(xtime_with_noise)
yfft = h*xfft
ytime = ifft(yfft)

# how to get xhattime from yfft ?

'''
# after getting xhattime

xhattime 
xhatbin = []
for i in range(0,noof_symbols):
	maxindex = i*symdur
	maxvalue = xhattime[i*symdur]
	for j in range(0,poi_per_sym):
		if xhattime[i*symdur+j] > maxvalue :
			maxvalue = xhattime[i*symdur+j]
			maxindex = j
	if 0<=j and j<0.25*poi_per_sym :
		xhatbin.append(0)
		xhatbin.append(0)
	elif 0.25*poi_per_sym<=j and j<0.5*poi_per_sym :
		xhatbin.append(0)
		xhatbin.append(1)
	if 0.5*poi_per_sym<=j and j<0.75*poi_per_sym :
		xhatbin.append(1)
		xhatbin.append(0)
	if 0.75*poi_per_sym<=j and j<1*poi_per_sym :
		xhatbin.append(1)
		xhatbin.append(1)
		
print(xbinary)
print(xhatbin)

count = 0
for i in range(0,2*noof_symbols):
	if(xbinary[i] != xhatbin[i]):
		count = count + 1
print("error="+str((1.0*count)/(2*noof_symbols)))

'''	
		

plt.plot(n,xtime,label='xtime')
plt.plot(n,abs(fft(xtime)),label='fft')
plt.legend(loc='best')

plt.grid()
plt.show()
