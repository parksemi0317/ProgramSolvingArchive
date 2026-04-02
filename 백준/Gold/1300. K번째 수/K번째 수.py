import sys

print = sys.stdout.write

N = int(input())
K = int(input())

# ============= 디버깅용

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         print(F"{i*j}".rjust(4))
#     print("\n")
    
# ============= 특정 숫자보다 작은 수의 개수 찾기

def getSmallNumCnt(N, num):
    result = 0
    for i in range(1, N+1): # i : 가로 num
        result += min(N, num // i)
    # print(F"[DEBUG] getSmallNumCnt({num}) : {result}\n")
    return result

# ============= 이분탐색
MIN = 1
MAX = N**2

while MIN < MAX:
    mid = (MIN + MAX) // 2

    if getSmallNumCnt(N, mid) < K:
        MIN = mid + 1
    else:
        MAX = mid
print(F"{MIN}")
