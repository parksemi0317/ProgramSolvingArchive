import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

ns = list(map(int, input().rstrip().split()))

dp = [[ns[i], ns[i]] for i in range(3)] # [min, max]
# print(F"[DEBUG] dp : {dp}\n\n")


for _ in range(N-1):
    n1, n2, n3 = map(int, input().rstrip().split())
    new_dp = [[0 , 0] for _ in range(3)]
    new_dp[0] = [min(dp[0][0], dp[1][0]) + n1, max(dp[0][1], dp[1][1]) + n1]
    new_dp[1] = [min(dp[0][0],dp[1][0], dp[2][0]) + n2, max(dp[0][1], dp[1][1], dp[2][1]) + n2]
    new_dp[2] = [min(dp[1][0], dp[2][0]) + n3, max(dp[1][1], dp[2][1]) + n3]
    dp = new_dp
    
    # print(F"[DEBUG] n1, n2, n3 : {n1}, {n2}, {n3}\n")
    # print(F"[DEBUG] dp : {dp}\n\n")

print(f"{max(dp[0][1], dp[1][1], dp[2][1])} {min(dp[0][0], dp[1][0], dp[2][0])}")