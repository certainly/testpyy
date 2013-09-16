import os

def make_text_file():

        # a=open('text.txt',"a")
        # a.write("""dff
        # dddrxd""")
        # a.close()
    a=open('text.txt',"r")
    text=a.readlines();
    for line in text:
        print (len(line))


make_text_file();