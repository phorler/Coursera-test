import os
import shutil
import re


def main():

    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    sourceFolder=r"E:\Google photos back up\cleaned"
    targetFolder=r"E:\Google photos back up\cleaned\Sorted"

    totalFilesCopied=0
    filesAlreadyPresent=0

    print("Copying files from " + sourceFolder + " to " + targetFolder)

    for archFolder in range(2,42):

        archiveStr = str(archFolder)
#        print("Checking archive: " + archiveStr)
        if len(archiveStr) == 1:
            archiveStr="0" + archiveStr
        path = sourceFolder + "\\" + str(archFolder) + "\\takeout-20190314T083138Z-0" + archiveStr + "\\Takeout\\Google Photos\\"
#        print("Source path: " + path)
        # r=root, d=directories, f = files

        for r, d, f in os.walk(path):
            for folder in d:
                month, year = getYearMonth(folder)
                if year == "": 
                     destination = folder
                     try:
                        os.makedirs(targetFolder + "\\" + folder)
                     except:
                         pass
#                        print(targetFolder + "\\" + folder + " already exists")
#                     if not os.path.isdir(targetFolder + "\\" + folder):                     
                elif month == "":
                    destination = year
                else:
                    destination = year + r"\\" + month + " " + year
#                print(destination)

                filePath = path +  folder

#                print(filePath)

                for fr, fd, ff in os.walk(filePath):
                    filesProcessed=1
#                    print("Processing " + str(len(ff)) + " files in " + folder)                     
                    for file in ff:
                        filesProcessed=filesProcessed + 1
 #                       print("Copy " + filePath + "\\" + file + " to " + targetFolder + "\\" + destination  + "\\" + file)
                        if not os.path.isfile(targetFolder + "\\" + destination  + '\\' + file):
                            try:
                                shutil.copyfile(filePath + '\\' + file,targetFolder + "\\" + destination  + '\\' + file)
                                totalFilesCopied = totalFilesCopied + 1
                            except:
                                print(filePath + "\\" + file + " not found")
                                print("Or destination not found: " + targetFolder + "\\" + destination  + '\\' + file)

                        else:
                            # check the file size and if not the same rename the file and try again
                            filesAlreadyPresent=filesAlreadyPresent+1

                    print(str(totalFilesCopied) + " files copied so far. Files already present: " +  str(filesAlreadyPresent) + " Total: " +  str(filesAlreadyPresent +  totalFilesCopied))

def getYearMonth(folder):

    #use separate function to pull year and month out of a folder name

    # is it a year only (YYYY), pol (MMM YYYY) format or a google format (YYYY-MM-DD) or something else?

    months=['January','February','March','April','May','June','July','August','September','October','November','December']

    folderName = folder.split() 

    if re.search("^[12][09][0-9][0-9]-[01][0-9]-[0123][0-9]",folder):
        year=folder[0:4]
        monthNum=int(folder[5:7])
   
        month=months[monthNum-1]
#        print("Google format: " + folder + " To folder " + month + " " + year)
        return(month,year)

        
    elif folderName[0] in months:
        if re.search("^[12][09][0-9][0-9]",folderName[1]):
            month = folderName[0]
            year = folderName[1]
#            print("Pol format: " + folder)
            return(month,year)

    elif re.search("^[12][09][0-9][0-9]",folder):
#        print("Pol year only format: " + folder)
        year = folder
        return("",year)


    else:
#        print("Not a standard folder name: " + folder)
        return("","")

main()