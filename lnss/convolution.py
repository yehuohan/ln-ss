#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def conv2d(img:np.matrix, kern:np.matrix, flip:bool=False):
    """二维卷积运算

    :Parameters:
        - img: 图像
        - kern: 卷积核
        - flip: 是否翻转卷积核

    :Returns: 卷积后的图像
    """
    # 扩充边缘
    m = kern.shape[0] // 2
    h, w = img.shape
    _img = np.zeros((h+2*m, w+2*m), dtype=img.dtype)
    _img[m:h+m, m:w+m] = img[:,:]
    # 翻转卷积核
    size = kern.size
    _kern = kern[::-1, ::-1] if flip else kern
    _kern = _kern.reshape(size, 1)
    # 卷积
    dsr = np.zeros((h, w), dtype=img.dtype)
    for r in np.arange(h):
        for c in np.arange(w):
            dsr[r,c] = np.dot(
                    _img[r:r+2*m+1, c:c+2*m+1].reshape((1, size)),
                    _kern)
    return dsr

def conv2drgb(img:np.ndarray, kern:np.matrix, flip:bool=False):
    """基于conv2d计算3通道图像卷积"""
    dsr = np.zeros(img.shape, dtype=img.dtype)
    dsr[:,:,0] = conv2d(np.mat(img[:,:,0]), kern, flip)
    dsr[:,:,1] = conv2d(np.mat(img[:,:,1]), kern, flip)
    dsr[:,:,2] = conv2d(np.mat(img[:,:,2]), kern, flip)
    return dsr
