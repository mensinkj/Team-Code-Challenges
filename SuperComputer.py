import numpy as np

def main():
    input1 = [["G","G","G","G","G","G",],["G","B","B","B","G","B",],["G","G","G","G","G","G",],["G","G","B","B","G","B",],["G","G","G","G","G","G",]]
    input2 = [["B","G","B","B","G","B",],["G","G","G","G","G","G",],["B","G","B","B","G","B",],["G","G","G","G","G","G",],["B","G","B","B","G","B",],["B","G","B","B","G","B",]]
    print(Emmas(input1));
    print(Emmas(input2));
    
    

def Emmas(input):
    T = [[0 for i in range(len(input[0])+2)] for i in range(len(input)+2)]
    answer = []
    
    for i in range(1, len(input)+1):
        for j in range(1, len(input[0])+1):
            if input[i-1][j-1] == "B":
                T[i][j] = 0
            else:
                T[i][j] = 1
                
    for i in range(1, len(input)+1):
        for j in range(1, len(input[0])+1):
                a = 1
                if T[i][j] == 1:
                    if T[i-a][j] == 1 and T[i+a][j] == 1 and T[i][j-a] == 1 and T[i][j+a] == 1:
                        ismaxlength = False
                        T[i][j] = 5
                        T[i-a][j] = 0
                        T[i+a][j] = 0
                        T[i][j-a] = 0 
                        T[i][j+a] = 0
                        while(ismaxlength == False):
                            a += 1
                            if T[i-a][j] == 1 and T[i+a][j] == 1 and T[i][j-a] == 1 and T[i][j+a] == 1:
                                T[i][j] += 4 
                            else:
                                ismaxlength = True
                            
    for i in range(0, len(input)+1):
        for j in range(0, len(input[0])+1):
            if T[i][j] > 0:
                answer.append(T[i][j])                    


    
    return np.prod(answer)

if __name__ == "__main__":
    main()