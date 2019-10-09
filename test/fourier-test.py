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
"""
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
"""

#%% FT
"""
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
"""


#%% DFS
"""
# 三角波序列，数字周期N=21
N = 21
xn = Piecewise((n/10+1, n < 0), (1-n/10, n >= 0))
xk = fourier.dfs(xn, N, (n, -(N//2), N//2))
print('xn : ', [xn.subs(n, j).evalf() for j in range(5)])
print('xk : ', [Abs(xk.subs(k, j).evalf()) for j in range(5)])
fig = plt.figure('Discrete Fourier Series')
fig.canvas.mpl_connect('key_press_event', on_key)
x_range = np.arange(-(N//2), N//2+1)
ax = fig.add_subplot(1, 2, 1)
xn_range = np.append(np.append(x_range-N, x_range), x_range+N)
xn_points = [xn.subs(n, j).evalf() for j in x_range]*3
ax.stem(xn_range, xn_points, linefmt='g-', basefmt='o', use_line_collection=True)
ax = fig.add_subplot(1, 2, 2)
xk_points = [Abs(xk.subs(k, j).evalf()) for j in x_range]*3
ax.stem(xn_range, xk_points, linefmt='g-', basefmt='o', use_line_collection=True)
ax.set_xlabel(r'$|X(k\Omega_0)|-k$')
plt.show()
sys.exit()
"""

#%% DTFT
"""
# 三角波序列
xn = Piecewise((0, (n < -1) | (n > 1)), (n+1, n < 0), (1-n, n >= 0))
# xW = fourier.dtft(xn)
xW = sy.fourier_transform(xn, n, W) # 因为dtft不能计算，使用ft来绘图
print('xn: ', [xn.subs(n, j).evalf() for j in range(5)])
print('xW: ', [Abs(xW.subs(W, j).evalf()) for j in range(5)])
fig = plt.figure('Discrete Time Fourier Transform')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(1, 2, 1)
xn_range = np.linspace(-2, 2, 51)
xn_points = [xn.subs(n, j).evalf() for j in xn_range]
ax.stem(xn_range, xn_points, linefmt='g-', basefmt='o', use_line_collection=True)
ax = fig.add_subplot(1, 2, 2)
xW_range = (np.linspace(-2*5, 2*5, 255))
xW_points = [Abs(xW.subs(W, j).evalf()) for j in xn_range]*5
ax.plot(xW_range, xW_points)
ax.set_xlabel(r'$|X(e^{j\Omega})|-\Omega$')
"""


#%% DFT and FFT
f = 16e3    # 采样频率16KHz
N = 1024    # 序列长度1000
t = np.linspace(0, N/f, N)
x = 7*np.sin(2*np.pi*6000*t) + 3*np.sin(2*np.pi*3000*t) + 5*np.sin(2*np.pi*800*t)
# w = fourier.dft(x, True)
# w = fourier.dft(x, False)
# xr = np.real(fourier.idft(w))
w = fourier.fft(x)  # 补零会频谱分布有些微影响
xr = np.real(fourier.ifft(w))
w = fourier.fftshift(w)
# w = np.fft.fftshift(np.fft.fft(x))
# w = np.fft.fft(x)
# xr = np.real(np.fft.ifft(w))
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
ax.set_xlim(0, 200)
ax = fig.add_subplot(1, 2, 2)
w_range = np.linspace(-f//2, f//2, w.size)
ax.plot(w_range[:int(w.size/2)], wabs[:int(w.size/2)], 'g-')
ax.plot(w_range[int(w.size/2):], wabs[int(w.size/2):], 'r-')
# ax.stem(w_range, wabs, linefmt='g-', basefmt='o', use_line_collection=True)
ax.set_xticks(np.linspace(-f//2, f//2, 9))
ax.set_xticklabels([str(n) for n in np.linspace(-f//2/1000, f//2/1000, 9)])
ax.set_xlabel(r'$KHz$')

plt.show()
sys.exit()
