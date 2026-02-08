import sys

input = sys.stdin.readline

# ============= 값 입력 받기 =============

T = int(input().rstrip())

n = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

m = int(input().rstrip())
B = list(map(int, input().rstrip().split()))


# ============= 누적합 구하기 =============
sumA = [0]
for num in A:
    sumA.append(sumA[-1] + num)

sumB = [0]
for num in B:
    sumB.append(sumB[-1] + num)
# print(sumA)
# print(sumB)

# ============= A로 만들 수 있는 부분 수열의 합 구하기 =============

listA = {}
for start in range(n):
    for end in range(start+1, n+1):
        # print(start, end, "=>",sumA[end] - sumA[start])
        num = sumA[end] - sumA[start]
        if num in listA:
            listA[num] += 1
        else:
            listA[num] = 1
# print(listA)


# ============= B로 만들 수 있는 부분 수열의 합 찾기 & 바로 대응되는 A 합 찾기 =============

result = 0
for start in range(m):
    for end in range(start+1, m+1):
        num = sumB[end] - sumB[start]

        aKey = T - num
        if aKey in listA:
            result += listA[aKey]
print(result)
