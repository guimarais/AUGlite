from builtins import str
from builtins import range
import dd

def spec_channels(shotnr, shotfile='EVL'):
    """Reads the channels from spectroscopy shotfiles
    
    Parameters
    ---------------
    shotnr: int
        Come on!
    shotfile: str
        Usually 'EVL', 'FVL', 'GVL' or 'HVL'
    
    Returns
    ---------------
    chans: list of str
        A list of strings with the ordered name of the channels
    """
    
    evs = dd.shotfile(shotfile, shotnr)
    chans = []
    for i in range(1,40):
        pname = 'CHAN_%.2d'%(i)
        try:
            channame = evs.getParameter('LOS', pname)
            if channame.data[0] != ' ':
                chans.append(str(channame.data).strip())
        except:
            a=0
    evs.close()
    return chans