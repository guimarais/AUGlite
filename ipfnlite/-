#Adapted from C. Fuchs' test_kcgred.py
#!/usr/bin/python
from ctypes import *
import sys
import numpy as np

def getVessel(shotnr):
    """Gets the vessel structure for a shot. Adapted from C. Fuchs' test_kcgred.py
    
    Parameters
    -----------
    shotnr: int
        Come on, really? You need this one explained?
    
    Returns
    -----------
    vessel: list of ndarray
        A list of several numpy arrays with varying dimensions containing the info
        of the vessel structures shot shot number shotnr.
    
    Example:
    -----------
    vessel = getVessel(shotnr)
    """
    # --- Import libkk library
    if sizeof(c_long) == 8:
      libkkso = "/afs/ipp/aug/ads/lib64/@sys/libkk8.so"
    else:
      libkkso = "/afs/ipp/aug/ads/lib/@sys/libkk.so"
    libkk = cdll.LoadLibrary(libkkso)

    error = c_int(0)
    exp   = create_string_buffer('AUGD')
    diag  = create_string_buffer('EQI')
    shotnr  = c_int(int(shotnr))
    edition = c_int(0)
    error   = c_int(0)

    # --- Get necessary dimensions
    ndgc   = c_int(0)
    ndit   = c_int(0)
    ndim   = c_int(0)
    nvalid = c_int(0)

    libkk.kkgcdimensions(byref(error), exp, diag, shotnr, byref(edition), byref(shotnr), byref(ndgc), byref(ndit),
                         byref(ndim), byref(nvalid) ); 

    # --- Read the coordinates

    xygcs= (((c_float*ndgc.value)*ndit.value)*2)()
    ngc  = c_int(0)
    lenix= (c_int*ndgc.value)()
    libkk.kkgcread(byref(error), exp, diag, shotnr, byref(edition), ndgc, ndit, byref(xygcs), byref(ngc), byref(lenix))

    # --- Print the coordinates
    vessel = []
    
    for igc in range (0, ngc.value-1):
        structure = []
        for i in range (0, lenix[igc] - 1):
            structure.append([xygcs[0][i][igc],xygcs[1][i][igc]])

        #Close the structure    
        structure.append([xygcs[0][0][igc], xygcs[1][0][igc]])
        #Append the structure to the vessel list
        vessel.append(np.reshape(structure, (-1, 2)))
        #vessel.append(structure)
        
    return vessel
