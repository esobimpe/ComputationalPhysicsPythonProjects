'''
Solves the differential equation for cold medication in GI tract and bloodstream
'''

import matplotlib.pyplot as plt

#Initial conditions

t =0
tstop =48
h=0.05 #step size
I=0 #Pill Dosage
y=0 #no cold meditation in bloodstream at start
x=0 #no cold meditation in the GI tract
k1 = 0.6931 #disolving constant
k2 = 0.231 #clearing constant

xend = 0
yend = 0
tend = 0


#Define rates

def Rx(x,I):
    return I-k1*x
def Ry(x,y):
    return k1*x-k2*y
plt.axis([0,tstop,0,12])

#Implementing Heun's method
while t <=tstop:
    if t%6<=4.5%4:
        I=20.0
    else:
        I = 0

    xend = x +Rx(x,I)*h 
    tend = t + h

    yend = y + Ry(x,y)*h #Y concentration at the end of our step

    y = y + (Ry(x,y) + Ry(xend,yend))/2.0*h
    x = x + (Rx(x,I) + Rx(xend,I))/2.0*h

    plt.plot(t,x,'b+')
    plt.plot(t,y,'r+')
    t = t + h
plt.show()
