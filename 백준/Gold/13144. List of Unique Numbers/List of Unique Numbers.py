n = int(input())
arr = list(map(int, input().split()))
last_seen = {}

result = 0
cur_s_idx = 0
for i, a in enumerate(arr):
    if a not in last_seen:
        last_seen[a] = i
    else:
        if last_seen[a] < cur_s_idx: # 범위 밖인 경우
            last_seen[a] = i
        else:
            cur_s_idx = last_seen[a] + 1
            last_seen[a] = i
    result += i-cur_s_idx+1
    # print(f"[DEBUG] {a} : +{i-cur_s_idx+1} -> {result}")

print(result)