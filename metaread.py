#from PIL import Image
#image = Image.open("Stared.jpg") 


from PIL import Image
from PIL.ExifTags import TAGS
image = Image.open("Stared.jpg") 
print(image) 
info = image._getexif() 
for tag, value in info.items(): 
    key = TAGS.get(tag, tag) 
    print(key + " " + str(value)) 