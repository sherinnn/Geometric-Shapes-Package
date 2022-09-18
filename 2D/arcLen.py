import math

def arcLen(diameter, angle):
    if angle >= 360:
        #print("Angle cannot be formed")
        return 0
    else:
        arc = (math.pi*diameter) * (angle/360.0)
        return arc
         
# Driver Code
# diameter = 25.0
# angle = 75.0
# arc_len = arcLen(diameter, angle)
# print(arc_len)