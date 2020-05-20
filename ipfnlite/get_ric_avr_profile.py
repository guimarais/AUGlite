"""Provides an average profile of RIC diagnostics
"""
import numpy as np

def get_ric_avr_profile(rhop, ne, ne_boundary_top=None, ne_boundary_bot=None, num=20, ne_max=None, ne_min=None):
    """Provides an averaged profile from a set of profiles. The set of profiles is devided in 
    electron density space in bins, whith edges defined by (ne_boundary_bot; ne_boundary_top). 
    If (ne_boundary_bot; ne_boundary_top) are not defined, the bin borders are equidistantly
    separated by num densities betwenn (ne_min; ne_max). The median rho poloidal and ne are 
    calculated from data points in each density bin. The maximum and minimum variations of 
    rho poloidal in each bin are also recorded.     

    Parameters
    ----------
    rhop : numpy array, float,
        2D array with rho poloidal coordinate of RIC
    ne : numpy array, float,
        2D array with density ne
    ne_boundary_top : numpy array, optional
        1D array defining the lower density limit of each bin rho, by default None.
        Has to be defined togeather with ne_boundary_bot 
    ne_boundary_bot : numpy array, optional
        1D array defining the lower density limit of each bin rho, by default None.
        Has to be defined togeather with ne_boundary_top 
    num : int, optional
        Number of density bins, by default 20
    ne_max : float, optional
        The upper edge of the density to be averaged, by default None
    ne_min : float, optional
        The lower edge of the density to be averaged, by default None

    Returns
    -------
    avr_rhop: numpy array, float
        Median rho poloidal in each density bin
    avr_ne: numpy array, float
        Median ne in each density bin
    min_rhop: numpy array, float
        Minimal rho poloidal in each density bin
    max_rhop: numpy array, float
        Maximal rho poloidal in each density bin
    """
    if np.logical_or(ne_boundary_top, ne_boundary_bot) is None:
        if ne_max is None:
            ne_max = np.max(ne)
        if ne_min is None:
            ne_min = np.min(ne)
        ne_bin_lst = np.linspace(ne_min, ne_max, num+1)
    else:
        ne_bin_lst = np.sort(np.concatenate((ne_boundary_top, ne_boundary_bot)))
    avr_ne = []
    avr_rhop = []
    min_rhop = []
    max_rhop = []
    for ii, nn in enumerate(ne_bin_lst[:-1]):
        ne_s = nn
        ne_e = ne_bin_lst[ii+1]
        
        mask = np.logical_and(ne >= ne_s, ne < ne_e)

        avr_ne.append(np.median(ne[mask]))
        avr_rhop.append(np.median(rhop[mask]))
        min_rhop.append(np.min(rhop[mask])) 
        max_rhop.append(np.max(rhop[mask]))

    avr_ne = np.asarray(avr_ne)
    avr_rhop = np.asarray(avr_rhop)
    min_rhop = np.asarray(min_rhop)
    max_rhop = np.asarray(max_rhop)

    return avr_rhop, avr_ne, min_rhop, max_rhop