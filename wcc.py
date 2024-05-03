import sys, os, re

def wordcounting (filename):
    nlines = 0 
    nwords = 0
    nchars = 0
    nlow   = 0 #lowercase letters
    nupp   = 0 #uppercase letters
    #open file in read mode
    file = open("C:/Users/91965/Surya.txt",'r')
    #go over every line
    for line in file:
    #increment nlines by one
        nlines = nlines + 1
        nwords = nwords + len(line.split())
        nchars = nchars + len(line) #Anzahl der Zeichen
        for i in line:
            if(i.islower()):
                nlow = nlow + 1
            elif(i.isupper()):
                nupp = nupp + 1
    file.close()
    #return(tuple((nlines,nwords,nchars,nlow,nupp)))
    d={"nlines":nlines,"nwords":nwords,"nchars":nchars,"nlow":nlow,"nupp":nupp}
    return(d)

def usage(argv):
    print("Usage: %s [-l|-c|-w] FILENAME" % argv[0])

### longer help message
def help (argv):
    print("Application name, Author, Date\n")
    usage(argv)
    print("\n   Mandatory arguments:")
    print("      arg1 : FILENAME")
    print("\n   Optional arguments:")
    print("      arg1 : OTHERARG")
    
def main(argv):
    if len(argv) < 2:
        usage(argv)
    elif "-h" in argv or "--help" in argv:
        help(argv)
    else:
        print("main is running")
        if len(argv) == 2:
            if os.path.isfile(argv[1]):
                print(wordcounting(argv[1]))
            else:
                print("Error file '%s' does not exists!" % argv[1])
        elif len(argv) == 3:
            if argv[1] in ["-w", "-l", "-c"]:
                print("fine")
                if os.path.isfile(argv[2]):
                    res=wordcounting(argv[2])
                    if argv[1] == "-l":
                        print("%10s    %s" % (res['nlines'], argv[2]))
                    elif argv[1] == "-w":
                        print("%10s    %s" % (res['nwords'], argv[2]))
                    elif argv[1] == "-c":
                        print("%10s    %s" % (res['nchars'], argv[2]))
                    
                           
                    
                else:
                    print("Error file '%s' does not exists!" % argv[2])
            else:
                print("Error: Options '%s' is invalid, use -c, -w or -l!" % argv[1])
            
            
### check if this file is the main script 
### so if is started: python3 FILENAME ...
if "__main__" == __name__:
    main(sys.argv)

#print(wordcounting())