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


#%% DFT
N = 41
t = np.linspace(-1, 1, N)
x = np.piecewise(t, [t < 0, t >= 0], [lambda t: 1 + t, lambda t: 1 - t])
w = fourier.dft(x)
xr = np.real(fourier.idft(w))
w = fourier.fftshift(w)
# w = np.fft.fft(x)
# xr = np.real(np.fft.ifft(w))
# w = np.fft.fftshift(w)
wabs = np.abs(w)/w.size
print('Parseval - x: ', np.sum(np.abs(x)**2))
print('Parseval - w: ', np.sum(np.abs(w)**2) / w.size)
fig = plt.figure('DFT')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
x_range = (np.arange(0, N) - N//2) / 2 # 绘图范围设到[-10, 10]
ax.stem(x_range, x, linefmt='g-', basefmt='o', use_line_collection=True)
ax = fig.add_subplot(1, 2, 2)
ax.stem(x_range, wabs, linefmt='g-', basefmt='o', use_line_collection=True)
ax.set_xlabel(r'$|X(k)|-k$')

plt.show()
