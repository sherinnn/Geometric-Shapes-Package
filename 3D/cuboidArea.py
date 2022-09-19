import math
pi = math.pi
sqrt = math.sqrt
 
def cuboidVol(l,b,h):
    return l*b*h
 
def cuboidSurf(l,b,h):
    return 2(l*b + b*h + l*h)

def cuboidLatSurf(l,b,h):
    return 2*h*(l+b)
