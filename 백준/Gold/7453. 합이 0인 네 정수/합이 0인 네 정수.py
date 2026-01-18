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


# ============= 딕셔너리 두개씩 합치기 =============
def mergeList(p, q):
    r = []

    for num1 in p:
        for num2 in q:
            r.append(num1 + num2)
    return r

AB = mergeList(A, B)
CD = mergeList(C, D)

# ============= 전체합 구하기 =============

AB.sort()
CD.sort()
lenAB = len(AB)
lenCD = len(CD)

result = 0
idx1 = 0
idx2 = lenCD-1


while  idx1 < lenAB and idx2 >= 0:
    # print(f"[DEBUG] idx1 : {idx1}, idx2 : {idx2}\n")
    if AB[idx1] + CD[idx2] == 0:
        prevIdx1 = idx1
        while idx1 <lenAB and AB[idx1] == AB[prevIdx1]:
            idx1 += 1

        prevIdx2 = idx2
        while idx2 >= 0 and CD[idx2] == CD[prevIdx2]:
            idx2 -= 1
            
        result += (idx1 - prevIdx1) * (prevIdx2 - idx2)

        
    elif AB[idx1] + CD[idx2] > 0:
        idx2 -= 1
    else:
        idx1 += 1
print(F"{result}")