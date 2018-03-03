import re

rawColor = open("../resources/colors.txt","r")
sortedColor = rawColor.read().split('\n')
#print (sortedColor)
#print (len(sortedColor))
rawColor.close()

def getBlueViolet():
    searchedBlueViolet = re.compile('(BV)(?=\d{2,4})')
    blueVioletList = filter(searchedBlueViolet.match, sortedColor)
    return blueVioletList

def getViolet():
    searchedViolet = re.compile('(V)(?=\d{2,4})')
    violetList = filter(searchedViolet.match, sortedColor)
    return violetList

def getRedViolet():
    searchedRedViolet = re.compile('(RV)(?=\d{2,4})')
    redVioletList = filter(searchedRedViolet.match, sortedColor)
    return redVioletList

def getRed():
    searchedRed = re.compile('(R)(?=\d{2,4})')
    redList = filter(searchedRed.match, sortedColor)
    return redList

def getYellow():
    searchedYellow= re.compile('(Y)(?=\d{2,4})')
    yellowList = filter(searchedYellow.match, sortedColor)
    return yellowList

def getYellowRed():
    searchedYellowRed = re.compile('(YR)(?=\d{2,4})')
    yellowRedList = filter(searchedYellowRed.match, sortedColor)
    return yellowRedList

def getYellowGreen():
    searchedYellowGreen = re.compile('(YG)(?=\d{2,4})')
    yellowGreenList = filter(searchedYellowGreen.match, sortedColor)
    return yellowGreenList

def getGreen():
    searchedGreen = re.compile('(G)(?=\d{2,4})')
    greenList = filter(searchedGreen.match, sortedColor)
    return greenList

def getBlueGreen():
    searchedBlueGreen= re.compile('(BG)(?=\d{2,4})')
    blueGreenList = filter(searchedBlueGreen.match, sortedColor)
    return blueGreenList

def getBlue():
    searchedBlue = re.compile('(B)(?=\d{2,4})')
    blueList = filter(searchedBlue.match, sortedColor)
    return blueList

def getEarth():
    searchedEarth = re.compile('(E)(?=\d{2,4})')
    earthList = filter(searchedEarth.match, sortedColor)
    return earthList

def getCoolGray():
    searchedCoolGray = re.compile('(C-)(?=\d{1,4})')
    coolGrayList = filter(searchedCoolGray.match, sortedColor)
    return coolGrayList

def getWarmGray():
    searchedWarmGray = re.compile('(W-)(?=\d{1,4})')
    warmGrayList = filter(searchedWarmGray.match, sortedColor)
    return warmGrayList

def getNeutralGray():
    searchedNeutralGray = re.compile('(N-)(?=\d{1,4})')
    neutralGrayList = filter(searchedNeutralGray.match, sortedColor)
    return neutralGrayList

def getTonerGray():
    searchedTonerGray = re.compile('(T-)(?=\d{1,4})')
    tonerGrayList = filter(searchedTonerGray.match, sortedColor)
    return tonerGrayList

def getAchromatic():
    searchedAchromatic = re.compile('(0|100|110)')
    achromaticList = filter(searchedAchromatic.match, sortedColor)
    return achromaticList

def getFluorescent():
    searchedFluorescent = re.compile('(F)')
    fluorescentList = filter(searchedFluorescent.match, sortedColor)
    return fluorescentList

def getAll():
    BV = getBlueViolet()
    V = getViolet()
    RV = getRedViolet()
    R = getRed()
    Y = getYellow()
    YR = getYellowRed()
    YG = getYellowGreen()
    G = getGreen()
    B = getBlue()
    BG = getBlueGreen()
    E = getEarth()
    C = getCoolGray()
    W = getWarmGray()
    N = getNeutralGray()
    T = getTonerGray()
    A = getAchromatic()
    F = getFluorescent()
    all = []
    all.extend(BV)
    all.extend(V)
    all.extend(RV)
    all.extend(R)
    all.extend(Y)
    all.extend(YR)
    all.extend(YG)
    all.extend(G)
    all.extend(BG)
    all.extend(B)
    all.extend(E)
    all.extend(C)
    all.extend(W)
    all.extend(N)
    all.extend(T)
    all.extend(A)
    all.extend(F)
    return all

#print([i for i in blueViolet])
#print([i for i in violet])
#print([i for i in redViolet])
#print([i for i in yellow])
#print([i for i in yellowRed])
#print([i for i in yellowGreen])
#print([i for i in green])
#print([i for i in blueGreen])
#print([i for i in blue])
#print([i for i in earth])
#print([i for i in coolGray])
#print([i for i in warmGray])
#print([i for i in neutralGray])
#print([i for i in tonerGray])
#print([i for i in achromatic])
#print([i for i in fluorescent])
