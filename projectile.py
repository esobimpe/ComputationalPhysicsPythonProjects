from numpy import sin, cos, pi,sqrt
import matplotlib.pyplot as plt

g = 9.8
k_d =float(input("Enter the drag coefficient k_d: ")) # g/45**2
v = float(input("Enter the initial speed: "))
theta = float(input("Enter the initial angle in degrees: "))
theta = theta*pi/180

#for i in arange(10,50.1,0.1):
   # theta.append(i)

def euler(vx,vy):
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

        plt.plot(t,x,'+r')
      #  plt.plot(t,v,'bo')
vx = v*cos(theta)
vy = v*sin(theta)

euler(vx,vy)
plt.show()
        
