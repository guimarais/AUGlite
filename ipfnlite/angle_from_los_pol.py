from __future__ import division
import numpy as np

def angle_from_los_pol(diag_los, signal, degrees=True):
    """Gets the angle from a LOS signal that has been read with get_los
    
    Parameters
    -----------
    diag_los:
        Output of get_los
    signal: str
        Name of the signal inside diag_los to calculate the angle
    degrees: bool
        Default in degrees so you can use directly in text rotations. False for radians.
                
    Returns
    -----------
    angle: float
        Angle the diagnostic has in a poloidal projection
                
    Example
    -----------
    dcn_los = get_los('DCN.coords')
    angle_diag = angle_from_los_pol(dcn_los, 'H-5')
    
    """
    angle = np.arctan((diag_los['signals'][signal]['0']['z'][1]-diag_los['signals'][signal]['0']['z'][0])/
                      (diag_los['signals'][signal]['0']['R'][1]-diag_los['signals'][signal]['0']['R'][0]))
    
    if degrees:
        angle = np.degrees(angle)
    
    return angle