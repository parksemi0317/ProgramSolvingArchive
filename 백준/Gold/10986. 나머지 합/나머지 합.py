import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))
dp = [0]
cnts = [0 for i in range(M)] # 나머지 개수 세기

for i in range(N):
    dp.append((dp[-1] + arr[i])%M)

# print(f"{dp}\n")

result = 0 
for end in range(0, N+1):
    # print(f"[DEBUG] end : {end}, cnts : {cnts}")
    result += cnts[dp[end]-1]
    cnts[dp[end]-1] += 1
    # print(f"=> result : {result}\n")
print(F"{result}")