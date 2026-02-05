import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

cards = list(map(int, input().rstrip().split()))

sortedCards = sorted(cards)
maxNum = sortedCards[-1]
results = {}

for c in cards:
    results[c] = 0

for num in cards:

    iterNum = num * 2
    while iterNum <= maxNum:
        if iterNum in results:
            results[iterNum] -= 1
            results[num] += 1
        iterNum += num

for num in cards:
    print(F"{results[num]} ")