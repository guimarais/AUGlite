def plotVessel(vessel_structure, ax, color_border='k', lw_border=1.2, color_structure='#D3D3D3'):
    """Plots a vessel structure from getVessel onto an axis object 'ax'
    
    Parameters
    -----------
    vessel_structure: return of the getVessel function
        List of ndarrays containing the vessel structure
    ax: matplotlib axes
        Where you want to plot the strcture
    color_border: str
        Color of the vessel structure elements' borders
    lw_border: float
        Line width of the vessel structure elements' borders
    color_structure: str
        Color of the solid elements of the vessel structure
    
    Returns
    -----------
    Zilch
    
    Example
    -----------
    from ipfnpytools.getVessel import getVessel
    from ipfnpytools.plotVessel import plotVessel
    import matplotlib.pyplot as plt
    
    vessel = getVessel(32223)
    
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,12))
    plotVessel(vessel, ax)
    ax.set_aspect('equal')
    plt.show()    
    """
    for entry in vessel_structure:
        r = entry[:,0]
        z = entry[:,1]
        #Check if it's the vessel outline
        if ((min(r)<1.1) & (max(r)>2.0) & (min(z)<1) & (max(z)>1)):
            a=0 #Do nothing
        else:
            ax.fill(entry[:,0], entry[:,1], color=color_structure)

    for entry in vessel_structure:
        ax.plot(entry[:,0], entry[:,1], color=color_border, lw=lw_border)