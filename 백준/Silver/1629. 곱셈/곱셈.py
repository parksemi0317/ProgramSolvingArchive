import sys

input = sys.stdin.readline
print = sys.stdout.write

A, B, C = map(int, input().rstrip().split())
tmpb = B
cnt = 0
while tmpb > 0:
    tmpb = tmpb >> 1
    cnt+=1
# print(F"[Debug] cnt : {cnt}\n")
    
mul_squares = [-1 for _ in range(cnt+1)] # A를 2**i번 곱한 값
mul_squares[0] = A % C

def divideAndConq(n):
    global mul_squares, C, cnt

    if n<= cnt and mul_squares[n] != -1:
        return mul_squares[n]
    
    result = (divideAndConq(n-1)**2) % C
    mul_squares[n] = result
    # print(f"[Debug] divideAndConq({n}) : -> {result}\n")
    return result


iter = 0
result = 1 
while B > 0:
    if B & 1:
        # print(f"[Debug] {2**iter} -> ")
        result = (result * divideAndConq(iter)) % C
        # print(f"[Debug] result : {result}\n")
    B = B >> 1
    iter += 1

# print(f"[Debug] mul_squares : {mul_squares}\n")
print(f"{result}")
