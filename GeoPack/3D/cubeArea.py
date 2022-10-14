import math
pi = math.pi
 
def cubeVol(s):
    if(s<=0):
        return 0
    return s*s*s
 
def cubeSurf(s):
    if(s<=0):
        return 0
    return 6*s*s