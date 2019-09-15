"""
Compute poloidal flux radius (rho_pol) corresponding to given time (t),
major radius (R) and height (z).
"""

from __future__ import print_function
#from builtins import zip
import sys
import warnings
from itertools import count
import numpy as np
import kk_abock


def trz_to_rhop(
        t, r, z, shot=0, eq='EQH', n_verbose=100, verbose=True, squeeze=True):
    #TODO: examples
    """Compute poloidal flux radius (rho_pol) corresponding to given time (t),
    major radius (R) and height (z).

    Accepts scalar, 1D or 2D arrays as input.

    Parameters
    ----------
    t : float array (scalar or 1D)
        Time instants.
    r : float array (scalar, 1D or 2D)
        Major radius coordinates in real space.
    z : float array (scalar, 1D or 2D)
        Height coordinates in real space.
    shot : int, optional
        Shot number.
    eq : {'EQH', 'EQI', 'FPP', 'IDE'}, optional
        Desired equilibrium for the transformation.
    n_verbose : int, optional
        Number of time instants between each progress printing. Only relevant
        if 'verbose' is True.
    verbose : bool, optional
        If true, print progress of computation.
    squeeze : bool, optional
        If True, extra dimensions are squeezed out from the returned array:
            - if only one rho_pol is computed, it is returned as a scalar.
            - for Nx1 or 1xN, the result is returned as a 1D array.
            - for NxM, with N>1 and M>1, the result is returned as a 2D array.
        If False, no squeezing at all is done: the returned object is always a
        2D float array, even if it ends up being 1x1.

    Returns
    -------
    float array (scalar, 1D or 2D)
        Poloidal flux radius coordinates (rho_pol).

    Examples
    --------

    """

    # Open equilibrium
    equilibrium = kk_abock.kk()
    try:
        equilibrium.Open(shot, diag=eq)
    except Exception as ex:
        warnings.warn(
            "Error when opening {} for shot {} - {}: {!r}".format(
                eq, shot, type(ex).__name__, ex.args),
            stacklevel=2)
        if eq != "EQH":
            warnings.warn(
                "Could not open equilibrium {}, using EQH intead".format(eq),
                stacklevel=2)
            equilibrium.Open(shot, diag="EQH")
        else:
            raise

    # Compute poloidal flux radius and print progress if desired
    t = np.atleast_1d(t)
    r, z = np.broadcast_arrays(t[:, np.newaxis], r, z)[1:]
    rho_pol = np.full_like(r, np.nan)
    if verbose:
        n = len(t)
        progress_string = "{}:{{}}/{}".format(
            sys._getframe().f_code.co_name, n)
    for i, time, radius, height in zip(count(), t, r, z):
        rho_pol[i] = equilibrium.Rz_to_rhopol(time, radius, height)
        if verbose and (i % n_verbose == 0 or i + 1 == n):
            print(progress_string.format(i + 1), end='\r')
    if verbose:
        print("")

    # Close equilibrium and return data
    equilibrium.Close()
    if squeeze:
        rho_pol = np.squeeze(rho_pol)
    return rho_pol
