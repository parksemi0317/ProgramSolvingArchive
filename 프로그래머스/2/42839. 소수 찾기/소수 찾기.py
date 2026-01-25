from itertools import permutations

def isPrime(num):
    if num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    
    numCount = len(numbers)
    result = set([])
    for setLen in range(1, numCount+1):
        sets = permutations(numbers, setLen)
        
        for s in sets:
            if s[0] == "0":
                continue
            num = "".join(s)
            
            if isPrime(int(num)):
                # print(num)
                result.add(num)
                
    return len(set(result))
        