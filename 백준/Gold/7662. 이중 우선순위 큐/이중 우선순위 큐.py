import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

num_cnt_map = {}
min_queue = []
max_queue = []
q_len = 0

def pop_min():
    global min_queue, num_cnt_map, q_len
    
    while 1:
        min = heapq.heappop(min_queue)
        if num_cnt_map[min] > 0:
            num_cnt_map[min] -= 1
            q_len -= 1
            return min

def pop_max():
    global max_queue, num_cnt_map, q_len
    
    while 1:
        max = -heapq.heappop(max_queue)
        if num_cnt_map[max] > 0:
            num_cnt_map[max] -= 1
            q_len -= 1
            return max
        
for _ in range(T):
    # print("\n\n============== [Debug] 새로운 테스트 케이스 시작 ==============\n")
    
    num_cnt_map = {}
    min_queue = []
    max_queue = []
    q_len = 0
    
    k = int(input().rstrip())

    for _ in range(k):
        opt, n = input().rstrip().split()
        # print(f"\n[Debug] opt : {opt}, n : {n}\n")

        if opt == "I":
            n = int(n)
            heapq.heappush(min_queue, n)
            heapq.heappush(max_queue, -n)

            # print(f"[Debug] min_queue : {min_queue}, max_queue : {max_queue}\n")
            
            if n in num_cnt_map:
                num_cnt_map[n] += 1
            else:
                num_cnt_map[n] = 1
            q_len += 1
        elif q_len > 0:
            
            if n == "1":
                # 최댓값 삭제
                pop_max()
                
            else:
                # 최솟값 삭제
                pop_min()
        # print(f"[Debug] num_cnt_map : {num_cnt_map}, q_len : {q_len}\n")

    if q_len == 0:
        print("EMPTY\n")
    else:
        min = max = pop_min()
        
        if q_len != 0:
            max = pop_max()
            
        print(f"{max} {min}\n")
        
            