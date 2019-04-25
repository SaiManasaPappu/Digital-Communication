import numpy as  np
import scipy
import math
import matplotlib.pyplot as plt
from scipy import special
from scipy.fftpack import fft, ifft

#   http://www.satbroadcasts.com/DVB-S_Bitrate_and_Bandwidth_Calculator.html
 
symrate = 27500.0
symdur = 1/symrate
poi_per_sym = 100


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

noof_symbols = 10

n = np.linspace(0,noof_symbols*symdur,noof_symbols*poi_per_sym)

xbinary = np.random.randint(2, size = noof_symbols)
xtime = np.zeros(noof_symbols*poi_per_sym)

print "symdur=" + str(symdur)
print xbinary

#plt.plot(n,np.sinc(k*n-(1+0.875)*k*symdur))

k= 1.0/symdur

for i in range(0,noof_symbols):
	if xbinary[i] == 1 :
		xtime = xtime + np.sinc(k*(n-i*symdur))
	elif xbinary[i] == 0 :
		xtime = xtime - np.sinc(k*(n-i*symdur))

eb_by_n0 = 10 #in db
print 1.0/(10**(eb_by_n0/10))
xtime_with_noise = xtime + np.random.normal(0,1.0/(10**(eb_by_n0/10)),len(xtime))
xfft = fft(xtime_with_noise)
#yfft = h*xfft
#ytime = ifft(yfft)

# how to get xhattime from yfft ?


# Here part


ht = np.ones(poi_per_sym)
con = np.convolve(xtime_with_noise,ht)
plt.subplot(2,1,1)
plt.plot(n,xtime,label='xtime')
plt.plot(n,xtime_with_noise,label='xwith_noise')
plt.subplot(2,1,2)
plt.plot(np.linspace(0,symdur*noof_symbols,len(con)),con,label='conv_output')

#plt.plot(n,abs(fft(xtime)),label='fft')
plt.legend(loc='best')

trimmed = con[poi_per_sym/2 : poi_per_sym/2 + noof_symbols*poi_per_sym]
print len(trimmed)
bhat = []
for i in range(noof_symbols):
	if trimmed[i*poi_per_sym]>0 :
		bhat.append(1)
	elif trimmed[i*poi_per_sym]<0 :
		bhat.append(0)
		
print(bhat)

plt.grid()
plt.show()
