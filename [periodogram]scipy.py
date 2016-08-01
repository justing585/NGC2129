# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:12:00 2016

@author: justin1
"""

import scipy.signal
import numpy as np
import matplotlib.pyplot as plt


# Define the periodogram function (wrapper created by Ben Kimock)
def periodogram(time, data, start, stop, N=1e4):
    freq = 1/(10**np.linspace(np.log10(start), np.log10(stop), N))
    nfactor = 2/(data.size * np.var(data))

    pwr = scipy.signal.lombscargle(time,data-np.mean(data),2*np.pi*freq) * nfactor

    return 1/freq, pwr


star_lis = open('nstar_csv.lis').readlines()

for h in star_lis:
    print(h)
    # Read in the d_nstar####.csv file
    h = h.rstrip('\n')
    jd, dmag = np.loadtxt('d_' + h,
                    skiprows = 1,
                    delimiter = ',',
                    usecols = (1,2),
                    unpack = True)

     
    # Define minimum and maximum period
    start = 0.1
    stop = 100
    
    freq, pwr = periodogram(jd, dmag, start, stop)

    output = np.stack((freq,pwr), axis=1)
    
    np.savetxt('p2_star/p2_' + h,
               output,
#               fmt = '%.6',
               delimiter = ',',
               header = 'period,power',
               comments = '')
    
#    plot_out = plt.plot(1/freq, power)
#    plot_out.plt.savefig('p2.png')
#    plt.close(plot_out)
    
    
    