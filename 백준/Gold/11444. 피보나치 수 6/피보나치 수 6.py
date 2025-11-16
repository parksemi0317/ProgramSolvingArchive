import sys
DIV = 1000000007

n = int(input())

dp = {0 : 0, 1 : 1}

def fibo(n):
    global dp
    if n in dp:
        return dp[n]

    if n % 2 == 0:
        f1 = fibo(n//2)
        f2 = fibo(n//2 -1)
        dp[n] = (f1 * ( f1 + 2 * f2)) % DIV
        return dp[n]
    else:
        f1 = fibo(n//2)
        f2 = fibo(n//2 + 1)
        dp[n] = (f1 ** 2 + f2 ** 2) % DIV
        return dp[n]

print(fibo(n))