def main():
    n = 166
    c = [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10, 35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28]
    nn = 6
    cc = [1,2,3,4,5]
    print(getWays(n, c))
    print(getWays(nn,cc))

def getWays(n, c):
    # Write your code here
    T = [[0 for x in range(n+1)] for y in range(len(c)+1)]
    T[0][0] = 0
    for i in range(1,len(c)+1):
        for j in range(0,n+1):
            if j == 0:
                T[i][j] = 1
            elif c[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
               T[i][j] = T[i-1][j] + T[i][j-c[i-1]]            
    
    return T[len(c)][n]

if __name__ == '__main__':
    main()