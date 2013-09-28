import math
import random

def showName(b):
    if b == 1:
        return 'jiandoa'

    elif b == 2:
        return 'shitou'
    else:
        return 'bu'

def getresult(a,b):
    a=int(a)
    if a==b:
        return 0
    elif  (a==1 and b==2) or (a==2 and b==1) or (a==3 and b==1) :
        return -1
    else:
        return 1

def showrz(rz):
    if rz==0:
        return ('pingju')
    elif  rz==-1 :
        return ('you lose')
    else:
        return ('u win')

def go():
    """


    """
    total=totalb=0
    while total<3 and totalb<3:

        a=int(raw_input('your turn! jiandao 1 ,shitou 2,bu 3:'))
        if a<1 or a>3:
            continue
        b=random.randint(1,3)

        item= getresult(a, b)
        if item==1:
            total+=1
        elif item==-1:
            totalb+=1
        print showName(a)+" X "+showName(b) +'       '+showrz(getresult(a,b)),total,"|",totalb

go()


