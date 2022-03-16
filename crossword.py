import itertools
import numpy as np

def main():
    input1Graph = [ ["+","-","+","+","+","+","+","+","+","+"],
                    ["+","-","+","+","+","+","+","+","+","+"],
                    ["+","-","+","+","+","+","+","+","+","+"],
                    ["+","-","-","-","-","-","+","+","+","+"],
                    ["+","-","+","+","+","-","+","+","+","+"],
                    ["+","-","+","+","+","-","+","+","+","+"],
                    ["+","+","+","+","+","-","+","+","+","+"],
                    ["+","+","-","-","-","-","-","-","+","+"],
                    ["+","+","+","+","+","-","+","+","+","+"],
                    ["+","+","+","+","+","-","+","+","+","+"],  
                ]
    input1Words = ["LONDON","DELHI","ICELAND","ANKARA"]
    
    
    print(Crossword(input1Graph,input1Words));
    
def Crossword(inputGraph, words):
    def GetHorizontalLength(i,j):
        hLength = 1
        lengthFound = False
        while (not lengthFound):
            if T[i][j + 1] != "+":
                hLength += 1
                j += 1
            else:
                lengthFound = True
        return hLength

    def GetVerticalLength(i,j):
        vLength = 1
        lengthFound = False
        while (not lengthFound):
            if T[i + 1][j] != "+":
                vLength += 1
                i += 1
            else:
                lengthFound = True
        return vLength

    def AddWord(i,j, wordLength, isHorizontal, isVertical):
        crossLetters = []
        k = 0
        while (k <= wordLength-1):
            if T[i][j] != "-":
                crossLetters.append({T[i][j],k})
        
        for word in wordTracker:
            if word.wordLength == wordLength:
                if k == 0:
                    for letter in word:
                        if isHorizontal:
                            T[i][j] = letter
                            j += 1
                            
                        if isVertical:
                            T[i][j] = letter
                            i += 1
                else:
                    wordFit = False
                    for l in range( len(crossLetters)):
                        if word[l[1]] == l[0]:
                            continue;
                        else:
                            break;
                        
                        
                    
        return True    


    
    T = inputGraph
    wordTracker = []
    for word in words:
        w = Word(word)
        wordTracker.append(w)
                
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            if T[i][j] != "+":
                isHWordAdded = False
                isVWordAdded = False
                hLength = GetHorizontalLength(i,j)
                vLength = GetVerticalLength(i,j)
                if hLength > 1:
                   isHWordAdded = AddWord(i,j,hLength,True,False)
                if vLength > 1:
                   isVWordAdded = AddWord(i,j,vLength,False,True) 
       



class Word:
    
    id_iter = itertools.count()
    
    def ___init___(self, word):
        self.id = next(Word.id_iter)
        self.word = word
        self.wordLength = len(word)
        self.startCoordX = 0
        self.startCoordY = 0
        self.isHorizontal = True
        self.crosswords = []


if __name__ == "__main__":
    main()