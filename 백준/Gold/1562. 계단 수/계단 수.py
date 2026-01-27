import sys
DIV = 1000000000
ALL = (0b1 << 10) -1

N = int(input())

dp = {}

def dfs(leftLen, bitMask, lastNum):
    global N
    
    key = str(lastNum) + " " + str(leftLen) + " " + str(bitMask)
    if key in dp:
        return dp[key]

    if leftLen == 0:
        if bitMask == ALL:
            return 1
        else:
            return 0
    
    result = 0
    if lastNum > 0:
        tempBitMask = 0b1 << (lastNum-1)
        result += dfs(leftLen-1, bitMask | tempBitMask , lastNum-1)
    if lastNum < 9:
        tempBitMask = 0b1 << (lastNum+1)
        result += dfs(leftLen-1, bitMask | tempBitMask , lastNum+1)
    dp[key] = result % DIV
    return result % DIV
    
result = 0
for startNum in range(1, 10):
    result += dfs(N-1, 0b1 << startNum ,startNum)
print(f"{result % DIV}")
