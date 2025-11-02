import sys
import heapq

MAX = 100000

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().rstrip().split())

q = [] # 시간, 현재 위치
is_visited = [0 for _ in range(MAX+1)]


heapq.heappush(q, (0,N))

while 1:
    t, cur = heapq.heappop(q)

    if cur == K:
        print(f"{t}")
        break
        
    if  K != 0 and cur % K == 0:
        temp1 = cur // K
        while temp1  & 1:
            temp1 = temp1 >> 1
        if temp1 == 1:
            print(f"{t}")
            break

    if cur != 0 and K % cur == 0:
        temp2 = K // cur
        while temp2  & 1:
            temp2 = temp2 >> 1
        if temp2 == 1:
            print(f"{t}")
            break
            
    is_visited[cur] = 1
    
    if 2*cur <= MAX and is_visited[2*cur] == 0 :
        heapq.heappush(q, (t, 2*cur))
    if cur + 1 <= MAX and is_visited[cur + 1] == 0:
        heapq.heappush(q, (t+1, cur + 1))
    if cur -1 >= 0 and is_visited[cur-1] == 0:
        heapq.heappush(q, (t+1, cur-1))
    

