#from builtins import range
import numpy as np
import dd

def trimtimes(time, elmbeg, elmend, preft = 0.0, suft = 0.0):
    """
    Returns stuff...
    "eventbeg" and "eventend" are, respectively, the beggining and end of ELM events, for instance
    One can choose to also ignore "preft" seconds before the beggining of an ELM event and "suft" seconds after the end of an ELM event

    """
    valididx = np.zeros(len(time),dtype='bool')
    
    elmbeg = elmbeg - preft
    elmend = elmend + suft
    for i in range(len(time)):
        t = time[i]
        boolbeg = t>=elmbeg
        boolend = t<=elmend
        boolelm = boolbeg & boolend
        valididx[i] = np.sum(boolelm)
   
    #To use only data outside of ELMs
    valididx = np.invert(valididx)
    return time[valididx], valididx

def ddremoveELMData(shotnr, time, preft=0.0, suft=0.0, elm_exper="AUGD", elm_edition=0):
    """
    Returns a mask for inter-ELM times.
    One ignore "preft" seconds before the beggining of an ELM event and "suft" seconds after the end of an ELM event.

    Prarameters
    -------------
    shotnr: int
        You know what to do here.
    time: ndarray
        Array of times from the data you wish to analyse.
    preft: float
        "Prefix Time" -> Time before the ELM CRASH to ignore. The ELM regime will influence this value.
    suft: float
        "Suffix Time" -> Time after the ELM END to ignore. The ELM regime will influence this value.
    elm_exper: str
        Experiment for the ELM shotfile. Defaults to the available one in the AUG database.
    elm_edition: int
        Edition of the ELM shotfile

    Returns
    -------------
    validmask: bool array
        Mask with the Inter-ELM indices of "time"
    """
    
    ELM = dd.shotfile("ELM", shotnr, experiment=elm_exper)
    t_endELM = ELM("t_endELM")
    elmend = t_endELM.data
    elmbeg = t_endELM.time
    ELM.close()

    outtime, validmask = trimtimes(time, elmbeg, elmend, preft=preft, suft=suft)

    return validmask
