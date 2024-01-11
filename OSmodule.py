# -*- coding: utf-8 -*-
import os
from datetime import datetime
#to see all functions
print(dir(os))


#get current working directory
print(os.getcwd())

#to change our current working dir
os.chdir('/Users/Hamdard PC/allData')

#to see all the files and folder in our cwd
print(os.listdir())

#to see all contents of another folder we need to pass its path
print(os.listdir('/Users/Hamdard PC'))

#to create a folder somewhere, it can create files too
#1- it is one level,
os.mkdir('os-demo-1')

#2- it is used for both one level and two level
os.makedirs('os-demo-2/os-demo')

#to remove folders
os.rmdir('os-demo-1')

os.removedirs('os-demo-2/os-demo')

#to rename a folder or file
os.rename('os-demo-1', 'demo')

#to get info of the file
print(os.stat('datetime.py'))
#getting the size of file in bytes
print(os.stat('datetime.py').st_size)
#last modification time
print(os.stat('datetime.py').st_mtime)
#to make the timestamp readable
mod_time=os.stat('datetime.py').st_mtime
print(datetime.fromtimestamp(mod_time))

#to loop through all the directories of a folder
#os.walk() returns a tuple of three elements

for dirpath,dirnames,filenames in os.walk("C:/Users/Hamdard PC/allDATA/Modules learning"):
    print('Current Path:',dirpath)
    print('Directores:',dirnames)
    print('Files:', filenames)

#all the folders in the environment, or os as a whole
print(os.environ)
for i in os.environ:
    print(i+'--->'+os.environ[f'{i}'])
    
#following both are same, they return the value    
print(os.environ['APPDATA'])
print(os.environ.get('APPDATA'))

#if the first argument exist it returns the value for that else the second argument is returned
print(os.environ.get('APPDATA','EC2'))

print(os.environ.get('modules','EC2'))


#to join a file to a path
os.path.join('demo', 'Tutorial.html')

#getting basename which is file's name
print(os.path.basename('/tmp/test.txt'))
#directory name
print(os.path.dirname('/tmp/test.txt'))

#split
print(os.path.split('/tmp/test.txt'))

#to check if a path exists
print(os.path.exists('/tmp/test.txt'))

#to check if a path is file or dir

print(os.path.isfile('mapp.txt'))

print(os.path.isdir('demo'))

#split, split the extension and the paths
print(os.path.splitext('/tmp/test.txt'))

#all functionalities
print(dir(os.path))



#adding a new environment variable
os.environ['GeeksForGeeks']= 'www.geeksforgeeks.com'
print(os.environ['GeeksForGeeks'])

#modifying an environment variable

os.environ['GeeksForGeeks']= 'www.keeksforkeeks.com'
print(os.environ['GeeksForGeeks'])


















