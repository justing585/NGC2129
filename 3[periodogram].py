import scipy.signal
import pandas as pd
import numpy as np


# Define the periodogram function (wrapper created by Ben Kimock)
def periodogram(time, data, start, stop, N=1e4):
    freq = 1/(10**np.linspace(np.log10(start), np.log10(stop), N))
    nfactor = 2/(data.size * np.var(data))

    power = scipy.signal.lombscargle(time,data-np.mean(data),2*np.pi*freq) * nfactor

    return 1/freq, power


star_lis = open('nstar_csv.lis').readlines()

for h in star_lis:
    
    # Read in the d_nstar####.csv file
    h = h.rstrip('\n')
    df = pd.read_csv('d_' + h)
    
    n = len(df)
    
    # Determine first and last Julian dates of data
    t1 = df.ix[:0,'jd']
    t2 = df.ix[n-1:,'jd']
    t2 = t2.reset_index(drop=True)
    tj = t2-t1 
    
    # Iterate over each observation within each star file
    jd = df['jd']
    dmag = df['dmag']
    
    periodogram(jd, dmag, t1, t2)
    
