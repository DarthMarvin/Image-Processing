#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 04:33:55 2020

@author: carlos
"""

import numpy as np
from astropy.io import fits
import os
import glob

# Filter configurations: 1 = L, 2 = RGB, 3 = LRGB 4 = HOS, 5 = LRGBH, 6 = RGBH, 7 = H
FC = input('Filter configuration: ')
FC = int(FC)

def MasterF(filenames,datasum,N):
    for x in filenames:
        data = fits.getdata(x)
        datasum = np.add(datasum,data)
    Avg = datasum/N
    return Avg

datasum = np.zeros((582,752),dtype = int)
if FC == 1 or FC == 3 or FC == 5:
    datasum = np.zeros((582,752),dtype = int)
    os.chdir('/home/carlos/Desktop/Astrophotography/Luminance/Calibrated/Aligned')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    MasterL = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = MasterL
    hdu.writeto('MasterL.fit')
if FC == 2 or FC == 3 or FC == 5 or FC == 6:
    datasum = np.zeros((582,752),dtype = int)
    os.chdir('/home/carlos/Desktop/Astrophotography/Red/Calibrated/Aligned')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    MasterR = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = MasterR
    hdu.writeto('MasterR.fit')
    datasum = np.zeros((582,752),dtype = int)
    os.chdir('/home/carlos/Desktop/Astrophotography/Green/Calibrated/Aligned')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    MasterG = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = MasterG
    hdu.writeto('MasterG.fit')
    datasum = np.zeros((582,752),dtype = int)
    os.chdir('/home/carlos/Desktop/Astrophotography/Blue/Calibrated/Aligned')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    MasterB = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = MasterB
    hdu.writeto('MasterB.fit')
if FC == 4 or FC == 5 or FC == 6 or FC == 7:
    datasum = np.zeros((582,752),dtype = int)
    os.chdir('/home/carlos/Desktop/Astrophotography/Halpha/Calibrated/Aligned')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    MasterH = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = MasterH
    hdu.writeto('MasterH.fit')
if FC == 4:
    datasum = np.zeros((582,752),dtype = int)
    os.chdir('/home/carlos/Desktop/Astrophotography/O3/Calibrated/Aligned')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    MasterO = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = MasterO
    hdu.writeto('MasterO.fit')
    datasum = np.zeros((582,752),dtype = int)
    os.chdir('/home/carlos/Desktop/Astrophotography/S2/Calibrated/Aligned')
    filenames = glob.glob('*.fit')
    N = len(filenames)
    MasterS = MasterF(filenames,datasum,N)
    hdu = fits.PrimaryHDU()
    hdu.data = MasterS
    hdu.writeto('MasterS.fit')