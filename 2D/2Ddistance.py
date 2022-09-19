import math
from math import *
from decimal import Decimal

def EucDist(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)

def ManDist(x1,y1,x2,y2):
    return math.fabs(x2 - x1) + math.fabs(y2 - y1)

from math import *
from decimal import Decimal
 
# Function distance between two points
# and calculate distance value to given
# root value(p is root value)
def p_root(value, root):
     
    root_value = 1 / float(root)
    return round (Decimal(value) **
             Decimal(root_value), 3)
 
def MinkowDist(X, Y, p_value):
     
    # pass the p_root function to calculate
    # all the value of vector parallelly
    return (p_root(sum(pow(abs(a-b), p_value)
            for a, b in zip(X, Y)), p_value))