
from numpy import number


def main():
    wordlist = [5,"ab","bb","hefg","dhck","dkhc"]
    for word in wordlist:
        BiggerIsBetter(word)
    
    

def BiggerIsBetter(word):   
    
    if isinstance(word,int):
        return None
    else:
        letters = Convert(word)
        for i in reversed(range(len(letters))) :
            for j in reversed(range(len(letters)-1)):
                if ord(letters[i]) > ord(letters[j]):
                    letters[i], letters[j] = letters[j], letters[i]
                    return print(''.join(letters))
    
    return print('No Answer')
 
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

if __name__ == "__main__":
    main()
