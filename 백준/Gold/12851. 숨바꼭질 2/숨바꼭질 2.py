from collections import deque

N, K = map(int, input().split())

def solution():

    q = deque([(N, 0)])
    isVisited = {}

    minTime = -1
    while minTime == -1 and q:
        position, time = q.popleft()

        if 0 <= position -1 and (not position-1 in isVisited or isVisited[position-1] == time+1):
            if position-1 == K:
                minTime = time+1
            q.append((position-1, time+1))
            isVisited[position-1] = time + 1

        if position+1 <= 100000 and (not position+1 in isVisited or isVisited[position+1] == time+1):
            if position+1 == K:
                minTime = time+1
            q.append((position+1, time+1))
            isVisited[position+1] = time + 1

        if position*2 <= 100000 and (not position*2 in isVisited or isVisited[position*2] == time+1):
            if position*2 == K:
                minTime = time+1
            q.append((position*2, time+1))
            isVisited[position*2] = time + 1
    print(F"{minTime}")

    sameCnt = 1
    position, time = q.popleft()
    while time == minTime-1:

        if position -1 == K:
            sameCnt += 1

        if position+1==K:
            sameCnt += 1

        if position*2==K:
            sameCnt += 1
        position, time = q.popleft()
    print(sameCnt)
        
if N==K:
    print("0\n1")
else:
    solution()
        
