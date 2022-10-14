import math
pi = math.pi
sqrt = math.sqrt
 
def cuboidVol(l,b,h):
    if(l,b,h<=0):
        return 0
    return l*b*h
 
def cuboidSurf(l,b,h):
    if(l,b,h<=0):
        return 0
    return 2(l*b + b*h + l*h)

def cuboidLatSurf(l,b,h):
    if(l,b,h<=0):
        return 0
    return 2*h*(l+b)
