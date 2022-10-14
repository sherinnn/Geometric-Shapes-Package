def triPyrVol(BaseLen, BaseHeight, PyramidHeight):
    if(BaseLen, BaseHeight, PyramidHeight <=0):
        return 0
    return (0.1666) * BaseLen * BaseHeight * PyramidHeight
 
def sqPyrVol(BaseLen, PyramidHeight):
    if(BaseLen, PyramidHeight <=0):
        return 0
    return (0.33) * BaseLen * BaseLen * PyramidHeight

def pentPyrVol(BaseLen, BaseHeight, PyramidHeight):
    if(BaseLen, BaseHeight, PyramidHeight <=0):
        return 0
    return (0.83) * BaseLen * BaseHeight * PyramidHeight

def HexPyrVol(BaseLen, BaseHeight, PyramidHeight):
    if(BaseLen, BaseHeight, PyramidHeight <=0):
        return 0
    return BaseLen * BaseHeight * PyramidHeight