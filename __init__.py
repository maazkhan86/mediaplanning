def ctr(clicks, imp):
    '''
    Calculates Clickthrough rate (CTR) from clicks and impressions
        Parameters:
            clicks (int): An integer
            impressions (int): Another integer
        Returns:
            ctr (int): clicks / impressions
    '''
    return clicks / imp

def clicks(imp, ctr):
    '''
    Calculates Clicks from Impressions and CTR
        Parameters:
            impressions (int): An integer
            ctr (int): Another integer
        Returns:
            clicks (int): impressions * ctr
    '''
    return imp * ctr

def imp(clicks, ctr):
    return clicks / ctr

def cpm(cost, imp):
    return cost / (imp / 1000)

def cost(cpm, imp):
    return cpm * (imp / 1000)

def cpa(cpc, cvr):
    return  cpc / cvr

def conv(cost, cpa):
    return cost / cpa

def grps(reach, freq):
    return reach * freq

def reach(grps, freq):
    return grps / freq

def tai(reachn, freq):
    '''
    Calculates Total Audience Impressions (TAI) from reach # and frequency
        Parameters:
            reachn (int): An integer
            frequency (int): Another integer
        Returns:
            tai (int): reachn * frequency
    '''
    return reachn * freq

def freq(grps, reach):
    return grps / reach

def ots(grps, reach):
    return grps / reach

def cpp(cost, grps):
    return cost / grps

def bdi(bsales, pop):
    return (bsales / pop) * 100

def cdi(csales, pop):
    return (csales / pop) * 100

def boi(bdi, cdi):
    return (bdi/cdi) * 100

def adstock(pweight, cweight, decay):
    return cweight + (decay * pweight)
