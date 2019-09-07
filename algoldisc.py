# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:03:03 2018
algoldisc
calculate some parameters about Algol discs
"""
from __future__ import division
import matplotlib.pyplot as plt
from numpy import linspace, arange
from math import pow

def Rcirc(q):
    return (1+q)*RL1(q)**4

def RL1(q):
    w = pow(q/(3*(1+q)),1/3)
    return 1 - w + (w*w)/3+(w*w*w)/9 

def Rout(q):
    return (7/5)**2*Rcirc(q)


r = []
ro = []
rc = []
r21 =[]
r31 = []
x = []

for q in arange(0.01, 0.33, 0.001): 
    r.append(RL1(q))
    x.append(q)
    ro.append(Rout(q))
    rc.append(Rcirc(q))
    r21.append(pow(4*(1+q),-1/3))
    r31.append(pow(9*(1+q),-1/3))

plt.plot(x,r, 'b+', label="RL1")
plt.plot(x,ro, 'gx', label = "Rout")
plt.plot(x,rc,'r+', label = "Rcirc")
plt.plot(x, r21, 'ko', label = "R2:1")
plt.plot(x,r31,'yo', label = "R3:1")
plt.xlabel("mass ratio q")
plt.ylabel('disc radius')
plt.legend()
plt.show()
