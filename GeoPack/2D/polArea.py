def polArea(XArr, YArr, NumberofTerms):
    area = 0.0
    if(len(XArr) = 0 or len(XArr) != len(YArr)):
        return 0
    else:
 # Calculate value of shoelace formula
        j = NumberofTerms - 1
        for i in range(0,NumberofTerms):
                area += (XArr[j] + XArr[i]) * (YArr[j] - YArr[i])
                j = i   # j is previous vertex to i
                return int(abs(area / 2.0))
 
# Driver program to test above function
# X = [0, 2, 4]
# Y = [1, 3, 7]
# n = len(X)
# print(polygonArea(X, Y, n))