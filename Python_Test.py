#Assignment 1: SimpleAlgorithm

def find_two_sum(numbers,targetsum):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            result=int(numbers[i])+int(numbers[j])
            if result==targetsum:
                print(i,j)
    
find_two_sum([3, 1, 5, 7, 5, 9], 10)
