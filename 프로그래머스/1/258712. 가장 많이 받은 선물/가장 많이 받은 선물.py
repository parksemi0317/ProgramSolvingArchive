def solution(friends, gifts):
    friend_map = {}
    f_cnt = len(friends)
    for i, f in enumerate(friends):
        friend_map[f] = i
    
    give_cnt = [[0 for _ in range(f_cnt)] for _ in range(f_cnt)]
    gift_num = [0] * f_cnt
    for g in gifts:
        give, get = g.split()
        
        giveIdx = friend_map[give]
        getIdx = friend_map[get]
        
        give_cnt[giveIdx][getIdx] += 1
        gift_num[giveIdx] += 1
        gift_num[getIdx] -= 1
    
    next_get_cnt = [0] * f_cnt
    for i in range(f_cnt):
        for j in range(i+1, f_cnt):
            if give_cnt[i][j] > give_cnt[j][i]:
                # i가 j한테 더 많이 준 경우
                next_get_cnt[i] += 1
            elif give_cnt[i][j] < give_cnt[j][i]:
                # j가 i한테 더 많이 준 경우
                next_get_cnt[j] += 1
            elif gift_num[i] > gift_num[j]:
                next_get_cnt[i] += 1
            elif gift_num[i] < gift_num[j]:
                next_get_cnt[j] += 1
    return max(next_get_cnt)
                
        