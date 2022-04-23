#!/usr/bin/env python3

import sys,os
sys.path.append(os.getcwd() + '/../')

import lnss.sampler as sampler
import matplotlib.pyplot as plt
import skimage


img = skimage.io.imread('brickwall.jpg')
print(img.shape)
out = sampler.sample(img, (128, 256), (8, 4))
# out = sampler.sample(img, (128, 256), (1, 1))

plt.figure('Sample')
plt.subplot(1, 2, 1)
plt.imshow(img, interpolation=None)
plt.subplot(1, 2, 2)
plt.imshow(out, interpolation=None)
plt.imsave('out.png', out)
plt.show()

