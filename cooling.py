# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:45:51 2018
cooling.py
solve newton's law of cooling
"""
import matplotlib.pyplot as plt
from math import sin, pi

def R(T,Ts):
    return -r*(T- Ts)

def Ts(t):
    return 92 - 10*sin(2*pi*(t+3)/24)

#initialize parameters
t = 0
T =74
Tend = 0.0
tend = 0.0
r = 0.1
h = 0.1

#apply Heun's method
while t < 48.0:
    Tsur = Ts(t)
    tend = t + h
    Tsurend = Ts(tend)
    Tend = T + R(T,Tsurend)*h
    T = T + (R(T, Tsur) + R(Tend, Tsurend))/2.0*h
    t = t + h
    
    plt.plot(t, T, 'bo')
    plt.plot(t, Tsur, 'rx')
plt.show()







