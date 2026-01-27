import sys
ALL = (0b1 << 10) -1
MOD = 10**9;
# 3차원 DB 풀이
N = int(input())

# [N][10][ALL]
# [길이-1][마지막 수][비트마스크]
dp =[[[0 for _ in range(ALL + 1)] for _ in range(10)] for i in range(N)]

# 길이 1인 경우들 1로 채우기
for startNum in range(1, 10):
    dp[0][startNum][0b1 << startNum] = 1

for prevLenIdx in range(N-1):
    for lastNum in range(10):
        for bitMask in range(ALL+1):
            
            if lastNum > 0:
                newBitMask =  bitMask | (0b1 << (lastNum -1))
                dp[prevLenIdx+1][lastNum-1][newBitMask] += dp[prevLenIdx][lastNum][bitMask]
                dp[prevLenIdx+1][lastNum-1][newBitMask] %= MOD
            if lastNum < 9:
                newBitMask =  bitMask | (0b1 << (lastNum +1))
                dp[prevLenIdx+1][lastNum+1][newBitMask] += dp[prevLenIdx][lastNum][bitMask]
                dp[prevLenIdx+1][lastNum+1][newBitMask] %= MOD

result = 0
for lastNum in range(10):
    result += dp[N-1][lastNum][ALL]
print(f"{result % MOD}")
    