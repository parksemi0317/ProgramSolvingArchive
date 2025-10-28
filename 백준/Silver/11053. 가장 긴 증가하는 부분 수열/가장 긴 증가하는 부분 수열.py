import sys

input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))

# print("[Debug arr : ", arr)

dp = [1 for _ in range(N)] # 특정 위치까지의 최장 증가 수열 (마지막값 포함)


for i in range(1, N):
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
# print("[Debug] dp : ", dp)
print(max(dp))
