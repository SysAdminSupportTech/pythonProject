#Build
import os, glob
def spiderCrawler(ext):
    print("Welcome to our Spider Crawler Application two")
    rtpath = r"C:\Users\DeptAdmin" #Creating Variable root path
    #Getting the index Value of the file and Folder
    fileFolders = os.listdir(rtpath)
    for item in fileFolders:
        itemIndex = fileFolders.index(item)
        if os.path.isdir(os.path.join(rtpath,item)):
            item_path = rtpath + "\\" + item + "\\" #Getting the absolute path of the document
            try:
                item_Count = len(os.listdir(os.path.join(rtpath,item_path)))
                print("{}. {} ({})".format(itemIndex,item, item_Count))
            except PermissionError:
                pass
        else:
            print("{}. {}".format(itemIndex, item))
    
spiderCrawler('txt')
