import sys
import re
from sys import exit

def usage():
    print("Word and Line counter by Detlef Groth, Uni Potsdam, 2022")
    print("Usage: appname [-h -clw] filename1 [filename2 ...]")
    print("  Options are:")
    print("     -h   - seeing this help page")
    print("     -c   - counting only chars")
    print("     -l   - counting only lines")
    print("     -w   - counting only words")
    exit()

def wc(filename, lines=True, word=True, chars=True):
    nlines = 0
    nwords = 0
    nchars = 0
    nlow = 0
    nupp = 0
    with open(filename, 'r') as file:
        for line in file:
            nlines += 1
            nchars += len(line)
            nwords += len(line.split())
            nlow += sum(1 for char in line if char.islower())
            nupp += sum(1 for char in line if char.isupper())
    return nlines, nwords, nchars, nlow, nupp, filename

def main(args):
    if len(args) <= 1 or "-h" in args:
        usage()

    word = False
    lines = False
    chars = False

    files = []
    options = set(args[1:])
    for item in options:
        match = re.search('^-[a-z]*w', item)
        if match:
            word = True
        match = re.search('^-[a-z]*l', item)
        if match:
            lines = True
        match = re.search('^-[a-z]*c', item)
        if match:
            chars = True

    for filename in args[2:]:
        files.append(wc(filename, lines, word, chars))

    for res in files:
        res2 = []
        if lines:
            res2.append(res[0])
        if word:
            res2.append(res[1])
        if chars:
            res2.append(res[2])
        res2.append(res[len(res) - 1])

        for item in res2:
            print(str(item) + "\t", end="")
        print("")

if __name__ == "__main__":
    # Example usage: python script.py -lcw file1.txt file2.txt file3.txt
    main(sys.argv)
