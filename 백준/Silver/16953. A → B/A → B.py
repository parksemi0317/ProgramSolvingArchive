import sys
from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])
result = -1
while q:
    num, cnt = q.popleft()

    if num * 2 == b:
        result = cnt + 1
        break
    elif num * 2 < b:
        q.append((num * 2, cnt+1))
         
        
    if num * 10 + 1 == b:
        result = cnt + 1
        break
    elif num * 10 + 1 < b:
        q.append((num * 10 + 1, cnt + 1))
print(result)