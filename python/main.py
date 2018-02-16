import re

rawColor = open("../resources/colors.txt","r")
sortedColor = rawColor.read().split('\n')
#print (sortedColor)
#print (len(sortedColor))
rawColor.close()


searchedBlueViolet = re.compile('(BV)(?=\d{2,4})')
blueVioletList = filter(searchedBlueViolet.match, sortedColor)
#print([i for i in blueVioletList])

searchedViolet = re.compile('(V)(?=\d{2,4})')
violetList = filter(searchedViolet.match, sortedColor)
#print([i for i in violetList])

searchedRedViolet = re.compile('(RV)(?=\d{2,4})')
redVioletList = filter(searchedRedViolet.match, sortedColor)
#print([i for i in redVioletList])

searchedYellow= re.compile('(Y)(?=\d{2,4})')
yellowList = filter(searchedYellow.match, sortedColor)
#print([i for i in yellowList])

searchedYellowRed = re.compile('(YR)(?=\d{2,4})')
yellowRedList = filter(searchedYellowRed.match, sortedColor)
#print([i for i in yellowRedList])
    
searchedYellowGreen = re.compile('(YG)(?=\d{2,4})')
yellowGreenList = filter(searchedYellowGreen.match, sortedColor)
#print([i for i in yellowGreenList])

searchedGreen = re.compile('(G)(?=\d{2,4})')
greenList = filter(searchedGreen.match, sortedColor)
#print([i for i in greenList])

searchedBlueGreen= re.compile('(BG)(?=\d{2,4})')
blueGreenList = filter(searchedBlueGreen.match, sortedColor)
#print([i for i in blueGreenList])

searchedBlue = re.compile('(B)(?=\d{2,4})')
blueList = filter(searchedBlue.match, sortedColor)
#print([i for i in blueList])

searchedEarth = re.compile('(E)(?=\d{2,4})')
earthList = filter(searchedEarth.match, sortedColor)
#print([i for i in earthList])

searchedCoolGray = re.compile('(C-)(?=\d{1,4})')
coolGrayList = filter(searchedCoolGray.match, sortedColor)
#print([i for i in coolGrayList])

searchedWarmGray = re.compile('(W-)(?=\d{1,4})')
warmGrayList = filter(searchedWarmGray.match, sortedColor)
#print([i for i in warmGrayList])

searchedNeutralGray = re.compile('(N-)(?=\d{1,4})')
neutralGrayList = filter(searchedNeutralGray.match, sortedColor)
#print([i for i in neutralGrayList])

searchedTonerGray = re.compile('(T-)(?=\d{1,4})')
tonerGrayList = filter(searchedTonerGray.match, sortedColor)
#print([i for i in tonerGrayList])

searchedAchromatic = re.compile('(0|100|110)')
achromaticList = filter(searchedAchromatic.match, sortedColor)
#print([i for i in achromaticList])

searchedFluorescent = re.compile('(F)')
fluorescentList = filter(searchedFluorescent.match, sortedColor)
#print([i for i in fluorescentList])

