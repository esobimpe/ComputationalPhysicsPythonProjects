'''
VectorFieldPlot.py
Plots a vector field.
'''

import numpy as np
import matplotlib.pyplot as plt

n =16
X, Y = np.mgrid[0:n, 0:n]
#T = np.arctan2(Y - n / 2., X - n/2.)
#R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
#U, V = R * np.cos(T), R * np.sin(T)
#U = X-n/2  #plot r vector, x coord
#V = Y-n/2  #plot r vector, y coord
R = 1

x = X-n/2
y = Y-n/2
#U = -y/(x*x + y*y+0.1)
#V = x/(x*x + y*y+0.1)
U = x/(x +0.001)
V = y/(y+0.001)


plt.axes([0.025, 0.025, 0.95, 0.95])
plt.quiver(X[::2, ::2], Y[::2, ::2], U[::2, ::2], V[::2, ::2], R, alpha=.5)
plt.quiver(X[::2, ::2], Y[::2, ::2], U[::2, ::2], V[::2, ::2], edgecolor='k', facecolor='none', linewidth=.5)

plt.xlim(-1, n)
plt.xticks(())
plt.ylim(-1, n)
plt.yticks(())

plt.show()
