import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


#Experimental data"
#First we do the experiment - here we simulate the data from 1/t decay.

xMeas = np.random.uniform(0.5,3.0,size=6)
yTrue = 1.5/xMeas
sError = 0.1
yMeas = yTrue + np.random.normal(scale=sError, size=np.size(yTrue))

#Let's plot this to see how our experiment looked:
plt.figure(1)
plt.errorbar(xMeas,yMeas,yerr=sError,lw=0,elinewidth=1,ecolor='b', fmt='ko',markersize=2)
plt.xlabel('"Time"')
plt.ylabel('Measured value')
plt.xlim(0.4,3.0)
plt.show()

def f_decay(x,a,b):
    return a*x**(b)

vGuess = [2.0,-2.0]
vPars, aCova = optimize.curve_fit(f_decay, xMeas, yMeas, vGuess)
print (vPars)
xFine = np.linspace(0.4,3.0,100)
plt.figure(2)
plt.errorbar(xMeas,yMeas,yerr=sError,lw=0,elinewidth=1,ecolor='b', fmt='ko',markersize=2)
plt.plot(xFine, f_decay(xFine,*vPars), 'g-', lw=1) # Fitted parameters
plt.plot(xFine, f_decay(xFine,1.5,-1.0), 'r--', lw=1) # Parameters used to generate data
plt.title('Fitted curve (green) and "truth" curve (red dashed)')
plt.show()


nTrials = 4000
aFitPars = np.array([])

for iTrial in range(nTrials):
    xTrial = np.random.uniform(0.5,3.0,size=np.size(xMeas))
    #yGen = 1.5/xTrial
    yGen = 1.5*(xTrial)**2
    yTrial = yGen + np.random.normal(scale=sError,size=np.size(yGen))
    
    # We use a try/except clause to catch pathologies
    try:
        vTrial, aCova = optimize.curve_fit(f_decay,xTrial,yTrial,vGuess)
    except:
        dumdum=1
        continue  # This moves us to the next loop without stacking.
    
    #here follows the syntax for stacking the trial onto the running sample:
    if np.size(aFitPars) < 1:
        aFitPars=np.copy(vTrial)
    else:
        aFitPars = np.vstack(( aFitPars, vTrial ))

np.shape(aFitPars)
print (np.median(aFitPars[:,1]))
print (np.std(aFitPars[:,1]))
plt.figure(3)
plt.hist(aFitPars[:,1],bins=50)
plt.xlabel('Power-law index b')
plt.ylabel('N(b)')
plt.show()

print (np.std(aFitPars[:,1]))

plt.figure(4)
plt.scatter(aFitPars[:,0], aFitPars[:,1], alpha=0.5, s=9, edgecolor='none')
plt.xlabel('Normalization of power-law a')
plt.ylabel('Power-law index b')
plt.show()


from scipy.stats import kde
x,y=aFitPars.T

# Use a kernel density estimator to produce local-counts in this space, and grid them to plot.
k = kde.gaussian_kde(aFitPars.T)
nbins=200
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

# Show the density
plt.figure(5)
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), zorder=3)
plt.colorbar()
plt.show()

# Show the datapoints on top of this, and also the contours. "zorder" sets the vertical order in the plot.
plt.figure(6)
plt.scatter(aFitPars[:,0], aFitPars[:,1], c='w', s=2, zorder=15, edgecolor='none',alpha=0.75)
plt.contour(xi,yi,zi.reshape(xi.shape), zorder=25, colors='0.25')
plt.ylim(-1.45,-0.55)
plt.xlim(1.25,1.80)
plt.xlabel('Power-law normalization a')
plt.ylabel('Power-law index b')
plt.show()
