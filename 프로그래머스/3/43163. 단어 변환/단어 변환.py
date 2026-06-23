from collections import deque

def canChange(curStr, nextStr, n):
    flag = False
    for i in range(n):
        if curStr[i] != nextStr[i]:
            if flag:
                return False
            else:
                flag = True
    return flag
        

def solution(begin, target, words):
    n = len(begin) # 문자열 길이
    wLen = len(words)
    
    q = deque([(begin, 0)])
    visit = [False for _ in range(wLen)]
    while q:
        cur, cnt = q.popleft()
        print(cur, cnt)
        
        if cur == target:
            return cnt
        
        for wIdx in range(wLen):
            if not visit[wIdx] and canChange(cur, words[wIdx], n):
                q.append([words[wIdx], cnt + 1])
                visit[wIdx] = True
    return 0