# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:14:11 2018
polyfit.py
fit different orders of polynomials to a curve
@author: olenick
"""

import numpy as np
import matplotlib.pyplot as plt

# create a  data curve
x = np.linspace(-5.,5.,25)
y =( (0.5*x**4) + (-4*x**3) + (3*x**2) + (-2*x) + 1 ) #*0.5*np.random.normal(size=len(x))

#create function
#f = np.poly1d([0.5,-4,3,-2,1])

#perform fits and get coeefficients

c1 = np.polyfit(x,y,1)
c2 = np.polyfit(x,y,2)
c3 = np.polyfit(x,y,3)
c4 = np.polyfit(x,y,4)

print("Fit Coefficients, 1st through 4th order")
print("{}\n{}\n{}\n{}\n".format(c1,c2,c3,c4))

p1 = np.poly1d(c1)
p2 = np.poly1d(c2)
p3 = np.poly1d(c3)
p4 = np.poly1d(c4)

plt.plot(x,y, 'ko', label='Data')
plt.plot(x, p1(x), 'g-', label = '1st order')
plt.plot(x, p2(x), 'b-', label = '2nd order')
plt.plot(x, p3(x), 'c-', label = '3rd order')
plt.plot(x, p4(x), 'r-', label = '4th order')

plt.legend()
plt.show()












