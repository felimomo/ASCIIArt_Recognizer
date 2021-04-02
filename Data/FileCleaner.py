import os
from string import punctuation

def explanation(line):
    # detects whether a line is an explanation by looking into dictionary
    
    for word in line.split():
        word=word.strip(punctuation)
        with open("Dict.txt") as dic:
            for dicWord in dic.readlines():
                if dicWord.strip("\n") == word:
                    return True
    return False
    
def removeWords(line):
    # replaces english words for an equal number of spaces
    #
    for word in line.split():
        wordNoPunct=word.strip(punctuation)
        replace=False
        with open("Dict3000.txt") as dic:
            for w in dic.readlines():
                if wordNoPunct == w.strip("\n"):
                    print(line)
                    replace=True
                    break;
        line = line.replace(word, " "*len(word))
    
    print(line)
    return line

def isWhitespace(line):
    # returns whether the line is purely white space
    #
    if line.split() == []:
        return True
    return False
                

def withoutExpla(oldLoc,filename,newLoc):
    # creates new file with no explanations nor whitespace (easier than 
    # creating a new file per art piece, hopefully correlations are similar 
    # enough to not be a problem.
    
    with open(oldLoc+"/"+filename,"r") as oldF, open(newLoc+"/"+filename,"w") as newF:
        for line in oldF.readlines():
            newline = removeWords(line)
            if not isWhitespace(newline):
                newF.write(newline)
            # if not explanation(line) and line!="\n":
            #     newF.write(line)
    

def cleaner(oldLoc,newLoc):
    # cleans all files in location
    for filename in os.listdir(path=oldLoc):
        withoutExpla(oldLoc,filename,newLoc)
    
cleaner('RawASCII','DataASCII')