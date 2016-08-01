import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import LombScargle


star_lis = open('nstar_csv.lis').readlines()

for h in star_lis:
    print(h)
    # Read in the d_nstar####.csv file
    h = h.rstrip('\n')
    df = pd.read_csv('d_' + h)
    
#    n = len(df)
#    
#    # Determine first and last Julian dates of data
#    t1 = df.ix[:0,'jd']
#    t2 = df.ix[n-1:,'jd']
#    t2 = t2.reset_index(drop=True)
#    tj = t2-t1 
    
    # Iterate over each observation within each star file
    jd = df['jd']
    dmag = df['dmag']
    var = df['dmag'].var()
#    periodogram(jd, dmag, t1, t2)
    
    # Periodogram
    frequency, power = LombScargle(jd, dmag).autopower()
    
#    power = power/var
    
    cols_out = np.column_stack((frequency.flatten(), power.flatten()))
#    hdr = 'frequency, power'
    
    np.savetxt('p3_' + h,
               cols_out,
               delimiter = ',',
               fmt = '%.3e',
               header = 'frequency,power',
               comments='')
    
plt.plot(1/frequency, power)