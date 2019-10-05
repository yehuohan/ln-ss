#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fourier（傅里叶）相关算法。

- FS(Fourier Series)
- FT(Fourier Transform)
- DFS(Discrete Time Fourier Series)
- DTFT(Discrete Time Fourier Transform)
- DFT(Discrete Fourier Transform)
- FFT(Fast Fourier Transform)
"""

import numpy as np
import sympy as sy

def fs(f, T:float, r:tuple=()):
    """计算傅里叶级数（一维信号）

    fs用于连续周期信号，这里基于符号运算库sympy进行计算。

    示例：

    ..  code:: python

        f = Piecewise((0, t < -0.5), (1, (-0.5 <= t) & (t <= 0.5)), (0, t > 0.5))
        (a0, an, bn, fn) = fs(f, 2, (t, -1, 1))
        print('a0 : ', a0.evalf())
        print('a1 : ', an.subs(n, 1).evalf())
        print('b1 : ', bn.subs(n, 1).evalf())
        print('f1 : ', Abs(fn.subs(n, 1).evalf()))

    :Parameters:
        - f: 基于sympy的周期连续函数表示，函数只能有1个自变量
        - T: 函数周期
        - r: 函数一个周期的范围

    :Returns: Fourier级数系数表达式，自变量符号为n
    """
    t = tuple(f.free_symbols)[0]    # 函数自变量符号
    if not r:
        r = (t, -T/2.0, T/2.0)      # 函数周期范围，积分范围
    n = sy.symbols('n')             # 级数自变量
    w = 2.0 * sy.pi / T
    a0 = 1.0 / T * sy.integrate(f, r)
    an = 2.0 / T * sy.integrate(f * sy.cos(n * w * t), r)
    bn = 2.0 / T * sy.integrate(f * sy.sin(n * w * t), r)
    fn = 1.0 / T * sy.integrate(f * sy.exp(-sy.I * n * w * t), r)
    return (a0, an, bn, fn)

def ft(f, r:tuple=()):
    """傅里叶变换

    :Parameters:

    :Returns:
    """
    t = tuple(f.free_symbols)[0]    # 函数自变量符号
    w = sy.symbols('w')
    if not r:
        r = (t, -sy.oo, sy.oo)
    fw = sy.integrate(f * sy.exp(-sy.I * w * t), r)
    return fw

def ift(f):
    pass

def dfs():
    pass

def dtft():
    pass

def dft():
    pass

def fft():
    pass
