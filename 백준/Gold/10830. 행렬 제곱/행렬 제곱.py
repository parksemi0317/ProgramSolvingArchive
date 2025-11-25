import sys

input = sys.stdin.readline
print = sys.stdout.write

## ========== 값 입력 빋기 
N, B = map(int, input().rstrip().split())

# print(f"[DEBUG] N : {N}, B : {B}\n")

m = []

for i in range(N):
    m.append(list(map(int, input().rstrip().split())))

## ========== 디버깅용 출력 함수

def printMatrix(m):
    for line in m:
        for i in line:
            print(f"{i} ")
        print("\n")
    print("\n")

# print("[DEBUG] m : \n")
# printMatrix(m)

## ========== 2 ** n 제곱 행렬 구하기


s = []

def calNextSquare():
    global N, s, m

    if len(s) == 0:
        s.append(m)
        return

    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += s[-1][i][k]* s[-1][k][j]

    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000
                
    s.append(result)

to_binary = []
while B > 0:
    # print(f"[DEBUG] B : {B}\n")
    to_binary.append(B & 1)
    calNextSquare()
    B = B >> 1

# print(f"[DEBUG] to_binary : {to_binary}\n")
'''
for idx, m in enumerate(s):
    print(f"[DEBUG] s[{idx}] (m의 {2 ** idx} 제곱))\n")
    printMatrix(m)
'''
## ========== 

result = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

def mulMatrix(m):
    global result, N

    new_result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_result[i][j] += result[i][k]* m[k][j]

    for i in range(N):
        for j in range(N):
            new_result[i][j] %= 1000
            
    result = new_result
                
    

for idx, i in enumerate(to_binary):
    if i:
        # print(f"[DEBUG] {2 ** idx} 곱하기\n")
        mulMatrix(s[idx])   
        # printMatrix(result)
printMatrix(result)
