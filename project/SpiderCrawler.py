#Build
import os
print("Welcome to our Spider Crawler Application")
def spiderCrawler(ext):
    rtpath = "C:\\" #Creating Variable root path
    stlocation = os.chdir(rtpath) #Set Location to root folder
    rtpathContent = os.listdir() #Get content of C:\ dir
    for fileFolder in rtpathContent:
        indexVal = rtpathContent.index(fileFolder)
        print("{}.{}".format(indexVal, fileFolder))

        #Print each item in the directory of the root folder
        for itemVal in rtpathContent:
            if os.path.isdir(itemVal):
                try:
                    DisplayContent = os.listdir(itemVal)
                    countItem = len(os.listdir(itemVal))
                    print(80*"-")
                    print("{} ({})".format(itemVal, countItem))
                    print(DisplayContent)
                    
                except PermissionError:
                    print("{} Access Denied".format(itemVal))
            else:
                print(itemVal)
spiderCrawler('.txt')

