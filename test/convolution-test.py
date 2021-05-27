#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.convolution as convolution
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
from skimage import io as skio

mpl.rcParams['font.family'] = 'Consolas'
mpl.rcParams['font.size'] = 11

def on_key(event:mpl.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close()

k = np.matrix(
        [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]], dtype=np.float)
# k = np.matrix(
#         [[-1, -1, -1],
#          [-1,  9, -1],
#          [-1, -1, -1]], dtype=np.float)
k = np.matrix(
        [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]], dtype=np.float)
# img = np.matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
img = skio.imread('pic2.jpg', as_gray=True)
imgf = convolution.conv2d(img, k, True)
# imgf = sp.signal.convolve2d(img, k)

# print(img)
# print(imgf)
plt.figure('Convolution')
plt.connect('key_press_event', on_key)
plt.subplot(1, 2, 1)
plt.title('img')
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('img filter')
plt.imshow(imgf, cmap='gray')
plt.show()
