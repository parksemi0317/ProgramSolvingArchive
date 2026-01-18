import sys
import bisect

input = sys.stdin.readline
print = sys.stdout.write

# ============= 입력 받기 =============
N = int(input().rstrip())

A = [0 for _ in range(N)]
B = [0 for _ in range(N)]
C = [0 for _ in range(N)]
D = [0 for _ in range(N)]

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().rstrip().split())

# ============= 딕셔너리로 변환 =============
def convertToDict(arr):
    result = {}

    for n in arr:
        if n in result:
            result[n] += 1
        else:
            result[n] = 1
    return result

A = convertToDict(A)
B = convertToDict(B)
C = convertToDict(C)
D = convertToDict(D)

# ============= 딕셔너리 AB 합치기 =============

AB = {}
for num1 in A:
    for num2 in B:
        if num1 + num2 in AB:
            AB[num1 + num2] += A[num1] * B[num2]
        else:
            AB[num1 + num2] = A[num1] * B[num2]

# ============= 전체합 구하기 =============
result = 0

for num1 in C:
    for num2 in D:
        if -(num1 + num2) in AB:
            result += AB[-(num1 + num2)] * C[num1] * D[num2]

print(f"{result}")