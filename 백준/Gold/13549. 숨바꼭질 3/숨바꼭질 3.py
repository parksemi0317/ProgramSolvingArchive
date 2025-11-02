import sys
import heapq

MAX = 100000

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().rstrip().split())

q = [] # (시간, 현재 위치) 꼴의 우선순위 큐
is_visited = [0 for _ in range(MAX+1)]

# 시작 지점 우선 순위 큐에 삽입
heapq.heappush(q, (0,N))

while 1:
    t, cur = heapq.heappop(q)

    # 목적지에 도달한 경우
    if cur == K:
        print(f"{t}")
        break

    # 목적지에 순간 이동으로 접근 가능한 경우 처리
    if cur != 0 and K % cur == 0:
        temp = K // cur
        while temp  & 1:
            temp = temp >> 1
        if temp == 1:
            print(f"{t}")
            break
            
    is_visited[cur] = 1
    
    # 이동 가능 지점 우선 순위 큐에 삽입
    if 2*cur <= MAX and is_visited[2*cur] == 0 :
        heapq.heappush(q, (t, 2*cur))
    if cur + 1 <= MAX and is_visited[cur + 1] == 0:
        heapq.heappush(q, (t+1, cur + 1))
    if cur -1 >= 0 and is_visited[cur-1] == 0:
        heapq.heappush(q, (t+1, cur-1))
    

