#!/usr/bin/python3
#coding: utf8

import os
import sys
import fnmatch
import subprocess

dirPath = r'/cygdrive/folder/with/images'
irfanview = r'/cygdrive/c/Program Files/IrfanView/i_view32.exe' # Choose your program

def showImage(rootName, fileName):
	#print ("\n %s" % os.path.join(rootName,fileName))
	os.chdir(os.path.join(dirPath,rootName))
	subprocess.Popen([irfanview,fileName])
	return

def main():

	imgCounter = 0

	if len(sys.argv) > 1:
		searchParam = sys.argv[1]
		regExpParam = '*' + searchParam + '*.*'
	else:
		print ("Enter a search parameter")
		exit()
	
	if not os.path.exists(dirPath):
		print ("\n Can\'t find directory %s - Connect to server" % dirPath)
		exit()

	for root, subDir, files in os.walk(dirPath):
		for file in files:
			if fnmatch.fnmatch(file, regExpParam):
				showImage(root, file)
				imgCounter += 1
				
	if (imgCounter == 0):
		print("%s not found!" % searchParam)
	else:
		print("%d matches for %s" % (imgCounter,searchParam))

if __name__ == '__main__': 
    main()
