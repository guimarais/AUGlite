#!/usr/bin/env python
from __future__ import print_function
#from builtins import str
#from builtins import range
#from builtins import object
import numpy as np
import re
import ast
import matplotlib.pylab as plt
import os

def run():
    shotnr = 29865
    nevin   = readDivData(getDivFname(shotnr,'nev','in'))
    nevout  = readDivData(getDivFname(shotnr,'nev','out'))
    jsatin  = readDivData(getDivFname(shotnr,'jsat','in'))
    jsatout = readDivData(getDivFname(shotnr,'jsat','out'))

def getDivFname(shotnr,what,pos):
    
    homedir = str(os.environ["HOME"])
    ##Expects data to be saved in "$HOME/Divertor"
    fin = homedir + '/Divertor/' + str(shotnr) + '/3D_'+ str(shotnr) + '_'

    if what == 'nev':
        fin = fin + 'nev'
    elif what == 'jsat':
        fin = fin + 'jsat'
    elif what == 'net':
        fin = fin + 'net'
    elif what == 'te':
        fin = fin + 'te'
    else:
        print("Item not recognized, defaulting to jsat")
        fin = fin + 'jsat'

    if pos == 'in':
        fin = fin+'_in.dat'
    else:
        fin = fin+'_out.dat'

    return fin

def readDivData(filename):
    """Reads contour-plot DIVERTOR data from an ascii file

    Parameters
    ----------
    filename:
         String with the filename outputted from DIVERTOR, ususally "3D_..."

    Returns
    ----------
    An object with three fields:
    obj.time: ndarray
         The times of the contour
    obj.deltas: ndarray
         The y axis of the contour, usually Delta S, but rho is also possible
    obj.data: matrix
        The matrix with the jsat, density, etc., data.
    
    """
    class objview(object):
        def __init__(self, d):
            self.__dict__=d
            
    try:
        fin = open(filename, 'r')
    except:
        print("No such file " + filename)
        print("Returning dummy data")
        data = np.array([[0.0, 0.0],[0.0,0.0]])
        #return dummy data
        #Return ranges that will always be covered by the times ELM analysis are performed
        return objview({'time': np.array([-21.0, 21.0]),
                        'deltas': np.array([-17.0, 57.0]),
                        'data': data})

    #Read dumb line
    fin.readline()
    #Time points
    tpts = int(fin.readline())
    #Read dumb lines
    fin.readline()
    fin.readline()
    #DS coordinate points
    spts = int(fin.readline())
    #Read dumb lines
    fin.readline()
    fin.readline()
    #Density scale
    nes = float(fin.readline())
    nesc = np.array(nes)
    #Read dumb lines
    fin.readline()
    fin.readline()
    #Read time vector
    time = []
    for i in range(0, tpts):
        time.append(float(fin.readline()))
    #Read dumb lines
    fin.readline()
    fin.readline()
    #Read Delta S vector
    deltas = []
    for i in range(0, spts):
        deltas.append(float(fin.readline()))
    #Read dumb lines
    fin.readline()
    fin.readline()
    #Read Density data
    data = []
    for i in range(0, tpts):
        string = fin.readline()
        string = re.sub(r"\s+",",",string)
        string = "[" + string[1:-1] + "]"
        vec = ast.literal_eval(string)
        data.append(vec)
    #Close shotfile
    fin.close()
    
    return objview({'time': np.array(time),
                    'deltas': np.array(deltas),
                    'data': np.array(data).T})


#a = readDivData(getDivFname(29865, "nev", "in"))
#plt.pcolormesh(a.time, a.deltas, a.data, vmax=40);plt.show()
