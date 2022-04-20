#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier as fourier
import numpy as np
import matplotlib.pyplot as plt


N = 41

def gen():
    t = np.linspace(-1, 1, N)
    x = np.piecewise(t, [t < 0, t >= 0], [lambda t: 1 + t, lambda t: 1 - t])
    # 无论怎么截取x主周期，不会改变周期信号的频谱信息
    # x = np.append(x[N//3:], x[:N//3])
    return x

def calc(x):
    w = fourier.dft(x, True)
    xr = np.real(fourier.idft(w, True))
    amp = np.abs(w) / w.size
    print('Parseval - x: ', np.sum(np.abs(x)**2))
    print('Parseval - w: ', np.sum(np.abs(w)**2) / w.size)
    return (xr, amp)

def plot(x, xr, amp):
    fig = plt.figure('DFT')

    ax = fig.add_subplot(1, 2, 1)
    x_range = (np.arange(0, N) - N//2) / 2 # 绘图范围设到[-10, 10]
    ax.stem(x_range, x, linefmt='g-', basefmt='o', use_line_collection=True)
    # ax.stem(x_range, xr, linefmt='r-', basefmt='o', use_line_collection=True)

    ax = fig.add_subplot(1, 2, 2)
    ax.stem(x_range, amp, linefmt='g-', basefmt='o', use_line_collection=True)
    ax.set_xlabel(r'$|X(k)|-k$')
    plt.show()


plt.show()
x = gen()
xr, amp = calc(x)
plot(x, xr, amp)
