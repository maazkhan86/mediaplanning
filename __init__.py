def ctr(clicks, imp):
    return clicks / imp

def clicks(imp, ctr):
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

def freq(grps, reach):
    return grps / reach

def ots(grps, reach):
    return grps / reach

def cpp(cost, grps):
    return cost / grps

def bdi(brandsales, pop):
    return (brandsales / pop) * 100

def cdi(catsales, pop):
    return (catsales / pop) * 100

def boi(bdi, cdi):
    return (bdi/cdi) * 100

def adstock(pweight, cweight, decay):
    return cweight + (decay * pweight)
