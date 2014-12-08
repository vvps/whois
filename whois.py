import os
import sys
import fnmatch
from PIL import Image

dirPath = r'I:\A_folder_with_photos_and_subfolders'

if len(sys.argv) > 1:
    searchParam = sys.argv[1]
    regExpParam = '*' + searchParam + '*.*'
else:
    print('Enter a search parameter')
    exit
    
if os.path.exists(dirPath):
    os.chdir(dirPath)
else:
    print('Directory does not exist - Connect to server')


def showImage(rootName, fileName):
    print (os.path.join(rootName,fileName))
    os.startfile(os.path.join(rootName,fileName))
    return


for root, subDir, files in os.walk('.'):
    for file in files:
        if fnmatch.fnmatch(file, regExpParam):
            showImage(root, file)
