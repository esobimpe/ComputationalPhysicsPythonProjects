from numpy import sin, cos, pi,sqrt,arange,delete,argmax
import matplotlib.pyplot as plt

g = 9.8
#k_d =float(input("Enter the drag coefficient k_d: "))
k_d = g/45**2
v = float(input("Enter the initial speed: "))
#theta = float(input("Enter the initial angle in degrees: "))
#theta = theta*pi/180
theta = []
dist = []

for i in arange(10,50.1,0.1):
    theta.append(i)

def euler(vx,vy,dist):
    x = 0
    y = 0
    t = 0
    dt = 0.01
    while y >=0:
        ax = -k_d*sqrt(vx*vx+vy*vy)*vx
        ay = -g-k_d*sqrt(vx*vx+vy*vy)*vy
        vx = vx +ax*dt
        vy = vy +ay*dt

        x = x + vx*dt
        y = y + vy*dt
        t = t + dt
    dist.append(x)

for i in theta:
    i = i*pi/180
    vx = v*cos(i)
    vy = v*sin(i)
    euler(vx,vy,dist)

plt.plot(theta,dist,'+r')

print ("Max range is {0:4.2f} m at an angle of {1:4.2f} degrees.".format(max(dist),theta[argmax(dist)]))
        
plt.show()
