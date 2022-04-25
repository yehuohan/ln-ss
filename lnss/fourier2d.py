#!/usr/bin/env python3

"""
二维离散傅里叶(Fourier)变换
"""

from .fourier import fft
from .fourier import ifft
import numpy as np


def dft2d(fxy:np.ndarray):
    """二维离散傅里叶变换

    :Parameters:
        - fxy: 二维离散序列

    :Returns: 二维频谱序列
    """
    M,N = fxy.shape
    m = np.arange(M).reshape(M, 1)
    n = np.arange(N).reshape(N, 1)
    wm = np.exp((-2j * np.pi / M) * np.dot(m, m.T))
    wn = np.exp((-2j * np.pi / N) * np.dot(n, n.T))
    fuv = np.dot(np.dot(wm, fxy), wn)   # wm和wn为对称矩阵，不用提心转置问题
    return fuv

def idft2d(fuv:np.ndarray):
    """二维离散傅里叶逆变换

    :Parameters:
        - fuv: 二维频谱序列

    :Returns: 二维离散序列
    """
    M,N = fuv.shape
    m = np.arange(M).reshape(M, 1)
    n = np.arange(N).reshape(N, 1)
    wm = np.exp((2j * np.pi / M) * np.dot(m, m.T))
    wn = np.exp((2j * np.pi / N) * np.dot(n, n.T))
    fxy = np.dot(np.dot(wm, fuv), wn) / (M * N)  # wm和wn为对称矩阵，不用提心转置问题
    return fxy

def fft2d(fxy:np.ndarray):
    """二维离散傅里叶变换

    基于一维fft计算太慢，可以考虑使用原位计算优化。
    """
    M,N = fxy.shape
    fuv = np.zeros((M, N), dtype=np.complex128)
    for k in np.arange(M):
        fuv[k, :] = fft(fxy[k, :])
    for k in np.arange(N):
        fuv[:, k] = fft(fuv[:, k])
    return fuv

def ifft2d(fuv:np.ndarray):
    """二维离散傅里叶逆变换"""
    M,N = fuv.shape
    fxy = np.zeros((M, N), dtype=np.complex128)
    for k in np.arange(M):
        fxy[k, :] = ifft(fuv[k, :])
    for k in np.arange(N):
        fxy[:, k] = ifft(fxy[:, k])
    return fxy

def shift2d(img:np.ndarray):
    """平移二维序列

    :Parameters:
        - img: 二维序列

    :Returns: 平移后的序列
    """
    M,N = img.shape
    s = np.zeros((M, N), dtype=img.dtype)
    mu = int(np.ceil(M / 2))
    md = int(np.trunc(M / 2))
    nu = int(np.ceil(N / 2))
    nd = int(np.trunc(N / 2))
    s[:md, :nd] = img[mu:, nu:]
    s[:md, nd:] = img[mu:, :nu]
    s[md:, :nd] = img[:mu, nu:]
    s[md:, nd:] = img[:mu, :nu]
    return s

def amp2d(fuv):
    """计算频变幅值"""
    return np.abs(fuv)

def amp2d_log10(fuv):
    """计算log10的频谱"""
    return np.log10(np.abs(fuv))

def pha2d(fuv):
    """计算频谱的相位"""
    return np.arctan2(np.imag(fuv), np.real(fuv))

def butterworth(index: np.ndarray, d0, n=1) -> np.ndarray:
    """巴特沃斯低通滤波

    H(u, v) = 1 / (1 + (d/d0)^(2n))
    """
    dd0 = np.sum((index - np.array(index.shape[0:2]) / 2.0) ** 2, axis=-1) / (d0 ** 2)
    return 1.0 / (1.0 + dd0 ** n)
