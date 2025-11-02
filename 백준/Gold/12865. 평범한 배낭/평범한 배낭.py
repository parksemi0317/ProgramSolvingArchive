import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().rstrip().split())


max_vals = [0 for i in range(K+1)]

# 물품 입력 받기
for i in range(N):
    w, v = map(int, input().rstrip().split())

    # print(f"[Debug] w, v : {w}, {v}\n")
    prev_arr = max_vals.copy()
    if w <= K:
        max_vals[w] = max(prev_arr[w], v)
        
        for j in range(1, K-w+1):
            if prev_arr[j] != 0:
                max_vals[j+w] = max(prev_arr[j+w], v + prev_arr[j])
        
    # print(f"[Debug] max_vals : {max_vals}\n\n")
    

print(f"{max(max_vals)}")