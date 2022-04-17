#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier as fourier
import numpy as np
from sympy.abc import t, w
from matplotlib.backend_bases import KeyEvent
import matplotlib.pyplot as plt

def on_key(event:KeyEvent):
    if event.key == 'escape':
        plt.close()


#%% DFT and FFT
f = 16e3    # 采样频率16KHz
N = 1024    # 序列长度1000
t = np.linspace(0, N/f, N)
x = 7*np.sin(2*np.pi*6000*t) + 3*np.sin(2*np.pi*3000*t) + 5*np.sin(2*np.pi*800*t)
# w = fourier.dft(x)
# xr = np.real(fourier.idft(w))
# w = fourier.fftshift(w)
w = fourier.fft(x)  # 补零会频谱分布有些微影响
xr = np.real(fourier.ifft(w))
w = fourier.fftshift(w)
# w = np.fft.fft(x)
# xr = np.real(np.fft.ifft(w))
# w = np.fft.fftshift(w)
wabs = np.abs(w)/w.size
print('Parseval - x: ', np.sum(np.abs(x)**2))
print('Parseval - w: ', np.sum(np.abs(w)**2) / w.size)
fig = plt.figure('DFT and FFT')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
x_range = np.arange(N)
# ax.stem(x_range, x, linefmt='g-', basefmt='o', use_line_collection=True)
ax.plot(x_range, x, '-')
ax.plot(np.arange(xr.size), xr, 'r-')
ax = fig.add_subplot(1, 2, 2)
w_range = np.linspace(-f//2, f//2, w.size)
ax.plot(w_range[:int(w.size/2)], wabs[:int(w.size/2)], 'g-')
ax.plot(w_range[int(w.size/2):], wabs[int(w.size/2):], 'r-')
# ax.stem(w_range, wabs, linefmt='g-', basefmt='o', use_line_collection=True)
ax.set_xticks(np.linspace(-f//2, f//2, 9))
ax.set_xticklabels([str(n) for n in np.linspace(-f//2/1000, f//2/1000, 9)])
ax.set_xlabel(r'$KHz$')

plt.show()
