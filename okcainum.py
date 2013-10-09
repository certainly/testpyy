import random
number=random.randint(0,100)

print 'game start'
print

guessString=raw_input("guess:")
guess=int(guessString)

while 0<=guess<=100:
    if guess>number:
        print("high")
    elif guess<number:
        print("low")
    else:
        print "u are right:",number
        break
    guessString=raw_input("guess:")
    guess=int(guessString)
else:
    print("nono:",number)
