import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

V, E = map(int, input().rstrip().split())

edges = {} # edge 저장 list map
for i in range(1, V+1):
    edges[i] = []

canUseV = []

for _ in range(E):
    A, B, C = map(int, input().rstrip().split())
    edges[A].append((B, C))
    edges[B].append((A, C))

# for i in range(1, V+1):
#     print(f"[DEBUG] edges[{i}] : {edges[i]}\n")

isVisisted = [False for _ in range(V)] # mst 포함 여부
isVisisted[0] = True

# print("[DEBUG] 1번째 vertex 방문\n")
for b, c in edges[1]:
    heapq.heappush(canUseV,(c, 1, b))
# print(f"[DEBUG] canUseV : {canUseV}\n")


result = 0
while canUseV:
    c, a, b = heapq.heappop(canUseV)
    
    if not isVisisted[b-1]:
        isVisisted[b-1] = True
        # print(f"[DEBUG] {b}번째 vertex 방문\n")
        result += c
        for b2, c2 in edges[b]:
            heapq.heappush(canUseV,(c2, b, b2))
        
        # print(f"[DEBUG] result : {result}, canUseV : {canUseV}\n")

print(f"{result}")
        