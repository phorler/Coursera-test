from PIL import Image
import os, sys

im = Image.open("DSC_0001.NEF")

imNew=im.convert('jpg')

imNew.save("DSC_0001.JPG")

