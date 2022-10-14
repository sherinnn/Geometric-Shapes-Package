import math

def centAngle(diameter, arcLen):
    centAngle = (arcLen*360.0)/ (math.pi*diameter) 
    return centAngle

print(centAngle(10, 15))