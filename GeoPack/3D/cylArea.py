import math
pi = math.pi
sqrt = math.sqrt
 
def cylVol(r, h):
    if(r,h<=0):
        return 0
    return pi * r * r * h
 
def cylSurf(r, h):
    if(r,h<=0):
        return 0
    return 2*pi*r*(h + r)

def cylLatSurf(r,h):
    if(r,h<=0):
        return 0
    return 2 * pi * r * h

# print(cylLatSurf(2,5))