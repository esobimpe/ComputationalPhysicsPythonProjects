# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:36:44 2018
polynomialoptimize.py
fit a polynomial and optimize the fit
@author: olenick
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt("spec.txt",float)
t = data[:,0]
y = data[:,1]
ysigma = data[:,2]

print(np.mean(y))
print(np.median(y))

#give initial parameters 
A0,B0,C0,omega0,tau0 = 19.712,0.316,18.9757,10.334,12.95

#specify the function we wish to fit
def func(t, A, B, C, omega, tau):
    return A*(1 + B*np.cos(omega*t))*np.exp(-t**2/(2*tau**2)) + C

#now we fit the curve
popt, pcov = curve_fit(func, t, y, p0 = [A0,B0,C0,omega0,tau0], sigma = ysigma)
perr = np.sqrt(np.diag(pcov"
 print("A = {0:6.4f} +/- {1:6.4f}, B={2:6.4f} +/- {3:6.4f}, C={4:6.4f} +/- {5:6.4f}").format(popt[0], perr[0], popt[1], prtt[1],popt[2], perr[2]