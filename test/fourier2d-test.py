#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.fourier2d as fourier2d
import numpy as np
from matplotlib.backend_bases import KeyEvent
import matplotlib.pyplot as plt
import skimage

def on_key(event:KeyEvent):
    if event.key == 'escape':
        plt.close()

#%% DFT2D and FFT2D
# img = np.matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
M = N = 256
# img = np.zeros((M, M), dtype=np.uint8)
# img[M//2-5:M//2+5,N//2-5:N//2+5] = 255
img = skimage.io.imread('pic.jpg', as_gray=True)
M, N = img.shape
imgf = fourier2d.dft2d(img)
imgr = np.real(fourier2d.idft2d(imgf))
imgf = fourier2d.fft2d_shift(np.abs(imgf))
# imgf = fourier2d.fft2d(img)
# imgr = np.real(fourier2d.ifft2d(imgf))
# imgf = fourier2d.fft2d_shift(np.abs(imgf))
# imgf = np.fft.fft2(img)
# imgr = np.real(np.fft.ifft2(imgf))
# imgf = np.fft.fftshift(np.abs(imgf))
imgfn = imgf / np.max(imgf) * 255

plt.figure('DFT2D and FFT2D')
plt.connect('key_press_event', on_key)
plt.subplot(2, 2, 1)
plt.title('img')
plt.imshow(img, cmap='gray')

plt.subplot(2, 2, 2)
plt.title('img spectrum')
plt.imshow(imgfn, cmap='gray')

plt.subplot(2, 2, 3)
plt.title('img spectrum inverse')
plt.imshow(imgr, cmap='gray')

ax = plt.subplot(2, 2, 4, projection='3d')
plt.title('img spectrum 3d')
x, y = np.meshgrid(np.arange(M), np.arange(N))
ax.plot_surface(x, y, imgf, shade=True, cmap='jet')
plt.show()
