#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier as fourier
import numpy as np
import sympy as sy
from sympy import Piecewise, Abs
from sympy.abc import W, n
from matplotlib.backend_bases import KeyEvent
import matplotlib.pyplot as plt


def on_key(event:KeyEvent):
    if event.key == 'escape':
        plt.close()


#%% DTFT
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

plt.show()
sys.exit()
