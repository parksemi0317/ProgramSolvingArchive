import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

heap = []

for _ in range(N):
    num = int(input().rstrip())

    if num == 0:
        if len(heap) == 0:
            print("0\n")
        else:
            print(f"{heapq.heappop(heap)}\n")
    else:
        heapq.heappush(heap, num)