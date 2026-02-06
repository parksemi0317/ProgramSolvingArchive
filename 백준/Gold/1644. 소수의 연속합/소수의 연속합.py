import sys
import math

N = int(input())


# ============= N 이하의 소수 찾기 =============

isPrime = [True for _ in range(N+1)]
for num in range(2, int(math.sqrt(N)) + 1):
    if isPrime[num]:
        mulNum = num * 2
        while mulNum <= N:
            isPrime[mulNum] = False
            mulNum += num

# ============= 누적합 구하기 =============

sumPrimes = [0]
sumPrimesLen = 1

for num in range(2, N+1):
    if isPrime[num]:
        # print(f"{num}".ljust(3), end=" ")
        sumPrimes.append(sumPrimes[-1] + num)
        sumPrimesLen += 1
# print()

# for num in sumPrimes:
#     print(f"{num}".ljust(3), end=" ")
# print()

# ============= 투포인터로 합이 N인 경우의 수 찾기 =============

startIdx = 0
endIdx = 1

count = 0
while endIdx < sumPrimesLen and startIdx < sumPrimesLen:
    currentNum = sumPrimes[endIdx] - sumPrimes[startIdx]
    # print("startIdx :" , startIdx,  "endIdx :", endIdx  , "=>", currentNum)
    if currentNum == N:
        count += 1
        startIdx += 1
    elif currentNum < N:
        endIdx += 1
    elif currentNum > N:
        startIdx += 1
print(count)