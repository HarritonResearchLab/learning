import numpy as np 
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle 

# generate random data 

dates = 100 * np.random.random(100)
fluxes = np.sin(2 * np.pi * dates) + 0.1 * np.random.standard_normal(100)

# lomb scargle 

periods = 1/frequencies

best = np.argmax(powers)  
period = 1/float(frequencies[best]) # because P = 1/f
print(period)

#new_b = np.mod(lc[0], T) / T;

# fold light curve

phased_dates = np.mod(dates, period)/period

plt.scatter(phased_dates, fluxes, color='black')
plt.show()