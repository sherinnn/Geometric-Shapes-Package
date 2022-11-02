# import math
# from math import *
# from decimal import Decimal

# def EucDist(*args):
#     if len(args)==4:
#         x1 = args[0]
#         x2 = args[1]
#         y1 = args[2]
#         y2 = args[3]
#         if(type(x1).__name__ in ['int', 'float'] and type(x2).__name__ in ['int', 'float'] and type(y1).__name__ in ['int', 'float'] and type(y2).__name__ in ['int', 'float']):
#                 if(x1>=0 and x2>=0 and y1>=0 and y2>=0):
#                     return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)
#                 else:
#                     return "Invalid input"
#         else:
#                 return "Invalid Input" 
#     else:    
#         return "Please enter only 4 arguments"

# def ManDist(*args):
#     if len(args)==4:
#         x1 = args[0]
#         x2 = args[1]
#         y1 = args[2]
#         y2 = args[3]
#         if(type(x1).__name__ in ['int', 'float'] and type(x2).__name__ in ['int', 'float'] and type(y1).__name__ in ['int', 'float'] and type(y2).__name__ in ['int', 'float']):
#                 if(x1>=0 and x2>=0 and y1>=0 and y2>=0):
#                     return math.fabs(x2 - x1) + math.fabs(y2 - y1)
#                 else:
#                     return "Invalid input"
#         else:
#                 return "Invalid Input" 
#     else:
#         return "Please enter only 4 arguments"
    
# # Function distance between two points
# # and calculate distance value to given
# # root value(p is root value)
# def p_root(value, root):
     
#     root_value = 1 / float(root)
#     if(value,root>0):
#         return round (Decimal(value) **Decimal(root_value), 3)
#     else:
#         return 0
 
# def MinkowDist(*args):
#     if len(args)==3:
#         X = args[0]
#         Y = args[1]
#         p_value = args[2]
        
#         if(type(X).__name__ in ['int', 'float'] and type(Y).__name__ in ['int', 'float'] and type(p_value).__name__ in ['int', 'float']):
#                 if(X>=0 and Y>=0 and p_value>=0):
#                         return (p_root(sum(pow(abs(a-b),p_value) 
#                         for a, b in zip(X, Y)), p_value))
#                 else:
#                     return "Invalid input"
#         else:
#                 return "Invalid Input"    
#     else: 
#         return "Please enter only 4 arguments"
    # pass the p_root function to calculate
    # all the value of vector parallelly


