# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:06:06 2018
decay.py
solve for the parent and daughter populations in nuclear decay
@author: olenick
"""
import matplotlib.pyplot as plt
from numpy import linspace, log

#define differenetial equations as functions
def R1(N1):
    return -k1*N1    #disintegration rate for parent
def R2(N1,N2):
    return k1*N1 - k2*N2   #disintegration rate for daughter

#initialize parameters
k1 = log(2)/13.5
k2 = log(2)/11.0
N1 = 1000
N2 = 0
N1_end = 0
N2_end = 0
h = 0.01
t = 0
t_stop = 100.0

#need lists of values calculated for graphing
tcalc = []
N1calc = []
N2calc = []
N1calc.append(0)
N2calc.append(0)
tcalc.append(0)
#implementing Heun's algorithm

while t < t_stop:
    N2_end = N2 + R2(N1,N2)*h  #use Euler to get end point of h interval
    N2 = N2 + (R2(N1,N2)+R2(N1_end, N2_end))/2.0*h  #average the two slopes at beginning and end of interval
    N1_end = N1 + R1(N1)*h  #use Euler to get end point of h interval
    N1 = N1 + (R1(N1)+R1(N1_end))/2.0*h  #average the two slopes at beginning and end of interval
    N1calc.append(N1)
    N2calc.append(N2)
    t = t + h
    tcalc.append(t)

plt.plot(tcalc, N1calc, 'ro')
plt.plot(tcalc, N2calc, 'bx')
plt.show()

    











