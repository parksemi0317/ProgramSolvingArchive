import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().rstrip().split())
jewels_weight_q = []
bags = []

for _ in range (N):
    M, V = map(int, input().rstrip().split())
    jewels_weight_q.append((M, V))
heapq.heapify(jewels_weight_q)

for _ in range(K):
    C = int(input().rstrip())
    bags.append(C)

bags.sort()
jewels_value_q = []

result = 0
for b in bags:
    # 담을 수 있는 보석들 큐에 삽입
    while jewels_weight_q and jewels_weight_q[0][0] <= b:
        M, V = heapq.heappop(jewels_weight_q)
        heapq.heappush(jewels_value_q, (-V, M))

    # 가장 비싼 보석 담기
    if jewels_value_q:
        V, M = heapq.heappop(jewels_value_q)
        result -= V

print(f"{result}")