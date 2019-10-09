#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sy

def dct(xn:np.ndarray)->np.ndarray:
    """离散余弦变换

    使用矩陈乘法来计算乘积累加。

    :Parameters:
        - xn: 离散信号序列

    :Returns: DCT变换序列
    """
    N = xn.size
    n = k = np.arange(N).reshape(N, 1)
    wnk = np.cos(np.dot((2*n + 1) * np.pi / (2.0 * N), k.T))
    ck = np.sqrt(2.0 / N) * np.dot(xn, wnk)
    ck[0] = 1.0 / np.sqrt(N) * np.sum(xn)
    return ck

def idct(ck:np.ndarray)->np.ndarray:
    """离散余弦逆变换

    :Parameters:
        - xn: DCT变换序列

    :Returns: 离散信号序列
    """
    N = ck.size
    n = k = np.arange(N).reshape(N, 1)
    wnk = np.cos(np.dot((2*n + 1) * np.pi / (2.0 * N), k.T))
    xn = np.sqrt(2.0 / N) * np.dot(ck, wnk.T)
    xn += 1.0 / np.sqrt(N) * ck[0]
    return xn
