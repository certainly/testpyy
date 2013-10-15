# search for a string
#   starting from the current directory,walk a directory tree
#   look in all text files (extension ".txt") for the string

import os

#walk the directory subtree starting at the current directory
#search for searchStr,count files examined,
# keep lists of files found and directories

def check(searchStr,count,fileList,dirList):
    for dirName,dirs,files in os.walk("."):
        for f in files:
            if os.path.splitext(f)[1]==".txt":
                count+=1
                aFile=open(os.path.join(dirName,f),"r")
                fileStr=aFile.read()
                if searchStr in fileStr:
                    fileName=os.path.join(dirName,f)
                    fileList.append(fileName)
                    if dirName not in dirList:
                        dirList.append(dirName)
                aFile.close()
    return count

theStr=raw_input('What str to look for: ')
fileList=[]
dirList=[]
count=0

count=check(theStr,count,fileList,dirList)

print 'Looked at %d text files'%(count)
print 'Found %d directories containing files \with ".txt" suffix and target string:%s'\
    %(len(dirList),theStr)
print 'Found %d files with ".txt" suffix containing the target string: %s'\
    %(len(fileList),theStr)
print '\n*****Direc list***'
for d in dirList:
    print d
print '\n---FileList---'
for f in fileList:
    print f

