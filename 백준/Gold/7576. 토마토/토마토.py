import sys

input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().rstrip().split())

arr =[]

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

'''
# 디버깅용 함수
def printArrForDebug():
    global arr, N
    for line in arr:
        print(f"{line}\n")

printArrForDebug()
'''

job_queue = [] # (x좌표, y 좌표, 익는데 걸린 시간)
job_len = 0
job_idx = 0

for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            job_queue.append((x, y, 1))
            job_len += 1
            

while job_idx <= job_len-1:
    (x, y , cnt) = job_queue[job_idx]
    job_idx += 1

    # print(f"[Debug] x : {x}, y : {y}, cnt : {cnt}\n")

    # 상단
    if x > 0 and arr[x-1][y] == 0:
        arr[x-1][y] = cnt + 1
        job_queue.append((x-1, y, cnt + 1))
        job_len += 1
    # 하단
    if x < N-1 and arr[x+1][y] == 0:
        arr[x+1][y] = cnt + 1
        job_queue.append((x+1, y, cnt + 1))
        job_len += 1
    # 좌측
    if y > 0 and arr[x][y-1] == 0:
        arr[x][y-1] = cnt + 1
        job_queue.append((x, y-1, cnt + 1))
        job_len += 1
    # 우측
    if y < M-1 and arr[x][y+1] == 0:
        arr[x][y+1] = cnt + 1
        job_queue.append((x, y+1, cnt + 1))
        job_len += 1


# 정답 출력 함수 (익지 않은 토마토 발견 시 바로 return 하기 위함)
def printResult():
    global arr

    maxCnt = 0
    
    for line in arr:
        for c in line:
            # 익지 않은 토마토가 존재하는 경우
            if c == 0:
                print("-1")
                return 
            elif c > maxCnt:
                maxCnt = c

    print(f"{maxCnt -1}")
            

printResult()