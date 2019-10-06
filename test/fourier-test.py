#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FS(Fourier Series)，傅里叶级数
FT(Fourier Transform)，傅里叶变换
"""

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier as fourier
import numpy as np
from sympy import Piecewise, integrate, fourier_series, symbols, DiracDelta
from sympy import Sum, exp, cos, sin, pi, I, Abs, oo
from sympy.plotting import plot
from sympy.abc import t, w, n, k
import matplotlib as mpl
import matplotlib.pyplot as plt
import moviepy.editor as mpy
from moviepy.video.io.bindings import mplfig_to_npimage

mpl.rcParams['font.family'] = 'Consolas'
mpl.rcParams['font.size'] = 11

def on_key(event:mpl.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close()

#%% FS
"""
# 周期脉冲函数，周期T=2，脉宽=T/2，脉冲高度=1
# 周期增大时，频谱越来越密集
T = 2
f = Piecewise((0, t < -T/4.0), (1, (-T/4.0 <= t) & (t <= T/4.0)), (0, t > T/4.0))
(a0, an, bn, fn) = fourier.fs(f, T)
print('a0 : ', a0.evalf())
print('an : ', [an.subs(n, j).evalf() for j in range(1, 5)])
print('bn : ', [bn.subs(n, j).evalf() for j in range(1, 5)])
print('fn : ', [Abs(fn.subs(n, j).evalf()) for j in range(5)])
print('Ref: ', [Abs((sin(j * pi / 2) / (j * pi)).evalf()) for j in range(5)])
fig = plt.figure('Fourier series')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
ax.plot(np.linspace(-T/2*11, T/2*11, 550), [f.subs(t, j) for j in np.linspace(-T/2, T/2, 50)]*11)
ax = fig.add_subplot(1, 2, 2)
fn_range = np.arange(-5*T, 5*T + 1)
fn_points = [Abs(fn.subs(n, j).evalf()) for j in fn_range]
ax.plot(fn_range, fn_points, 'o')
for i,j in enumerate(fn_range):
    ax.plot([j, j], [0, fn_points[i]], 'g', linewidth=2)
ax.set_xlabel(r'$|F(n)|-n\omega$')
"""

#%% FT
"""
# 矩形脉冲函数，脉宽tau=1，脉冲高度=1
tau = 1
f = Piecewise((0, t < -tau/2.0), (1, (-tau/2.0 <= t) & (t <= tau/2.0)), (0, t > tau/2.0))
fw = fourier.ft(f)
print('fw : ', [Abs(fw.subs(w, j).evalf()) for j in range(5)])
print('Ref: ', [Abs((tau * sin(j * tau / 2) / (j * tau / 2)).evalf()) for j in range(5)])
fig = plt.figure('Fourier transform')
fig.canvas.mpl_connect('key_press_event', on_key)
f_range = np.linspace(-tau*15, tau*15, 100)
ax = fig.add_subplot(1, 2, 1)
ax.plot(f_range, [f.subs(t, j) for j in f_range])
ax = fig.add_subplot(1, 2, 2)
ax.plot(f_range, [Abs(fw.subs(w, j).evalf()) for j in f_range])
ax.set_xlabel(r'$|F(\omega)|-\omega$')
"""

#%% DFS
# 三角波序列，数字周期N=21
N = 21
xn = Piecewise((n/10+1, n < 0), (1-n/10, n >= 0))
xk = fourier.dfs(xn, N, (n, -(N//2), N//2))
print('xn : ', [xn.subs(n, j).evalf() for j in range(5)])
print('xk : ', [Abs(xk.subs(k, j).evalf()) for j in range(5)])
fig = plt.figure('Discrete Fourier Series')
fig.canvas.mpl_connect('key_press_event', on_key)
x_range = np.arange(-(3*N//2), (3*N)//2+1)
ax = fig.add_subplot(1, 2, 1)
xn_points = [xn.subs(n, j).evalf() for j in np.arange(-(N//2), N//2+1)]*3
ax.plot(x_range, xn_points, 'o')
for i,j in enumerate(x_range):
    ax.plot([j, j], [0, xn_points[i]], 'g', linewidth=2)
ax = fig.add_subplot(1, 2, 2)
xk_points = [Abs(xk.subs(k, j).evalf()) for j in x_range]
ax.plot(x_range, xk_points , 'o')
for i,j in enumerate(x_range):
    ax.plot([j, j], [0, xk_points[i]], 'g', linewidth=2)
ax.set_xlabel(r'$|X(k)|-k$')


#%% DTFT
# fig = plt.figure('Discrete Time Fourier Transform')

plt.show()
sys.exit()
