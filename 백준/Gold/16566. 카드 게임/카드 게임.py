import sys
from bisect import bisect_right

input = sys.stdin.readline
print = sys.stdout.write

N, M, K = map(int, input().rstrip().split())

cards = list(map(int, input().rstrip().split()))
cards.sort()
turns = list(map(int, input().rstrip().split()))
isUsed = [False for _ in range(M)]

for t in turns:
    idx = bisect_right(cards, t)
    while t == cards[idx] or isUsed[idx]:
        idx += 1
    print(F"{cards[idx]}\n")
    isUsed[idx] = True