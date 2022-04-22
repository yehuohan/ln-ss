#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier as fourier
import numpy as np
import matplotlib.pyplot as plt



f = 16e3    # 采样频率16KHz
N = 1024    # 序列长度1000

def gen():
    t = np.linspace(0, N/f, N)
    x = 7*np.sin(2*np.pi*6000*t) + 3*np.sin(2*np.pi*3000*t) + 5*np.sin(2*np.pi*800*t)
    return x

def calc(x):
    w = fourier.fft(x)  # 补零会频谱分布有些微影响
    xr = np.real(fourier.ifft(w))
    w = fourier.fftshift(w)
    amp = np.abs(w) / w.size
    print('Parseval - x: ', np.sum(np.abs(x)**2))
    print('Parseval - w: ', np.sum(np.abs(w)**2) / w.size)
    return (xr, amp)

def calc_np(x):
    w = np.fft.fft(x)
    xr = np.real(np.fft.ifft(w))
    w = np.fft.fftshift(w)
    amp = np.abs(w) / w.size
    print('Parseval - x: ', np.sum(np.abs(x)**2))
    print('Parseval - w: ', np.sum(np.abs(w)**2) / w.size)
    return (xr, amp)

def plot(x, xr, amp):
    fig = plt.figure('FFT')

    ax = fig.add_subplot(1, 2, 1)
    x_range = np.arange(N)
    # ax.stem(x_range, x, linefmt='g-', basefmt='o', use_line_collection=True)
    ax.plot(x_range, x, '-')
    ax.plot(np.arange(xr.size), xr, 'r-')

    ax = fig.add_subplot(1, 2, 2)
    K = amp.size
    w_range = np.linspace(-f//2, f//2, K)
    ax.plot(w_range[:int(K/2)], amp[:int(K/2)], 'g-')
    ax.plot(w_range[int(K/2):], amp[int(K/2):], 'r-')
    # ax.stem(w_range, amp, linefmt='g-', basefmt='o', use_line_collection=True)
    ax.set_xticks(np.linspace(-f//2, f//2, 9))
    ax.set_xticklabels([str(n) for n in np.linspace(-f//2/1000, f//2/1000, 9)])
    ax.set_xlabel(r'$KHz$')

    plt.show()


x = gen()
xr, amp = calc(x)
# xr, amp = calc_np(x)
plot(x, xr, amp)
