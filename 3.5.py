from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

n = 800
t = np.linspace(0, 0.3, n)
sinfreq = 1000
triangle = 2.0*np.array(signal.sawtooth(2 * np.pi * 50 * t, 0.5))
for i in range(n):
    if triangle[i] > 1 :
        triangle[i] = 1.0 + max(0.1*np.sin(2 * np.pi * sinfreq * t[i]),0)
    if triangle[i] < -1 :
        triangle[i] = -1.0 - max(0.1*np.sin(2 * np.pi * sinfreq * t[i]),0)

ts = 0.001
fs = 1/ts  # Sampling frequency
fc = 50  # Cut-off frequency of the filter
# Generate the time vector properly

   
input_signal = triangle
plt.plot(t,input_signal,label='input_signal')
plt.figure()

w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(1, w, 'low')
output_signal = signal.filtfilt(b, a, input_signal)



order = 4
fc = 50
b, a = signal.butter(order, fc, 'low', analog=True)
w, h = signal.freqs(b, a)

plt.plot(w, 20 * np.log10(abs(h)))
plt.xscale('log')
plt.title('Butterworth filter frequency response (Magnitude) ')
plt.xlabel('Frequency Hz')
plt.ylabel('Amplitude [dB]')
# plt.plot(50,-3,'o')
# plt.text(56,-3,'(50,-3dB)')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(fc, color='green') # cutoff frequency

plt.figure()
angles = np.unwrap(np.angle(h))
output_signal = (1.0/np.sqrt(2))*output_signal
deg = (180.0/np.pi)*np.array(angles)
plt.plot(t,output_signal)
plt.figure()
plt.plot(w, deg, 'g',label='angle in degrees')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Angle in degrees', color='g')
plt.title('Butterworth filter frequency response (Phase) ')
plt.grid()
plt.axis('tight')
# plt.plot(50,-179.83,'o')
# plt.text(60,-179.83,'(50,-180)')

plt.show()
