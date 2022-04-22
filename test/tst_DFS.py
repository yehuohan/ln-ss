#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier as fourier
import numpy as np
from sympy import Piecewise, Abs
from sympy.abc import n, k
from matplotlib.backend_bases import KeyEvent
import matplotlib.pyplot as plt

def on_key(event:KeyEvent):
    if event.key == 'escape':
        plt.close()

#%% DFS
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
