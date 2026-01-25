from itertools import permutations

def visit(k, p):
    result = 0
    for minK, useK in p:
        if k < minK or k < useK:
            continue
        result += 1
        k -= useK
    return result
        

def solution(k, dungeons):
    plist = permutations(dungeons, len(dungeons))
    
    maxCnt = 0
    
    for p in plist:
        maxCnt = max(maxCnt , visit(k, p))
    return maxCnt