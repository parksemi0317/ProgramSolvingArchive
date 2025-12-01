import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arrN = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
arrM = list(map(int, input().rstrip().split()))
result = []
def getMaxArr(max, idx1, idx2):
    global arrN, arrM, N, M, result
    if N <= idx1 or M <= idx2:
        return ""
    
    for num in range(max, -1, -1):
        find1 = find2 = -1
        
        for i in range(idx1, N):
            if arrN[i] == num:
                find1 = i
                break
        for i in range(idx2, M):
            if arrM[i] == num:
                find2 = i
                break

        if find1 != -1 and find2 != -1:
            result.append(num)
            getMaxArr(num, find1+1, find2+1)
            return

getMaxArr(100, 0, 0)
print(f"{len(result)}\n")
for c in result:
    print(f"{c} ")