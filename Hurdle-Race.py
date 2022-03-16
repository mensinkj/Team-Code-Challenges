
def main():
    sampleHurdles1 = [1,6,3,5,2]
    sampleHurdles2 = [2,5,4,5,2]
    sampleHeight1 = 4
    sampleHeight2 = 7
    print(hurdleRaceCalc(sampleHeight1, sampleHurdles1))
    print(hurdleRaceCalc(sampleHeight2, sampleHurdles2))
    

def hurdleRaceCalc(height, hurdles):   
    
    return (max(hurdles) - height, 0)[max(hurdles) - height <= 0]   

if __name__ == "__main__":
    main()
