def addWord(w,wcDict):
    if w in wcDict:
        wcDict[w]+=1
    else:
        wcDict[w]=1

import string
def processLine(line,wcDict):
    line=line.strip()
    wordList=line.split()
    for word in wordList:
        if word!='-':
            word=word.lower()
            word=word.strip()
            word=word.strip(string.punctuation)
            addWord(word,wcDict)

def prettyPrint(wcDict):
    valKeyList=[]
    for key,val in wcDict.items():
        valKeyList.append((val,key))
    valKeyList.sort(reverse=True)
    print '%-10s%10s'%('Word','Count')
    print '_'*21
    for val,key in valKeyList:
        print '%-12s  %3d'%(key,val)

def main():
    wcDict={}
    fObj=open('gettysburg.txt','r')
    for line in fObj:
        processLine(line,wcDict)
    print 'Length os dic:',len(wcDict)
    prettyPrint(wcDict)


main()