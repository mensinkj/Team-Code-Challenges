
def main():
    sampleArray1 = [3,10,2,1,20]
    sampleArray2 = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
    sampleArray3 = [50,3,10,7,40,80]
    print(LongestIncreasingSubsequence(sampleArray1))
    print(LongestIncreasingSubsequence(sampleArray2))
    print(LongestIncreasingSubsequence(sampleArray3))
    

def LongestIncreasingSubsequence(nums):   
    
    answer = []
    for i in range (len(nums)):
        if i == 0:
            answer.insert(i, 1)
        else:
            longestSub = 0
            j = i -1
            while j > -1:
                if nums[j] < nums[i]:                        
                    longestSub = (longestSub, answer[j])[longestSub < answer[j]]
                j -= 1
            
            answer.insert(i, longestSub + 1)

    
    return max(answer) 

if __name__ == "__main__":
    main()
