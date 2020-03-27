#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:57:40 2020

@author: carlos
"""

# Average all the Dark frames to create a master dark frame

import numpy as np
from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
import os
import glob
from matplotlib.colors import LogNorm

os.chdir('/home/carlos/Desktop/Astrophotography/Dark')
filenames = glob.glob('*.fit')
N = len(filenames)
datasum = np.zeros((582,752),dtype = int)
for x in filenames:
    data = fits.getdata(x)
    datasum = np.add(datasum,data)
Avg = datasum/N
hdu = fits.PrimaryHDU()
hdu.data = Avg
hdu.writeto('MasterDark.fit')
plt.imshow(Avg, cmap='gray', norm=LogNorm())