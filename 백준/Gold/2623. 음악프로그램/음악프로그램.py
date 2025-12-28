import sys
from collections import deque


input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

nextVertex = {}
prevVertex = {}

for i in range(1, N+1):
    nextVertex[i] = []
    prevVertex[i] = []


for _ in range(M):
    arr = list(map(int, input().rstrip().split()))

    for i in range(1, arr[0]):
        nextVertex[arr[i]].append(arr[i+1])
        prevVertex[arr[i+1]].append(arr[i])
'''
for i in range(1, N+1):
    print(f"nextVertex[{i}] : {nextVertex[i]}\n")
print("\n")

for i in range(1, N+1):
    print(f"prevVertex[{i}] : {prevVertex[i]}\n")
'''

q = deque([])

for i in range(1, N+1):
    if len(prevVertex[i]) == 0:
        q.append(i)
result = []
while q:
    now = q.popleft()
    result.append(now)

    for next in nextVertex[now]:
        prevVertex[next].remove(now)

        if len(prevVertex[next]) == 0:
            q.append(next)
if len(result) < N:
    print("0")
else:
    for i in result:
        print(f"{i}\n")
