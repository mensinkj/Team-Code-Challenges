
def main():
    sizes1 = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    sizes2 = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
    
    word1 = "abc"
    word2 = "zaba"
    
    print(getRectangleSize(word1, sizes1))
    print(getRectangleSize(word2, sizes2))
    
    
def getRectangleSize(word, sizes):
    
    maxHeight = 0
    nums = wordToNums(word)
       
    for num in nums:
        if sizes[num] > maxHeight:
            maxHeight = sizes[num]
    
    return (maxHeight*len(nums))
    
def wordToNums(word):
    nums = []
    for letter in word:
        nums.append(ord(letter)-97)
    
    return nums

if __name__ == "__main__":
    main()
