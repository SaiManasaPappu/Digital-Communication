from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


order = 4
fc = 50
b, a = signal.butter(order, fc, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.plot(w, 20 * np.log10(abs(h)))
plt.xscale('log')
plt.title('Butterworth filter frequency response (Magnitude) ')
plt.xlabel('Frequency Hz')
plt.ylabel('Amplitude [dB]')
plt.plot(50,-3,'o')
plt.text(56,-3,'(50,-3dB)')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(fc, color='green') # cutoff frequency

plt.figure()
angles = np.unwrap(np.angle(h))
deg = (180.0/np.pi)*np.array(angles)
plt.plot(w, deg, 'g',label='angle in degrees')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Angle in degrees', color='g')
plt.title('Butterworth filter frequency response (Phase) ')
plt.grid()
plt.axis('tight')
plt.plot(50,-179.83,'o')
plt.text(60,-179.83,'(50,-180)')

ts = 0.001
fs = 1/ts  # Sampling frequency
# Generate the time vector properly
t = np.linspace(0,1000,1001) / fs
signala = np.sin(2*np.pi*50*t) # with frequency of 50
plt.plot(t, signala, label='a')
plt.figure()
fc = 50  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(4, w, 'low')
output = -signala/np.sqrt(2)
plt.plot(t, signala, label='input')
plt.plot(t, output, label='filtered')


plt.legend()
plt.show()
