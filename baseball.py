from numpy import loadtxt, zeros,array
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Load DATA
data = loadtxt("",skiprows=1)
dtime = data[:,1] - data[:,0]
tmax = 45
#Number of pitch
N =len(ftime)

#get initial values

x = data[:,2]
y = data[:,3]
z = data[:,4]

vx = data[:,5]
vy = data[:,6]
vz = data[:,7]

accx = data[:,8]
accy = data[:,9]
accz = data[:,10]

t = 0
h = tmax/100.0

#plot

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_wireframe(array([[-0.722,0.722],[-0.722,0.722]]),array([[0,0],[0,0]]),
                  array([[1.64,1.64],[3.60,3.60]]),color = 'r')

#step through time and plot

for i in range(0,N):
    xplot = zeros(45,float)
    yplot = zeros(45,float)
    zplot = zeros(45,float)

    x0 = x[i]
    y0 = y[i]
    z0 = z[i]

    vx0 =vx[i]
    vy0 =vy[i]
    vz0 =vz[i]

    accx0 =accx[i]
    accy0 =accy[i]
    accz0 =accz[i]

    for j in range (0,tmax):
        t = j/100.0
        xplot[j] = x0 +vx0*t + 0.5*accz0*t**2
        yplot[j] = y0 +vy0*t + 0.5*accz0*t**2
        zplot[j] = z0 +vz0*t + 0.5*accz0*t**2
    ax.plot(xplot,yplot,zplot)
        
plt.show()
