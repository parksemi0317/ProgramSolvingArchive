def solution(name):
    N = len(name)
    print("N :", N)
    # ========== 알파벳 바꾸는 횟수 구하기
    up_down = 0
    for i, c in enumerate(name):
        if c != "A":
            up_down += min(ord(c)-65, 90-ord(c)+1)
            
    if up_down == 0: # 바꿀 알파벳이 없는 경우
        return 0
    
    # ========== 연속된 A 조합 구하기
    a_sets = []
    start_i = -1
    for i in range(N):
        if name[i] == "A":
            if start_i == -1:
                start_i = i
        else:
            if start_i != -1:
                a_sets.append((start_i, i-1))
                start_i = -1

    if start_i != -1:
        a_sets.append((start_i, N-1))
    
    print("a_sets :", a_sets)
    
    # ========== 연속된 A에 대하여 해당 구역 안지나가는 경우 고려하기
    
    left_right = N -1 # 오른쪽으로 쭉 이동하는 경우
    
    for s,e in a_sets:
        r_l = (s-1 if s > 0 else 0) * 2 + ((N-1) - e) # 오른쪽으로 갔다가 왼쪽으로 돌아가는 경우
        l_r = ((N-1) - e) * 2 + (s-1 if s > 0 else 0) # 왼쪽으로 갔다가 오른쪽으로 돌아오는 경우
        left_right = min(left_right, l_r, r_l)
        print(f"s:{s}, e:{e} => r_l:{r_l}, l_r:{l_r}")
    print("left_right :",left_right)                  
    return up_down + left_right