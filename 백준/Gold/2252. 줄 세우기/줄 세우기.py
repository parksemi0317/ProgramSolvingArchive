import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N , M = map(int, input().rstrip().split())

leftPrevCnt = [0 for _ in range(N)]
nexts = {}

for i in range(1, N+1):
    nexts[i] = []
    

for _ in range(M):
    A, B = map(int, input().rstrip().split())

    leftPrevCnt[B-1] += 1
    nexts[A].append(B)

q = deque([])

for i in range(N):
    if leftPrevCnt[i] == 0:
        q.append(i+1)

while q:
    cur = q.popleft()

    print(f"{cur} ")

    for p in nexts[cur]:
        leftPrevCnt[p-1] -= 1

        if leftPrevCnt[p-1] == 0:
            q.append(p)
        