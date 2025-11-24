import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
# print(F"[DEBUG] arr : {arr}\n")

# ========== 증가 수열 구하기

asc = [1 for _ in range(N)] # 자신을 포함하는 최대 증가 부분 수열

for cur in range(1, N):
    # print(F"[DEBUG] arr[{cur}] : {arr[cur]}\n")

    for i in range(cur-1, -1, -1):
        if arr[i] < arr[cur]:
            asc[cur] = max(asc[cur], asc[i] + 1)

# print(F"[DEBUG] asc : {asc}\n")

# ========== 감소 수열 구하기

disc = [1 for _ in range(N)] # 자신을 포함하는 최대 감소 부분 수열

for cur in range(N-2, -1, -1):
    # print(F"[DEBUG] arr[{cur}] : {arr[cur]}\n")

    for i in range(cur+1, N):
        if arr[cur] > arr[i]:
            disc[cur] = max(disc[cur], disc[i] + 1)

# print(F"[DEBUG] dis : {disc}\n")

# ========== 최대 합 구하기
result = 0

for i in range(N):
    result = max(result, asc[i] + disc[i] -1)
print(f"{result}")
        