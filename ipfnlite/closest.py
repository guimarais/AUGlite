import numpy as np

def closest(array, value):
    """Return the index of "array" with the value closest to "value"

    """
    idx = (np.abs(array-value)).argmin()
    return idx

def closest_val(array, value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]
