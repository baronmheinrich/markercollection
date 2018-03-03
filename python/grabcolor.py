import re
import time
import random
import shutil
import requests
import colorLists as cList

blueViolet = cList.getBlueViolet()
violet = cList.getViolet()
redViolet = cList.getRedViolet()
red = cList.getRed()
yellow = cList.getYellow()
yellowRed = cList.getYellowRed()
yellowGreen = cList.getYellowGreen()
green = cList.getGreen()
blueGreen = cList.getBlueGreen()
blue = cList.getBlue()
earth = cList.getEarth()
coolGray = cList.getCoolGray()
warmGray = cList.getWarmGray()
neutralGray = cList.getNeutralGray()
tonerGray = cList.getTonerGray()
achromatic = cList.getAchromatic()
fluorescent = cList.getFluorescent()
all = cList.getAll()


for color in blueViolet:
    restTimer = random.uniform(1,2)
    time.sleep(restTimer)
    url = 'https://copic.jp/images/color/Sample_'color.trim()+'@2x.jpg'
    response = requests.get(url).content
    with open('../colors/'+color.trim()+'.jpg', 'wb') as out_file:
        out_file.write(response)
