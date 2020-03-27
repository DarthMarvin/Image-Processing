#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:40:58 2020

@author: carlos
"""

import numpy as np
from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
import os
import glob
from matplotlib.colors import LogNorm

# Filter configurations: 1 = L, 2 = RGB, 3 = LRGB 4 = HOS, 5 = LRGBH, 6 = RGBH, 7 = H
FC = input('Filter configuration: ')
FC = int(FC)
datasum = np.zeros((582,752),dtype = int)
def MasterF(filenames,datasum,N):
    for x in filenames:
        data = fits.getdata(x)
        datasum = np.add(datasum,data)
    Avg = datasum/N
    return Avg
if FC == 1 or FC == 3 or FC == 5:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatL')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    AvgLF = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = AvgLF
    hdu.writeto('MasterLF.fit')
#    plt.imshow(AvgLF, cmap='gray', norm=LogNorm())
#    image_hist = plt.hist(AvgLF.flatten(), 1000)
if FC == 2 or FC == 3 or FC == 5 or FC == 6:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatR')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    AvgRF = MasterF(filenames,datasum,N)
    hdu.data = AvgRF
    hdu = fits.PrimaryHDU()
    hdu.data = AvgRF
    hdu.writeto('MasterRF.fit')
#    plt.imshow(AvgRF, cmap='gray', norm=LogNorm())
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatG')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    AvgGF = MasterF(filenames,datasum,N)
    hdu.data = AvgGF
    hdu = fits.PrimaryHDU()
    hdu.data = AvgGF
    hdu.writeto('MasterGF.fit')
#    plt.imshow(AvgGF, cmap='gray', norm=LogNorm())
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatB')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    AvgBF = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = AvgBF
    hdu = fits.PrimaryHDU()
    hdu.data = AvgBF
    hdu.writeto('MasterBF.fit')
#    plt.imshow(AvgBF, cmap='gray', norm=LogNorm())
if FC == 4 or FC == 5 or FC == 6 or FC == 7:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatH')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    AvgHF = MasterF(filenames,datasum,N)
    hdu.data = AvgHF
    hdu = fits.PrimaryHDU()
    hdu.data = AvgHF
    hdu.writeto('MasterHF.fit')
#    plt.imshow(AvgHF, cmap='gray', norm=LogNorm())
if FC == 4:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatO')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    AvgOF = MasterF(filenames,datasum,N)
    hdu.data = AvgOF
    hdu = fits.PrimaryHDU()
    hdu.data = AvgOF
    hdu.writeto('MasterOF.fit')
#    plt.imshow(AvgOF, cmap='gray', norm=LogNorm())
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatS')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    AvgSF = MasterF(filenames,datasum,N)
    hdu.data = AvgSF
    hdu = fits.PrimaryHDU()
    hdu.data = AvgSF
    hdu.writeto('MasterSF.fit')
#    plt.imshow(AvgSF, cmap='gray', norm=LogNorm())