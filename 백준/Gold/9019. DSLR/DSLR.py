import sys
from collections import deque

input = sys.stdin.readline
# print = sys.stdout.write

T = int(input().rstrip())

for _ in range(T):

    a, b = map(int, input().rstrip().split())
    # print(f"\n======== [DEBUG] a: {a}, b : {b}")
    q = deque([(a, "")])
    is_in = [False for _ in range(10000)]
    is_in[a] = True

    while q:
        
        num, opt = q.popleft()
        # print(f"\n[DEBUG] num : {num}, opt : {opt}")
        
        # D
        new_num = (num * 2) % 10000
        if not is_in[new_num]:
            if new_num == b:
                print(opt + "D")
                break
            else:
                q.append((new_num, opt + "D"))
                is_in[new_num] = True

        # S
        new_num = (num -1) % 10000
        if not is_in[new_num]:
            if new_num == b:
                print(opt + "S")
                break
            else:
                q.append((new_num, opt + "S"))
                is_in[new_num] = True

        # L
        new_num = num//1000 + (num % 1000) * 10
        if not is_in[new_num]:
            # print(f"[DEBUG] {num} L 연산 -> {new_num}")
            if new_num == b:
                print(opt + "L")
                break
            else:
                q.append((new_num, opt+ "L"))
                is_in[new_num] = True
    
        # R
        new_num = num//10 + (num%10) * 1000
        if not is_in[new_num]:
            if new_num == b:
                print(opt + "R")
                break
            else:
                q.append((new_num, opt + "R"))
                is_in[new_num] = True

            
        # print(f"[DEBUG] {q}")
    