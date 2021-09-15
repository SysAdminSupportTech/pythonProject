https://www.youtube.com/watch?v=fvvJC-17cDA

indexVal = rtpathContent.index(fileFolder)
        #Print each item in the directory of the root folder
        for itemVal in rtpathContent:
            if os.path.isdir(itemVal):
                try:
                    pathName = os.listdir(itemVal)
                    filePath = os.path.dirname(os.path.abspath(str(pathName)))
                    print(f'{pathName}{filePath}')
                except PermissionError:
                    pass
            else:
                pass
                #dirPathFile = os.path.dirname(os.path.abspath(itemVal))
                #print(f'{dirPathFile}{itemVal}')

                dirContent = os.listdir(os.path.join(rtpath,item))
                for file in dirContent:
                    if os.path.isfile(file):
                        print(file)
                    
for item in os.listdir(rtpath):
        try:
            if os.path.isdir(os.path.join(rtpath,item)):
                print("{} Directory".format(item))  
            else:
                print("{} File".format(item))
        except PermissionError:
            pass