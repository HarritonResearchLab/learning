import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle 

# generate random data 

rand = np.random.default_rng(42)  

dates = 100 * rand.random(100)
fluxes = np.sin(2 * np.pi * dates) + 0.1 * rand.standard_normal(100)

# lomb scargle 

frequencies, powers = LombScargle(dates, fluxes).autopower(minimum_frequency=0.25, maximum_frequency=5)
periods = 1/frequencies

best = np.argmax(powers)  
period = 1/float(frequencies[best]) # because P = 1/f
print(period)

#new_b = np.mod(lc[0], T) / T;

# fold light curve
phased_dates = np.mod(dates, period)/period

plt.scatter(phased_dates, fluxes, color='black')
plt.show()