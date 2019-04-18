import os
from iptcinfo3 import IPTCInfo
import shutil

sourceFolder=r"z:\photos"
targetFolder=r"z:\photos\favorites"

totalFilesCopied=0
totalFilesRead=0
totalFilesChecked=0
missingIni=list()

print("Copying favorites from " + sourceFolder + " to " + targetFolder)

months=['January','February','March','April','May','June','July','August','September','October','November','December']

totalFilesProcessed=0
totalFilesCopied=0
existingFile=0

for yearInt in range(2012,2020):
    year=str(yearInt)
    for month in months:
        currentFolder=sourceFolder +"\\" + year + "\\" + month + " " + year
        destFolder=targetFolder +"\\" + year + "\\" + month + " " + year

        print("Current folder being processes: "+ currentFolder)

        filesProcessed=0
        filesCopied=0

        try:
            iniFile=open(currentFolder + "\\.picasa.ini","r")
        except:
            try:
                iniFile=open(currentFolder + "\\picasa.ini","r")
            except:
                print("No picasa.ini file found")
                missingIni.append(currentFolder)

        imageName=""
        for line in iniFile:            
            if imageName!="":
            
                if line[0:4]=="star":
                    filesCopied=filesCopied+1
                    print("Star found in " + imageName)
                    if os.path.isfile(destFolder  + "\\" + imageName):
                         print("File aready in favorites.")
                         existingFile=existingFile+1
                    else:
                         print("Copying file "+ str(filesCopied) + " to favorites"),
                         try:
                             shutil.copyfile(currentFolder + "\\" + imageName,destFolder  + "\\" + imageName)
                         except:
                             print("File not found")
                    imageName=""

            if line[0:1]=="[":
                imageName=line[1:-2]
                filesProcessed=filesProcessed+1


        print("Files found in : " + month + " " + year + " : " + str(filesProcessed))
        print("Files copied   : " + str(filesCopied))

        totalFilesProcessed=totalFilesProcessed+filesProcessed
        totalFilesCopied=totalFilesCopied+filesCopied

print("Total number of files found    : " + str(totalFilesProcessed))
print("Total number of files copied   : " + str(totalFilesCopied))
print("The following folders contained no picassa.ini file")
for item in missingIni:
    print(item)


