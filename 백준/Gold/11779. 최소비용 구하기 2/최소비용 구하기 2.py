import sys
import heapq
INF = 100000 * 100000

input = sys.stdin.readline
print = sys.stdout.write

## =============== 값 입력 받기
n = int(input().rstrip())
m = int(input().rstrip())

bus = {}

for s in range(1, n+1):
    bus[s] = []

for _ in range(m):
    s, e, c = map(int, input().rstrip().split())

    bus[s].append((e, c))

start, end = map(int, input().rstrip().split())

## =============== 다익스트라

dp = [[INF, []] for _ in range(n)]
dp[start-1] = [0, [start]]

q = [(0, start)]
visited = [False for _ in range(n)]

cnt = 0
while q: 
    if cnt >= n:
        break
    cost, mid = heapq.heappop(q)
    # print(f"\n=== [DEBUG] cost : {cost}, mid : {mid}\n")

    if visited[mid-1]:
        continue
        
    for to, cost in bus[mid]:
        # print(f"[DEBUG] cost : {cost}, to : {to}\n")
        if not visited[mid-1] and dp[to-1][0] > dp[mid-1][0] + cost:
            dp[to-1] = [dp[mid-1][0] + cost, dp[mid-1][1] + [to]]
            heapq.heappush(q, (dp[to-1][0], to))
    # print(f"[DEBUG] dp : {dp}\n")
            
    visited[mid-1] = True

    cnt += 1

## =============== 결과 출력

print(f"{dp[end-1][0]}\n")
print(f"{len(dp[end-1][1])}\n")

for v in dp[end-1][1]:
    print(f"{v} ")
    
    