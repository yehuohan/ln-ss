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

#%% FS
# 三角波函数，周期T=2，高度=1
# 周期增大时，频谱越来越密集
T = 2
f = Piecewise((t/(T/2)+1, t < 0), (1-t/(T/2), t >= 0))
(a0, an, bn, fn) = fourier.fs(f, T)
print('a0 : ', a0.evalf())
print('an : ', [an.subs(n, j).evalf() for j in range(1, 5)])
print('bn : ', [bn.subs(n, j).evalf() for j in range(1, 5)])
print('fn : ', [Abs(fn.subs(n, j).evalf()) for j in range(5)])
print('Ref: ', [(Abs((2 / ((j*j*pi*pi)).evalf()) if j & 1 == 1 else 0)) for j in range(5)])
fig = plt.figure('Fourier series')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
ax.plot(np.linspace(-T/2*5, T/2*5, 250), [f.subs(t, j) for j in np.linspace(-T/2, T/2, 50)]*5)
ax = fig.add_subplot(1, 2, 2)
fn_range = np.arange(-5*T, 5*T + 1)
fn_points = [Abs(fn.subs(n, j).evalf()) for j in fn_range]
ax.stem(fn_range, fn_points, linefmt='g-', basefmt='o', use_line_collection=True)
ax.set_xlabel(r'$|F(n\omega_0)|-n$')

plt.show()
sys.exit()
