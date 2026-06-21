def dfs(curNum, curIdx, numbers, target, n):
    if curIdx == n:
        if curNum == target:
            return 1
        return 0
    return dfs(curNum+numbers[curIdx], curIdx+1, numbers, target, n) + dfs(curNum-numbers[curIdx], curIdx+1, numbers, target, n)
    

def solution(numbers, target):
    return dfs(0, 0, numbers, target, len(numbers))