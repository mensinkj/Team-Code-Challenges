import numpy as np

def main():
    sampleinputArray1 = [4,6,5,3,3,1]
    sampleinputArray2 = [1,2,2,3,1,2]
    print(pickNumberFunction(sampleinputArray1))
    print(pickNumberFunction(sampleinputArray2))
    print(pickNumberFunction(generateRandomArray()))
    

def pickNumberFunction(inputArray):   
    inputArray.sort()
    print(inputArray) 
    answer = 0

    for i in range(0, len(inputArray)):
        for j in range(i+1, len(inputArray)):
            if abs(inputArray[i] - inputArray[j]) <= 1:
                if (j - i + 1) > answer:
                    answer = j - i + 1                  
            else:
                break

    return answer      

def generateRandomArray():
    return np.random.randint(1,25,100)

if __name__ == "__main__":
    main()
