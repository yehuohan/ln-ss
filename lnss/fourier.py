#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fourier（傅里叶）变换相关计算。

此模块只适用于一维信号，以下4个计算基于sympy符号运算库实现（直接套公式）：

- FS(Fourier Series)
- FT(Fourier Transform)
- DFS(Discrete Time Fourier Series)
- DTFT(Discrete Time Fourier Transform)

以下2个变换计算基于numpy运算库实现：

- DFT(Discrete Fourier Transform)
- FFT(Fast Fourier Transform)
"""

import numpy as np
import sympy as sy

def fs(ft, T:float, r:tuple=()):
    """傅里叶级数

    示例（周期矩形波）：

    ..  code:: python

        ft = Piecewise((0, t < -0.5), (1, (-0.5 <= t) & (t <= 0.5)), (0, t > 0.5))
        (a0, an, bn, fn) = fs(ft, 2, (t, -1, 1))
        print('a0 : ', a0.evalf())
        print('a1 : ', an.subs(n, 1).evalf())
        print('b1 : ', bn.subs(n, 1).evalf())
        print('f1 : ', Abs(fn.subs(n, 1).evalf()))

    :Parameters:
        - ft: 连续周期信号，只能有1个自变量
        - T: 信号周期
        - r: 信号一个周期的范围

    :Returns: Fourier级数系数表达式，自变量符号为n
    """
    t = tuple(ft.free_symbols)[0]    # 函数自变量符号
    if not r:
        r = (t, -T/2.0, T/2.0)      # 函数周期范围，积分范围
    n = sy.symbols('n')             # 级数自变量
    w = 2.0 * sy.pi / T
    a0 = 1.0 / T * sy.integrate(ft, r)
    an = 2.0 / T * sy.integrate(ft * sy.cos(n * w * t), r)
    bn = 2.0 / T * sy.integrate(ft * sy.sin(n * w * t), r)
    fn = 1.0 / T * sy.integrate(ft * sy.exp(-sy.I * n * w * t), r)
    return (a0, an, bn, fn)

def ft(ft):
    """傅里叶变换

    示例（矩形脉冲波）：

    ..  code:: python

        tau = 1
        ft = Piecewise((0, t < -tau/2.0), (1, (-tau/2.0 <= t) & (t <= tau/2.0)), (0, t > tau/2.0))
        fw = fourier.ft(ft)
        print(Abs(fw.subs(w, 0).evalf()))

    :Parameters:
        - ft: 连续非周期信号，信号只能有1个自变量

    :Returns: 频谱密度函数（连续非周期信号），自变量符号为omega(用w表示)
    """
    t = tuple(ft.free_symbols)[0]
    w = sy.symbols('w')
    r = (t, -sy.oo, sy.oo)
    fw = sy.integrate(ft * sy.exp(-sy.I * w * t), r)
    return fw

def ift(fw):
    """傅里叶逆变换

    :Parameters:
        - fw: 频谱密度函数（连续非周期信号），信号只能有1个自变量

    :Returns: 返回原信号，信号自变量变为t
    """
    w = tuple(fw.free_symbols)[0]
    t = sy.symbols('t')
    r = (w, -sy.oo, sy.oo)
    ft = (1.0 / (2 * sy.pi)) * sy.integrate(fw * sy.exp(sy.I * w * t), r)
    return ft

def dfs(xn, N:int, r:tuple=()):
    """离散傅里叶级数

    示例（三角波）：

    ..  code:: python

        N = 21
        xn = Piecewise((n/10+1, n < 0), (1-n/10, n >= 0))
        xk = fourier.dfs(xn, N, (n, -(N//2), N//2))
        print(Abs(xk.subs(k, 1).evalf()))

    :Parameters:
        - xn: 离散周期序列，序列只能有1个自变量
        - N: 序列最小数字周期
        - r: 序列一个周期的范围

    :Returns: 频谱序列（离散周期序列），自变量为k
    """
    n = tuple(xn.free_symbols)[0]
    k = sy.symbols('k')
    if not r:
        r = (n, 0, N-1)
    W = sy.exp(-sy.I * 2 * sy.pi * k * n / N)
    xk = sy.Sum(xn * W, r)
    return xk

def idfs(xk, N:int, r:tuple=()):
    """离散傅里叶级数逆运算

    :Parameters:
        - xk: 离散周期频谱序列，序列只能有1个自变量
        - N: 序列最小数字周期
        - r: 序列一个周期的范围

    :Returns: 原信号序列（离散周期序列），序列自变量为n
    """
    k = tuple(xk.free_symbols)[0]
    n = sy.symbols('n')
    if not r:
        r = (k, 0, N-1)
    W = sy.exp(sy.I * 2 * sy.pi * k * n / N)
    xn = sy.Sum(xk * W, r) / N
    return xn

def dtft(xn):
    """离散时间傅里叶变换

    :Parameters:
        - xn: 离散非周期序列，序列只能有1个自变量

    :Returns: 频谱密度函数（周期连续信号），自变量为Omega(用W表示)
    """
    raise Exception("Can't sum from -oo to oo")
    n = tuple(xn.free_symbols)[0]
    W = sy.symbols('W')
    r = (n, -sy.oo, sy.oo)
    xW = sy.Sum(xn * sy.exp(-sy.I * W * n), r)
    return xW

def idtft(xW):
    """离散时间傅里叶逆变换

    :Parameters:
        - xW: 频谱密度函数（周期连续信号），信号只能有一个自变量

    :Returns: 原信号序列（离散非周期序列），序列自变量为n
    """
    W = tuple(xW.free_symbols)[0]
    n = sy.symbols('n')
    r = (W, 0, 2 * sy.pi)
    xn = (1.0 / (2 * sy.pi)) * sy.integrate(xW * sy.exp(sy.I * W * n), r)
    return xn

def dft(xn:np.ndarray):
    """离散傅里叶变换

    默认DFT是对[0, N)之间的点进行变换，得到的频谱也是[0, N)，所以在
    不进行shift的情况下，频谱并不是关于零频率对称的（DFT是DFS时域和
    频率的主值周期，参照DFS的演示图理解）。

    这里使用矩陈乘法来计算乘积累加。

    :Parameters:
        - xn: 离散信号序列

    :Returns: 频谱信号序列
    """
    N = xn.size
    n = k = np.arange(N).reshape(N, 1)
    wnk = np.exp((-1j * 2 * np.pi / N) * np.dot(n, k.T))
    xk = np.dot(xn, wnk.T)
    return xk

def idft(xk:np.ndarray):
    """离散傅里叶逆变换

    :Parameters:
        - xk: 频谱信号序列

    :Returns: 离散信号序列
    """
    N = xk.size
    n = k = np.arange(N).reshape(N, 1)
    wnk = np.exp(-(-1j * 2 * np.pi / N) * np.dot(n, k.T))
    xn = np.dot(xk, wnk) / N
    return xn

def _fft(x:np.ndarray, inv:bool):
    """基2时分法计算DFT和IDFT

    :Parameters:
        - x: 离散信号序列（或频谱信号序列）
        - inv: 是否为逆变换

    :Returns: 频谱信号序列（或离散信号序列）
    """
    N = x.size
    wn = np.exp(-1j * 2 * np.pi / N)
    xt = x = x.astype(dtype=np.complex128)
    if N >= 2:
        xt = np.append(_fft(x[::2], inv),  _fft(x[1::2], inv))
        alpha = 0.5 if inv else 1.0
        for k in range(N//2):
            val = xt[k]
            wnk = np.power(wn, (-k if inv else k))
            # 递归计算式
            xt[k]        = alpha * (val + wnk * xt[k + N//2])
            xt[k + N//2] = alpha * (val - wnk * xt[k + N//2])

    return xt

def fft(x:np.ndarray, N:int=None):
    """快速傅里叶变换

    使用基2时分法。

    :Parameters:
        - x: 离散信号序列
        - N: 傅里叶变换区间长度，必须为2的整数幂

    :Returns: 频谱信号序列
    """
    if N == None or N < x.size:
        N = int(np.exp2(np.ceil(np.log2(x.size))))
    if N == x.size:
        xn = x
    else:
        xn = np.append(x, np.zeros((N-x.size), dtype=x.dtype))
    xk = _fft(xn, False)
    return xk

def fftshift(x:np.ndarray):
    """平移FFT频谱

    FFT默认频谱不是关于零频率对称的，使用fftshift可以对调左右频谱。

    :Parameters:
        - x: 频谱序列

    :Returns: 平移后的频谱
    """
    N = x.size
    return np.append(x[N//2:], x[:N//2])

def ifft(xk:np.ndarray):
    """快速傅里叶逆变换

    使用基2时分法。

    :Parameters:
        - xk: 频谱信号序列，序列长度必须为2的整数幂

    :Returns: 离散信号序列
    """
    xn = _fft(xk, True)
    return xn
