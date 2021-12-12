#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier as fourier
import numpy as np
import scipy as sp
import sympy as sy
from sympy import Piecewise, integrate, fourier_series, symbols, DiracDelta
from sympy import Sum, exp, cos, sin, pi, I, Abs, oo
from sympy.plotting import plot
from sympy.abc import t, w, W, n, k
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'Consolas'
mpl.rcParams['font.size'] = 11

def on_key(event:mpl.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close()


#%% FT
# 三角波函数，三角波宽T=2，高度=1
T = 2
f = Piecewise((0, (t < -T/2) | (t > T/2)),  (t/(T/2)+1, t < 0), (1-t/(T/2), t >= 0))
fw = fourier.ft(f)
# fw = sy.fourier_transform(f, t, w)  # sympy用的另一个ft形式，e的指数多了2pi
print('fw : ', [Abs(fw.subs(w, j).evalf()) for j in range(5)])
fig = plt.figure('Fourier transform')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
fx_range = np.linspace(-T, T, 100)
ax.plot(fx_range, [f.subs(t, j) for j in fx_range])
ax = fig.add_subplot(1, 2, 2)
fw_range = np.linspace(-T*8, T*8, 100)
ax.plot(fw_range, [Abs(fw.subs(w, j).evalf()) for j in fw_range])
ax.set_xlabel(r'$|F(\omega)|-\omega$')

plt.show()
sys.exit()
