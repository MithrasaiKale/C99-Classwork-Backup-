import os
import shutil

path = input("enter the name of the directory to be sorted : ")

list_of_files = os.listdir(path)

for file in list_of_files:
     name, ext = os.path.splitext(file)
     myext = ext[1:]
     ## This forces the next iteration, if it is the directory
     if myext == '':
          continue
     if os.path.exists(path+'/'+myext):
          shutil.move(path+'/'+file, path+'/'+myext+'/'+file)
     else:
          os.makedirs(path+'/'+myext)
          shutil.move(path+'/'+file, path+'/'+myext+'/'+file)