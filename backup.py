import shutil
import os

s=input("Enter Source Folder(thing you want to copy from) : ")
d=input("Enter Destination Folder(thing you want to copy to) : ")

s=s+"/"
d=d+"/"

fileList=os.listdir(s)
for file in fileList:
    shutil.copy( (s+file), (d))