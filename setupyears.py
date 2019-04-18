import os
import shutil

#targetFolder=r"z:\photos\favorites"
targetFolder=r"E:\Google photos back up\Cleaned\Sorted"

months=['January','February','March','April','May','June','July','August','September','October','November','December']

for yearInt in range(1937,2020):
    year=str(yearInt)
    print("Creating folders for " + year)
    os.makedirs(targetFolder + "\\" + year)
    for month in months:
        os.makedirs(targetFolder + "\\" + year + "\\" + month + " " + year)