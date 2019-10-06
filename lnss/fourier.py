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
        - ft: 连续周期函数，函数只能有1个自变量
        - T: 函数周期
        - r: 函数一个周期的范围

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
        - ft: 连续非周期函数，函数只能有1个自变量

    :Returns: 频谱密度函数，自变量符号为omega(用w表示)
    """
    t = tuple(ft.free_symbols)[0]
    w = sy.symbols('w')
    r = (t, -sy.oo, sy.oo)
    fw = sy.integrate(ft * sy.exp(-sy.I * w * t), r)
    return fw

def ift(fw):
    """傅里叶逆变换

    :Parameters:
        - fw: 频谱密度函数（连续非周期函数），函数只能有1个自变量

    :Returns: 返回原函数，函数自变量变为t
    """
    w = tuple(fw.free_symbols)[0]
    t = sy.symbols('t')
    r = (w, -sy.oo, sy.oo)
    ft = (1.0 / 2 * sy.pi) * sy.integrate(fw * sy.exp(sy.I * w * t), r)
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

    :Returns: 序列频谱（周期连续信号），自变量为Omega(用W表示)
    """
    n = tuple(xn.free_symbols)[0]
    W = sy.symbols('W')

def idtft(xW):
    W = tuple(xn.free_symbols)[0]
    n = sy.symbols('n')

def dft():
    pass

def fft():
    pass
