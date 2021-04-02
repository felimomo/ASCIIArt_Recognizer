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
                

def withoutExpla(oldLoc,filename,newLoc):
    # creates new file with no explanations nor whitespace (easier than 
    # creating a new file per art piece, hopefully correlations are similar 
    # enough to not be a problem.
    
    with open(oldLoc+filename,"r") as oldF, open(newLoc+filename,"w") as newF:
        for line in oldF.readlines():
            if not explanation(line) and line!="\n":
                newF.write(line)
    

def cleaner(oldLoc,newLoc):
    # cleans all files in location
    for filename in os.scandir(path=location):
        assert filename.path.endswith(".txt"), "Found non .txt file."
        eraseExpla(location,filename)
        separate(location,filename)
    
cleaner('./RawData')