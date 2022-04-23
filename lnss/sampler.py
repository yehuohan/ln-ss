#!/usr/bin/env python3


"""
* Mipmap:
    使用kernel提前采样的一系列texture。
    - Lower mipmap level  => Narrower kernel
    - Higher mipmap level => Wider kernel

* Coordinate:
    ---------> w/u/x
    | +-----+
    | |     |
    | +-----+
    V
    h/v/y

* Gradients:
    梯度为 (dU/dX, dV/dY)，dX=dY=1 表示用2x2的neighboring pixels计算梯度。
    - Smaller step size => Smaller gradient => High sampling rate => Narrower kernel
    - Larger step size  => Larger gradient  => Low sampling rate  => Wider kernel

* Scale:
    Wider kernel    => Narrower frequency domain function => Keep more lower frequency data  => Blurry
    Narrower kernel => Wider frequency domain function    => Keep more higher frequency data => Aliasing

* Anistropy:
    Different gradient of U and V dimension for texture mapping.
    Use different step size and kernel size for U and V dimension when generating mipmaps.
"""

import numpy as np

def sample(img:np.ndarray, dstshape:tuple, kernelshape:tuple):
    """Sample image

    高分辨率材质，采样到低分辨率图像上时，采样频率足够高，才能将足够的信息保留下来，减少aliasing。
    kernel size变大时，sum-average的pixels越多，相当于提高了采样频率。

    :Parameters:
        - img: original image at HWC
        - dstshape: sample shape at HW
        - kernelshape: kernal shape at HW
    """
    wid = dstshape[1]
    hei = dstshape[0]
    dx = float(img.shape[1]) / float(wid)
    dy = float(img.shape[0]) / float(hei)
    kx = kernelshape[1]
    ky = kernelshape[0]

    out = np.zeros((hei, wid, img.shape[-1]), dtype=img.dtype)
    for y in range(hei):
        for x in range(wid):
            yy = int(y * dy)
            xx = int(x * dx)
            out[y, x, :] = np.sum(img[yy:(yy+ky), xx:(xx+kx), :], axis=(0, 1)) / (kx * ky)

    return out

