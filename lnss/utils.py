#!/usr/bin/env python3

import numpy as np


def gen_indices(shape):
    hei = shape[0]
    wid = shape[1]
    cc, rr = np.meshgrid(np.arange(wid), np.arange(hei))
    rc = np.column_stack((rr.flat, cc.flat))
    indices = np.reshape(rc, (hei, wid, 2))
    return indices
