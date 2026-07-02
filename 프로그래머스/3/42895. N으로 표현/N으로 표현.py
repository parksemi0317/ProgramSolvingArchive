from collections import deque
import math

def addNum(num, cnt, possible, rev_map):
        if num in rev_map:
            return
        rev_map[num] = cnt
        possible[cnt].append(num)
        
def solution(N, number):
    possible = [[] for _ in range(9)]
    rev_map = {}
    
    
    tmp = N
    for cnt in range(1, 9):
        possible[cnt].append(tmp)
        rev_map[tmp] = cnt
        
        tmp = tmp * 10 + N
        
        for leftCnt in range(1, cnt): # 뺄셈, 나눗셈
            rightCnt = cnt - leftCnt
            
            for leftNum in possible[leftCnt]:
                for rightNum in possible[rightCnt]:
                    addNum(leftNum - rightNum, cnt, possible, rev_map)
                    if rightNum != 0:
                        addNum(leftNum // rightNum, cnt, possible, rev_map)
        for leftCnt in range(1, cnt // 2 + 1): # 덧셈, 곱셈
            rightCnt = cnt - leftCnt 
            for leftNum in possible[leftCnt]:
                for rightNum in possible[rightCnt]:
                    addNum(leftNum + rightNum, cnt, possible, rev_map)
                    addNum(leftNum * rightNum, cnt, possible, rev_map)
    if number in rev_map:
        return rev_map[number]
    return -1
    
    
    
    
    
    