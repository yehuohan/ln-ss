#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.dct as dct
import numpy as np
import scipy as sp
from scipy import fftpack
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'Consolas'
mpl.rcParams['font.size'] = 11

def on_key(event:mpl.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close()


f = 16e3    # 采样频率16KHz
N = 1024    # 序列长度1000
t = np.linspace(0, N/f, N)
x = 7*np.sin(2*np.pi*6000*t) + 3*np.sin(2*np.pi*3000*t) + 5*np.sin(2*np.pi*800*t)
ck = dct.dct(x)
xr = dct.idct(ck)
fig = plt.figure('DCT')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
x_range = np.arange(N)
ax.plot(x_range, x, '-')
ax.plot(x_range, xr, 'r-')
ax = fig.add_subplot(1, 2, 2)
c_range = np.linspace(0, f//2, N)
ax.plot(c_range, ck, 'g-')
ax.set_xlabel(r'$Hz$')

plt.show()
