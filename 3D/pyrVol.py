def triPyrVol(BaseLen, BaseHeight, PyramidHeight):
    return (0.1666) * BaseLen * BaseHeight * PyramidHeight
 
def sqPyrVol(BaseLen, PyramidHeight):
    return (0.33) * BaseLen * BaseLen * PyramidHeight

def pentPyrVol(BaseLen, BaseHeight, PyramidHeight):
    return (0.83) * BaseLen * BaseHeight * PyramidHeight

def HexPyrVol(BaseLen, BaseHeight, PyramidHeight):
    return BaseLen * BaseHeight * PyramidHeight