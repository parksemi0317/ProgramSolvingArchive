import sys

input = sys.stdin.readline
print = sys.stdout.write

str1 = input().rstrip()
str2 = input().rstrip()

len1 = len(str1)
len2 = len(str2)

dp = [[[0, ""] for _ in range(len1+1)] for _ in range(len2+1)]

for j in range(len1):
    for i in range(len2):

        if dp[i][j+1][0] > dp[i+1][j][0]:
            dp[i+1][j+1] = [dp[i][j+1][0], dp[i][j+1][1]]
        else:
            dp[i+1][j+1] = [dp[i+1][j][0], dp[i+1][j][1]]
            
        if str1[j] == str2[i] and dp[i+1][j+1][0] < dp[i][j][0] + 1: 
            dp[i+1][j+1] = [dp[i][j][0] + 1, dp[i][j][1] + str1[j]]
'''
for line in dp:
    for item in line:
        print(f"[{item[0]}".rjust(3))
        print(f"{item[1]}] ".rjust(8))
    print("\n")
'''

print(f"{dp[len2][len1][0]}\n")
print(f"{dp[len2][len1][1]}")