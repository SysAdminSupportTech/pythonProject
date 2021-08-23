import os
def spiderCrawler(fileExt):
    print("Welcome to our Spider Crawler Application two")
    rtpath = r"C:\\" #Creating Variable root path
    #Getting the index Value of the file and Folder
    fileFolders = os.listdir(rtpath)
    for dirName, subdirs, fileList in os.walk(rtpath,topdown=False):
        for name in fileList:
            if name.endswith(fileExt):
                print("{}".format(name))

spiderCrawler(".ps1")
