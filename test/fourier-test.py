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
from sympy import Piecewise, integrate, fourier_series, symbols
from sympy import exp, cos, sin, pi, I, Abs, oo
from sympy.plotting import plot
from sympy.abc import t, n
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
# 周期脉冲函数，周期T=2，脉宽=T/2，脉冲高度=1
# 周期增大时，频谱越来越密集
T = 2
f = Piecewise((0, t < -T/4.0), (1, (-T/4.0 <= t) & (t <= T/4.0)), (0, t > T/4.0))
(a0, an, bn, fn) = fourier.fs(f, T)
# print('a0 : ', a0.evalf())
# print('an : ', [an.subs(n, k).evalf() for k in range(1, 5)])
# print('bn : ', [bn.subs(n, k).evalf() for k in range(1, 5)])
# print('fn : ', [Abs(fn.subs(n, k).evalf()) for k in range(5)])
# print('Ref: ', [Abs((sin(k * pi / 2) / (k * pi)).evalf()) for k in range(5)])
fig = plt.figure('Fourier series')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
ax.plot(np.linspace(-5*T, 5*T, 500), [f.subs(t, k) for k in np.linspace(-T/2, T/2, 50)]*10)
ax = fig.add_subplot(1, 2, 2)
fn_range = [k for k in range(-5*T, 5*T)]
fn_points = [Abs(fn.subs(n, k).evalf()) for k in fn_range]
ax.plot(fn_range, fn_points, 'o')
for k in fn_range:
    ax.plot([k, k], [0, fn_points[k+5*T]], 'g', linewidth=2)
ax.set_xlabel(r'$|F(n)|-n\omega$')

plt.show()
sys.exit()

#%% FT
fig = plt.figure('Fourier transform')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
# ax.plot(np.linspace(-5, 5, 500), [f.subs(t, k) for k in np.linspace(-1, 1, 50)]*10)
ax = fig.add_subplot(1, 2, 2)
# ax.plot(fn_range, fn_points, 'o')
# ax.set_xlabel(r'$|F(n)|-n\omega$')
