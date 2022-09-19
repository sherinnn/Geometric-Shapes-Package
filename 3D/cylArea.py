import math
pi = math.pi
sqrt = math.sqrt
 
def cylVol(r, h):
    return pi * r * r * h
 
def cylSurf(r, h):
    return 2*pi*r*(h + r)

def cylLatSurf(r,h):
    return 2 * pi * r * h

# print(cylLatSurf(2,5))