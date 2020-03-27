#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:10:20 2020

@author: carlos
"""

import numpy as np
from astropy.io import fits
import os
import glob
from astropy.nddata import Cutout2D
from astropy import units

#Filter configurations: 1 = L, 2 = RGB, 3 = LRGB 4 = HOS, 5 = LRGBH, 6 = RGBH, 7 = H
FC = input('Filter configuration: ')
FC = int(FC)

os.chdir('/home/carlos/Desktop/Astrophotography/Luminance/Calibrated')
filenames = glob.glob('*.fit')
ReferenceData = fits.getdata(filenames[0])
coord = np.where(ReferenceData == np.amax(ReferenceData))
print(coord)

Rows = np.arange(582)
Columns = np.arange(752)
if FC == 1 or FC == 3 or FC == 5:
    Counter = 0
    os.chdir('/home/carlos/Desktop/Astrophotography/Luminance/Calibrated')
    filenames = glob.glob('*.fit')
    for name in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Luminance/Calibrated')
        data = fits.getdata(name)
        crop_center = (coord[1],coord[0])
        crop_size = units.Quantity((41,41),units.pixel)
        crop = Cutout2D(data,crop_center,crop_size)
        coordM = np.where(crop.data == np.amax(crop.data))
        coordF = [coordM[0]-20+coord[0],coordM[1]-20+coord[1]]
        diff = [coordF[0]-coord[0],coordF[1]-coord[1]]
        newarr = np.ones((582,752),dtype = int)
        Median = np.median(data)
        newarr = newarr*Median
        for x in Rows:
            if x + diff[0] < 0 or x + diff[0] > np.amax(Rows):
                pass
            else:
                y = x
                for x in Columns:
                    if x + diff[1] < 0 or x + diff[1] > np.amax(Columns):
                        pass
                    else:
                        newarr[y,x] = data[y+diff[0],x+diff[1]]
        os.chdir('/home/carlos/Desktop/Astrophotography/Luminance/Calibrated/Aligned')
        hdu = fits.PrimaryHDU()
        hdu.data = newarr
        hdu.writeto('A%s' % (name))
        Counter = Counter+1
        print(Counter)
if FC == 2 or FC == 3 or FC == 5 or FC == 6:
    Counter = 0
    os.chdir('/home/carlos/Desktop/Astrophotography/Red/Calibrated')
    filenames = glob.glob('*.fit')
    for name in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Red/Calibrated')
        data = fits.getdata(name)
        crop_center = (coord[1],coord[0])
        crop_size = units.Quantity((41,41),units.pixel)
        crop = Cutout2D(data,crop_center,crop_size)
        coordM = np.where(crop.data == np.amax(crop.data))
        coordF = [coordM[0]-20+coord[0],coordM[1]-20+coord[1]]
        diff = [coordF[0]-coord[0],coordF[1]-coord[1]]
        newarr = np.ones((582,752),dtype = int)
        Min = np.amin(data)
        newarr = newarr*Min
        for x in Rows:
            if x - diff[0] < 0 or x-diff[0] > np.amax(Rows):
                pass
            else:
                y = x
                for x in Columns:
                    if x - diff[1] < 0 or x-diff[1] > np.amax(Columns):
                        pass
                    else:
                        newarr[y,x] = data[y-diff[0],x-diff[1]]
        os.chdir('/home/carlos/Desktop/Astrophotography/Red/Calibrated/Aligned')
        hdu = fits.PrimaryHDU()
        hdu.data = newarr
        hdu.writeto('A%s' % (name))
        Counter = Counter+1
        print(Counter)
    Counter = 0
    os.chdir('/home/carlos/Desktop/Astrophotography/Green/Calibrated')
    filenames = glob.glob('*.fit')
    for name in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Green/Calibrated')
        data = fits.getdata(name)
        crop_center = (coord[1],coord[0])
        crop_size = units.Quantity((41,41),units.pixel)
        crop = Cutout2D(data,crop_center,crop_size)
        coordM = np.where(crop.data == np.amax(crop.data))
        coordF = [coordM[0]-20+coord[0],coordM[1]-20+coord[1]]
        diff = [coordF[0]-coord[0],coordF[1]-coord[1]]
        newarr = np.ones((582,752),dtype = int)
        Min = np.amin(data)
        newarr = newarr*Min
        for x in Rows:
            if x - diff[0] < 0 or x-diff[0] > np.amax(Rows):
                pass
            else:
                y = x
                for x in Columns:
                    if x - diff[1] < 0 or x-diff[1] > np.amax(Columns):
                        pass
                    else:
                        newarr[y,x] = data[y-diff[0],x-diff[1]]
        os.chdir('/home/carlos/Desktop/Astrophotography/Green/Calibrated/Aligned')
        hdu = fits.PrimaryHDU()
        hdu.data = newarr
        hdu.writeto('A%s' % (name))
        Counter = Counter+1
        print(Counter)
    Counter = 0
    os.chdir('/home/carlos/Desktop/Astrophotography/Blue/Calibrated')
    filenames = glob.glob('*.fit')
    for name in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Blue/Calibrated')
        data = fits.getdata(name)
        crop_center = (coord[1],coord[0])
        crop_size = units.Quantity((41,41),units.pixel)
        crop = Cutout2D(data,crop_center,crop_size)
        coordM = np.where(crop.data == np.amax(crop.data))
        coordF = [coordM[0]-20+coord[0],coordM[1]-20+coord[1]]
        diff = [coordF[0]-coord[0],coordF[1]-coord[1]]
        newarr = np.ones((582,752),dtype = int)
        Min = np.amin(data)
        newarr = newarr*Min
        for x in Rows:
            if x - diff[0] < 0 or x-diff[0] > np.amax(Rows):
                pass
            else:
                y = x
                for x in Columns:
                    if x - diff[1] < 0 or x-diff[1] > np.amax(Columns):
                        pass
                    else:
                        newarr[y,x] = data[y-diff[0],x-diff[1]]
        os.chdir('/home/carlos/Desktop/Astrophotography/Blue/Calibrated/Aligned')
        hdu = fits.PrimaryHDU()
        hdu.data = newarr
        hdu.writeto('A%s' % (name))
        Counter = Counter+1
        print(Counter)
if FC == 4 or FC == 5 or FC == 6 or FC == 7:
    Counter = 0
    os.chdir('/home/carlos/Desktop/Astrophotography/Halpha/Calibrated')
    filenames = glob.glob('*.fit')
    for name in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/Halpha/Calibrated')
        data = fits.getdata(name)
        crop_center = (coord[1],coord[0])
        crop_size = units.Quantity((41,41),units.pixel)
        crop = Cutout2D(data,crop_center,crop_size)
        coordM = np.where(crop.data == np.amax(crop.data))
        coordF = [coordM[0]-20+coord[0],coordM[1]-20+coord[1]]
        diff = [coordF[0]-coord[0],coordF[1]-coord[1]]
        newarr = np.ones((582,752),dtype = int)
        Min = np.amin(data)
        newarr = newarr*Min
        for x in Rows:
            if x - diff[0] < 0 or x-diff[0] > np.amax(Rows):
                pass
            else:
                y = x
                for x in Columns:
                    if x - diff[1] < 0 or x-diff[1] > np.amax(Columns):
                        pass
                    else:
                        newarr[y,x] = data[y-diff[0],x-diff[1]]
        os.chdir('/home/carlos/Desktop/Astrophotography/Halpha/Calibrated/Aligned')
        hdu = fits.PrimaryHDU()
        hdu.data = newarr
        hdu.writeto('A%s' % (name))
        Counter = Counter+1
        print(Counter)
if FC == 4:
    Counter = 0
    os.chdir('/home/carlos/Desktop/Astrophotography/O3/Calibrated')
    filenames = glob.glob('*.fit')
    for name in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/O3/Calibrated')
        data = fits.getdata(name)
        crop_center = (coord[1],coord[0])
        crop_size = units.Quantity((41,41),units.pixel)
        crop = Cutout2D(data,crop_center,crop_size)
        coordM = np.where(crop.data == np.amax(crop.data))
        coordF = [coordM[0]-20+coord[0],coordM[1]-20+coord[1]]
        diff = [coordF[0]-coord[0],coordF[1]-coord[1]]
        newarr = np.ones((582,752),dtype = int)
        Min = np.amin(data)
        newarr = newarr*Min
        for x in Rows:
            if x - diff[0] < 0 or x-diff[0] > np.amax(Rows):
                pass
            else:
                y = x
                for x in Columns:
                    if x - diff[1] < 0 or x-diff[1] > np.amax(Columns):
                        pass
                    else:
                        newarr[y,x] = data[y-diff[0],x-diff[1]]
        os.chdir('/home/carlos/Desktop/Astrophotography/O3/Calibrated/Aligned')
        hdu = fits.PrimaryHDU()
        hdu.data = newarr
        hdu.writeto('A%s' % (name))
        Counter = Counter+1
        print(Counter)
    Counter = 0
    os.chdir('/home/carlos/Desktop/Astrophotography/S2/Calibrated')
    filenames = glob.glob('*.fit')
    for name in filenames:
        os.chdir('/home/carlos/Desktop/Astrophotography/S2/Calibrated')
        data = fits.getdata(name)
        crop_center = (coord[1],coord[0])
        crop_size = units.Quantity((41,41),units.pixel)
        crop = Cutout2D(data,crop_center,crop_size)
        coordM = np.where(crop.data == np.amax(crop.data))
        coordF = [coordM[0]-20+coord[0],coordM[1]-20+coord[1]]
        diff = [coordF[0]-coord[0],coordF[1]-coord[1]]
        newarr = np.ones((582,752),dtype = int)
        Min = np.amin(data)
        newarr = newarr*Min
        for x in Rows:
            if x - diff[0] < 0 or x-diff[0] > np.amax(Rows):
                pass
            else:
                y = x
                for x in Columns:
                    if x - diff[1] < 0 or x-diff[1] > np.amax(Columns):
                        pass
                    else:
                        newarr[y,x] = data[y-diff[0],x-diff[1]]
        os.chdir('/home/carlos/Desktop/Astrophotography/S2/Calibrated/Aligned')
        hdu = fits.PrimaryHDU()
        hdu.data = newarr
        hdu.writeto('A%s' % (name))
        Counter = Counter+1
        print(Counter)