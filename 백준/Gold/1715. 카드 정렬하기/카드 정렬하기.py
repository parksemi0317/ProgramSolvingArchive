import sys
import heapq

N = int(input().rstrip())

q = []
for _ in range(N):
    q.append(int(input().rstrip()))
heapq.heapify(q)

result = 0
while q:
    first = heapq.heappop(q)

    if q:
        second = heapq.heappop(q)
        result += first + second
        heapq.heappush(q, first+ second)
print(f"{result}")