from numpy import sin, cos, pi,sqrt
import matplotlib.pyplot as plt
from math import fabs

g = 9.8
k_d = 0.5*1.225*0.33
v = 4.0
P = 400
m = 70

#for i in arange(10,50.1,0.1):
   # theta.append(i)
x = 0
t = 0
dt = 0.01
while t <=200:
    a = -k_d*v**2**v/fabs(v)/m+P/(m*v)
    v = v +a*dt
    x = x + v*dt
    t = t + dt
plt.plot(t,v,'+r')
      #  plt.plot(t,v,'bo')
print ("Max speed is {0:4.2f}".format(v))
plt.show()

        
