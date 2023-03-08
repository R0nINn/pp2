
import os
import sys


path1 = os.access('python.txt' , os.F_OK)
print('Exist path:' , path1)

path2 = os.access('pyhron.txt' , os.R_OK)
print( 'It acceses to read:' , path2)

path3 = os.access('python.txt' , os.W_OK)
print('It acceses to write:' , path3)

path4 = os.access('python.txt' , os.X_OK)
print('Check if path can be executed:' , path4)

# os.access()
# This function uses real uid/gid to test if the invoking user has access to the path.


import os

path = "C:\Users\VivoBook\Desktop\c++\git_tutorial\work\pp2\lab6\python.txt"

if os.path.exists(path):
    file_name = os.path.basename(path)
    print(file_name)
else:
    print("This file in puth does not exist")

#This code print name of file 
#for example: This path exists and my output will be file.txt

if os.path.exists(path):
    print(path)
else:
    print("This file it puth does not exist")
    
#A this code print all puth if file exists 


import os
path  = "C:\Users\VivoBook\Desktop\c++\git_tutorial\work\pp2\lab6\python.txt"
file = open(path, "r")
cnt = 0
Read = file.read()
List = Read.split("\n")
for item in List:
    if item:
        cnt+=1
print(cnt)

import os 

path  = "C://Users//GTA//Desktop//pp2//lab6//directory and files//5.txt"

file = open(path, "w")
items = ['apple', 'banana','orange']

for i in items:
    file.write(i+"\n")
file.close()


import os
import shutil
path_1 = "C://Users//VivoBook//Desktop//c++//git_tutorial//work//pp2//lab6//7//first.txt"
path_2 = "C://Users//VivoBook//Desktop//c++//git_tutorial//work//pp2//lab6//7//second.txt"

with open(path_1, "r") as first, open (path_2, 'w') as second:
    for item in first:
        second.write(item)

first.close()
second.close()

import os

Delete_file = "delete.txt"

path = "C:\\Users\\GTA\\Desktop\\pp2\\lab6\\directory and files\\8"

location = os.path.join(path, Delete_file)

try:
    os.remove(path)
except:
    print("The specified file not found")
#if os.path.exists(path):
 #   if not os.path.join(path, Delete_file):
 #       print("The specified file not found")
 #   else:
  #      os.remove(os.path.join(path,Delete_file))
