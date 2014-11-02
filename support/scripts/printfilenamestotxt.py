 import os
import sys

rootdir = '../..'

validFiletype = ['html','png']
outputname = 'allfilenames.txt'
open(outputname, 'w').close()
with open( outputname, 'a' ) as txtFile:
    for root, subFolders, files in os.walk(rootdir):
            for filename in files:
                for type in validFiletype:
                    if type in filename:
                        txtFile.write(filename + '\n')
                        print(filename + '\n')
                        break
