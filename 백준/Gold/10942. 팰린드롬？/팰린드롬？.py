import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [[False for i in range(N)] for i in range(N)]


# 길이가 홀수인 팰린드롬 구하기
for mid in range(N): # 중간 인덱스
    front= mid
    back = mid
    while front >=0 and back < N and arr[front] == arr[back]:
        dp[front][back] = True
        front -= 1
        back += 1
        
# 길이가 짝수인 팰린드롬 구하기
for leftMid in range(N):
    front = leftMid
    back = front + 1

    while front >=0 and back < N and arr[front] == arr[back]:
        dp[front][back] = True
        front -= 1
        back += 1
        
M = int(input().rstrip())
for _ in range(M):
    S, E = arr = map(int, input().rstrip().split())
    print(F"{1 if dp[S-1][E-1] else 0}\n")