# Period Detective Exercise

## Overview
* Once you download and extract the .zip file ```light_curves.zip```, you will find a file inside it called ```key.csv``` which importantly contains a column of stellar identifiers for the 323 stars that have data in the ```light_curves/light_curves``` directory you will be working with in this exercise. 
* Your goal is to iterate through each of the object's ```_r.csv``` files (e.g. the file for the star ```2MASS_J20470481+4349114``` would be ```2MASS_J20470481+4349114_r.csv```), run the Lomb-Scargle periodogram on that light curve, return a list of stars whose lightcurves are periodic (for now we will assume stars whose peak power is more than 0.5 to have significant periods), and then make phase-folded light curve plots for those stars, as well as making a histogram displaying the distribution of periods among those stars with significant periods. 

## Code Hints
* Run the Lomb-Scargle Algorithm like this: 

<pr><code>
ls = LombScargle(mjds, mags)
frequencies, powers = ls.autopower(minimum_frequency=0.05, maximum_frequency=0.5)
periods = 1/frequencies
</code></pr>