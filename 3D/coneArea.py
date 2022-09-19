import math
pi = math.pi
sqrt = math.sqrt
 
def coneVol(r, h):
    return (1 / 3) * pi * r * r * h
 
def coneSurf(r, s):
    return pi * r * s + pi * r * r

def coneLatSurf(r,h):
    return pi * r * sqrt((h*h)+(r*r))
