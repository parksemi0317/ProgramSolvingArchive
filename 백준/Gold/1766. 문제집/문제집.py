import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

prevs = {}
nexts = {}

N, M = map(int, input().rstrip().split())

for i in range(1, N+1):
    prevs[i] = []
    nexts[i] = []

for _ in range(M):
    A, B = map(int, input().rstrip().split())

    prevs[B].append(A)
    nexts[A].append(B)

# =============== 선행 문제가 없는 문제들 찾기 ===============
hq = []

for i in range(1, N+1):
    if len(prevs[i]) == 0:
        heapq.heappush(hq, i)

# print(f"{hq}")

# =============== 선행 문제가 없는 문제들 찾기 ===============
while hq:

    n = heapq.heappop(hq)
    print(f"{n} ")

    for next in nexts[n]:
        prevs[next].remove(n)

        if len(prevs[next]) == 0:
            heapq.heappush(hq, next)