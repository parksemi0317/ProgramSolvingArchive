def solution(name):
    N = len(name)
    print("N :", N)
    
    up_down = 0
    for i, c in enumerate(name):
        if c != "A":
            up_down += min(ord(c)-65, 90-ord(c)+1)
    print("up_down : ", up_down)
    if up_down == 0:
        return 0
        
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
    left_right = N -1
    for s,e in a_sets:
        r_l = (s-1 if s > 0 else 0) * 2 + ((N-1) - e)
        l_r = ((N-1) - e) * 2 + (s-1 if s > 0 else 0) 
        left_right = min(left_right, l_r, r_l)
        print(f"s:{s}, e:{e} => r_l:{r_l}, l_r:{l_r}")
    print("left_right :",left_right)                  
    return up_down + left_right