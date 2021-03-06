from __future__ import division
#from builtins import zip
#from builtins import range
import dd
import numpy as np

def rhosep2(shotnr, times, equil='GQH'):
    sf = dd.shotfile(equil, shotnr)    
    dPsi_AxisSep1 = sf('fax-bnd')
    dPsi_Sep1Sep2 = sf('XPfdif')
    sf.close()

    rhoPol_Sep2 = np.zeros_like(times)

    for tme, i in zip(times, range(len(times))):
        indexTime = np.argmin(np.abs(dPsi_AxisSep1.time - tme))
        rhoPol_Sep2[i] = np.sqrt((dPsi_AxisSep1.data + dPsi_Sep1Sep2.data)/dPsi_AxisSep1.data)[indexTime]

    return rhoPol_Sep2

