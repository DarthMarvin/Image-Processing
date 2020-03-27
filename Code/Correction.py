#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:19:31 2020

@author: carlos
"""

import numpy as np
from astropy.io import fits
import os
import glob

# Filter configurations: 1 = L, 2 = RGB, 3 = LRGB 4 = HOS, 5 = LRGBH, 6 = RGBH, 7 = H
FC = input('Filter configuration: ')
FC = int(FC)
os.chdir('/home/carlos/Desktop/Astrophotography/Dark')
MasterDark = fits.getdata('MasterDark.fit')
def Correction(data,MasterDark,MasterFlat,FAvg):
    data = fits.getdata(x)
    correction = np.divide((np.subtract(data,MasterDark)*FAvg),np.subtract(MasterFlat,MasterDark))
    return correction
if FC == 1 or FC == 3 or FC == 5:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatL')
    MasterFlat = fits.getdata('MasterLF.fit')
    FAvg = np.average(MasterFlat)
    os.chdir('/home/carlos/Desktop/Astrophotography/Luminance')
    filenames = glob.glob('*.fit')
    for x in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Luminance')
        data = fits.getdata(x)
        CorrectionL = Correction(data,MasterDark,MasterFlat,FAvg)
        hdu = fits.PrimaryHDU()
        hdu.data = CorrectionL
        os.chdir('/home/carlos/Desktop/Astrophotography/Luminance/Calibrated')
        hdu.writeto('C%s' % (x))
if FC == 2 or FC == 3 or FC == 5 or FC == 6:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatR')
    MasterFlat = fits.getdata('MasterRF.fit')
    FAvg = np.average(MasterFlat)
    os.chdir('/home/carlos/Desktop/Astrophotography/Red')
    filenames = glob.glob('*.fit')
    for x in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Red')
        data = fits.getdata(x)
        CorrectionR = Correction(data,MasterDark,MasterFlat,FAvg)
        hdu = fits.PrimaryHDU()
        hdu.data = CorrectionR
        os.chdir('/home/carlos/Desktop/Astrophotography/Red/Calibrated')
        hdu.writeto('C%s' % (x))
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatG')
    MasterFlat = fits.getdata('MasterGF.fit')
    FAvg = np.average(MasterFlat)
    os.chdir('/home/carlos/Desktop/Astrophotography/Green')
    filenames = glob.glob('*.fit')
    for x in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Green')
        data = fits.getdata(x)
        CorrectionG = Correction(data,MasterDark,MasterFlat,FAvg)
        hdu = fits.PrimaryHDU()
        hdu.data = CorrectionG
        os.chdir('/home/carlos/Desktop/Astrophotography/Green/Calibrated')
        hdu.writeto('C%s' % (x))
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatB')
    MasterFlat = fits.getdata('MasterBF.fit')
    FAvg = np.average(MasterFlat)
    os.chdir('/home/carlos/Desktop/Astrophotography/Blue')
    filenames = glob.glob('*.fit')
    for x in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Blue')
        data = fits.getdata(x)
        CorrectionB = Correction(data,MasterDark,MasterFlat,FAvg)
        hdu = fits.PrimaryHDU()
        hdu.data = CorrectionB
        os.chdir('/home/carlos/Desktop/Astrophotography/Blue/Calibrated')
        hdu.writeto('C%s' % (x))
if FC == 4 or FC == 5 or FC == 6 or FC == 7:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatH')
    MasterFlat = fits.getdata('MasterHF.fit')
    FAvg = np.average(MasterFlat)
    os.chdir('/home/carlos/Desktop/Astrophotography/HAlpha')
    filenames = glob.glob('*.fit')
    for x in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/HAlpha')
        data = fits.getdata(x)
        CorrectionH = Correction(data,MasterDark,MasterFlat,FAvg)
        hdu = fits.PrimaryHDU()
        hdu.data = CorrectionH
        os.chdir('/home/carlos/Desktop/Astrophotography/HAlpha/Calibrated')
        hdu.writeto('C%s.fit' % (x))
if FC == 4:
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatO')
    MasterFlat = fits.getdata('MasterOF.fit')
    FAvg = np.average(MasterFlat)
    os.chdir('/home/carlos/Desktop/Astrophotography/O3')
    filenames = glob.glob('*.fit')
    for x in filenames:
        ('/home/carlos/Desktop/Astrophotography/O3')
        data = fits.getdata(x)
        CorrectionO = Correction(data,MasterDark,MasterFlat,FAvg)
        hdu = fits.PrimaryHDU()
        hdu.data = CorrectionO
        os.chdir('/home/carlos/Desktop/Astrophotography/O3/Calibrated')
        hdu.writeto('C%s' % (x))
    os.chdir('/home/carlos/Desktop/Astrophotography/FlatS')
    MasterFlat = fits.getdata('MasterLF.fit')
    FAvg = np.average(MasterFlat)
    os.chdir('/home/carlos/Desktop/Astrophotography/S2')
    filenames = glob.glob('*.fit')
    for x in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/S2')
        data = fits.getdata(x)
        CorrectionS = Correction(data,MasterDark,MasterFlat,FAvg)
        hdu = fits.PrimaryHDU()
        hdu.data = CorrectionS
        os.chdir('/home/carlos/Desktop/Astrophotography/S2/Calibrated')
        hdu.writeto('C%s' % (x))