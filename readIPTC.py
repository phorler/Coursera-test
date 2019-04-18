import os
from iptcinfo3 import IPTCInfo
import shutil

sourceFolder=r"z:\photos"
targetFolder=r"z:\photos\favorites"

totalFilesCopied=0
totalFilesRead=0
totalFilesChecked=0

print("Copying favorites from " + sourceFolder + " to " + targetFolder)

#months=['January','February','March','April','May','June','July','August','September','October','November','December']
months=['March']

for yearInt in range(2015,2016):
    year=str(yearInt)
    for month in months:
        currentFolder=sourceFolder +"\\" + year + "\\" + month + " " + year
        destFolder=targetFolder +"\\" + year + "\\" + month + " " + year

#        currentFolder=r"c:\\Users\\Daffodil\\Pictures\\tmp"
#        destFolder=r"c:\\Users\\Daffodil\\Pictures\\tmp\\favorites"

        print("Current folder to be processes: "+ currentFolder)

        try:
            items = os.listdir(currentFolder)

        except:
            print("Folder not found: " + currentFolder)
            break

        print("Folder being searched: "+ currentFolder)

        totalNumberofFilestoProcess=len(items)

        numberofFilesProcessed=0

        numberFilesChecked=0

        numberFilesMoved=0

#        print(items)

        for name in items:
            numberofFilesProcessed=numberofFilesProcessed + 1

            print("Current file being processed: " + name + ", file "+ str(numberofFilesProcessed) + " of " + str(totalNumberofFilestoProcess))

            if name.endswith(".JPG") or name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".JPEG"):
                numberFilesChecked=numberFilesChecked+1

                print("File being checked " + currentFolder + "\\" + name)

                iptc = IPTCInfo(currentFolder + "\\" + name)

                print(iptc['keywords'])

                if iptc['keywords']==[b'Star']:
                    numberFilesMoved=numberFilesMoved+1
                    print("Star found in " + name + ". Copying file "+ str(numberFilesMoved) + " to favorites")
                    shutil.copyfile(currentFolder + "\\" + name,destFolder  + "\\" + name)


        totalFilesCopied = totalFilesCopied + numberFilesMoved
        totalFilesRead = totalFilesRead + totalNumberofFilestoProcess
        totalFilesChecked = totalFilesChecked + numberFilesChecked

print("Files read:    " + str(totalFilesRead))
print("Files checked: " + str(totalFilesChecked))
print("Files copied:  " + str(totalFilesCopied))


