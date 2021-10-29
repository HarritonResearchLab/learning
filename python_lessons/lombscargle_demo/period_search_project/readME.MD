# Period Detective Exercise

## Overview
* Once you download and extract the .zip file ```light_curves.zip```, you will find a file inside it called ```key.csv``` which importantly contains a column of stellar identifiers for the 323 stars that have data in the ```light_curves/light_curves``` directory you will be working with in this exercise. 
* Your goal is to iterate through each of the object's ```_r.csv``` files (e.g. the file for the star ```2MASS_J20470481+4349114``` would be ```2MASS_J20470481+4349114_r.csv```), run the Lomb-Scargle periodogram on that light curve, return a list of stars whose lightcurves are periodic (for now we will assume stars whose peak power is more than 0.5 to have significant periods), and then make phase-folded light curve plots for those stars, as well as making a histogram displaying the distribution of periods among those stars with significant periods. 
* As a first step, I talk a glance through this Astropy documentation example which explores the Lomb-Scargle Algorithm with simulated data: [link](https://docs.astropy.org/en/stable/timeseries/lombscargle.html). 
* Once you're done, please make a new folder in the ```./solutions``` directory of this project and put your code and plots in it so we can practice using GitHub. 

## Code Hints
* Run the Lomb-Scargle Algorithm like this (after extracting the ```mjd``` and ```mag``` arrays from the .csv file and importing ```LombScargle``` with ```from astropy.timeseries import LombScargle```): 
```python
ls = LombScargle(mjd, mag)
frequencies, powers = ls.autopower(minimum_frequency=0.05, maximum_frequency=0.5)
periods = 1/frequencies
```
* Setting ```minimum_frequency=0.05``` and ```maximum_frequency=0.5``` will restrict your search space between periods of two and fifty days (as period = 1/frequency, the maximum frequency 0.5 is the shortest period $1/0.5=2). 
* You want to focus on the period with the highest power for each light curve, and (as mentioned), for the purposes of this excercise only consider a period with power >0.5 to be significant. 
* Note that since lower values are brighter in the magnitude system, you'll want to invert the y-axis of your light curve plot. 
* You can save plots in matplotlib with ```plt.savefig()```


## Example Outputs
* Phase-folded light curve:  
![](https://raw.githubusercontent.com/HarritonResearchLab/learning/main/images/phased_lightcurve.png)

* Periods distribution histogram:  
![](https://raw.githubusercontent.com/HarritonResearchLab/learning/main/images/period_dist.png)
