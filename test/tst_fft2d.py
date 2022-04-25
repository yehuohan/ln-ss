#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier2d as fourier2d
import lnss.utils as utils
import numpy as np
import matplotlib.pyplot as plt

def gen():
    # M = N = 256
    # img = np.matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    # img = np.zeros((M, M), dtype=np.uint8)
    # img[M//2-5:M//2+5,N//2-5:N//2+5] = 255
    import skimage
    img = skimage.io.imread('pic.jpg', as_gray=True)
    return img

def calc(img):
    imgf = fourier2d.dft2d(img)
    imgr = np.real(fourier2d.idft2d(
        fourier2d.shift2d(
            fourier2d.shift2d(imgf) * \
            fourier2d.butterworth(utils.gen_indices(img.shape), 5))
        ))

    # imgf = fourier2d.fft2d(img)
    # imgr = np.real(fourier2d.ifft2d(imgf))

    # imgamp = fourier2d.amp2d(fourier2d.shift2d(imgf))
    imgamp = fourier2d.amp2d_log10(fourier2d.shift2d(imgf))
    return (imgr, imgamp)

def calc_np(img):
    imgf = np.fft.fft2(img)
    imgr = np.real(np.fft.ifft2(imgf))
    imgamp = np.abs(np.fft.fftshift(imgf))
    return (imgr, imgamp)

def plot(img, imgr, imgamp):
    M, N = img.shape
    plt.figure('DFT2D and FFT2D')
    plt.subplot(2, 2, 1)
    plt.title('img')
    plt.imshow(img, cmap='gray')

    plt.subplot(2, 2, 2)
    plt.title('img spectrum')
    plt.imshow(imgamp / np.max(imgamp), cmap='gray')

    plt.subplot(2, 2, 3)
    plt.title('img spectrum inverse')
    plt.imshow(imgr, cmap='gray')

    ax = plt.subplot(2, 2, 4, projection='3d')
    plt.title('img spectrum 3d')
    x, y = np.meshgrid(np.arange(M), np.arange(N))
    ax.plot_surface(x, y, imgamp, shade=True, cmap='jet')
    plt.show()


img = gen()
imgr, imgamp = calc(img)
# imgr, imgamp = calc_np(img)
plot(img, imgr, imgamp)


