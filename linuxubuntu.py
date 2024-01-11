# -*- coding: utf-8 -*-
'''
#to install ubuntu linux
1-you can install it only in your computer
2-double boot, use it alongside your other os
3-use virtual box,its computer on top of your current computer, which makes perofrmance slow

for installation:
    download ubuntu, boot it to a usb
    and install the way you install windows

to open the terminal, CTL+ALT+T

commands:
pwd   -print workin directory
~     -home
cd /home - bring us to home directory
ls  - list directories in that dir we are
ls -la -it shows all the hidden files also
sudo apt update  -to check for software updates
sudo apt list --upgrade - to list the upgradable softwares
sudo apt upgrade - upgrades all those upgradable softwares
sudo apt search vlc - it searches all the vlc types, you choose what you want and install
sudo apt install vlc - it installs vlc
sudo apt rmove vlc  - removes vlc
sudo apt autoremove  - it removes all those packages which was related to the vlc which is deleted before
touch <filename>  - it creates a file
mkdir <dirname>   - it creates a directory
cp <filename to be copied> <directory name>  - it copies a file into a directory
cp <file> <dir>/<file2> - it copies a file into another file into another dir
cp /dir/dir/dir/filename ~  -it copies the file to the home dir
cd ..   - it takes us back one directory
mv <filename> <dir>/<filetonamecopiedto> 
rm <filename>  -it removes a file 
rm -r <dirname> - it removes a dir
rm *  - rmoves everything in the dir you are
text editors:
nano <filename.extention> - it creates and opens a text file, where you can write stuff
CTL+C - it shows all nano files
vi <filename.txt> - it creates a vim file
vim commands:
    i - insert text
    a - append text
    dd  - delete
    :w - to write
    yy - yank text or copy text
    p  - paste text

man ls- it gets all the info about ls
or 
ls --help - it also get info about ls

to find a dir or:
find Documents - it finds the Document dir
/  - root
~  - home
ls - lists all dir
ls | grep Documents - it filters documents from ls
ls >> output.text - list all files in output.txt file
cat output.txt  - it shows the content of output.txt

echo 'hello world' - it shows the text in the terminal

echo 'hello world' | cat >> output.txt  - it appends the text into the output.txt
tail <filename>  -it shows the last ten content of the file
head <filename>  -it show the first ten content of the file

echo $USER -it shows the user

create an alias or variables:

    alias showuser='echo $USER'
    showuser - it shows the user

to install an app from downloads that you downloaded:
    
    sudo dpkg -i <applfileextentions>
    
    
    
files shown int the following way when making ls-la:
    -rwx------ output.tx
    -rwxrwxrwx - testfile.txt
    -r---------- textfile.txt

rwx -stands for read,write and execute
so in the output file only user has the right to read,write and execute
in the testfile user and groups has the the right to read, write and execute
but in the last one only user reads, 
we can change the above privileges, like
removing group privileges
chmod go-rwx testfile.txt
now
-rwx------ - testfile.txt

to change user privilege


chmod u-wx output.txt
-r------ - output.txt




    '''
















































