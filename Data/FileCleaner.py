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

def isAlmostAlpha(word):
    if word.isalpha():
        return 1
    if word[1:].isalpha():
        return 2
    if word[:-1].isalpha():
        return 3
    if word[1:-1].isalpha():
        return 4
    return 0

def giveAlpha(word):
    assert isAlmostAlpha(word)!=0, "giveAlpha only works if isAlmostAlpha!=0."
    if isAlmostAlpha(word)==1:
        return word
    if isAlmostAlpha(word)==2:
        return word[1:]
    if isAlmostAlpha(word)==3:
        return word[:-1]   
    if isAlmostAlpha(word)==4:
        return word[1:-1] 
        
    
def removeWords(line):
    # replaces english words for an equal number of spaces
    #
    for word in line.split():
        # wordNoPunct=word.strip(punctuation)
        replace=False
        alphaword=word
        if isAlmostAlpha(word)!=0:
            alphword = giveAlpha(word)
            with open("Dict3000.txt") as dic:
                for dicw in dic.readlines():
                    if alphaword.lower() == dicw.strip("\n"):
                        replace=True
                        break;
            if not replace:
                with open("Dict58000.txt") as dic:
                    for dicw in dic.readlines():
                        if alphaword.lower() == dicw.strip("\n"):
                            replace=True
                            break;
        if replace:
            # print(line)
            line = line.replace(alphaword, " "*len(alphaword))
            # print(line)
    
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
    
    with open(oldLoc+"/"+filename,"r",encoding="utf8",errors="replace") as oldF, open(newLoc+"/"+filename,"w",encoding="utf8",errors="replace") as newF:
        for line in oldF.readlines():
            newline = removeWords(line)
            if not isWhitespace(newline):
                newF.write(newline)
            # if not explanation(line) and line!="\n":
            #     newF.write(line)
    

def cleaner(oldLoc,newLoc):
    # cleans all files in location
    for filename in os.listdir(path=oldLoc):
        print("                                   ", end="\r")
        print("Working on "+filename, end="\r")
        withoutExpla(oldLoc,filename,newLoc)
    
cleaner('RawASCII','DataASCII')