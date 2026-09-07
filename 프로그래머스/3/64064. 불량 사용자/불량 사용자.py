def isPossible(user, ban):
    if len(ban) != len(user):
        return False
    
            
    l = len(ban)
    for i in range(l):
        if ban[i] != "*" and ban[i] != user[i]:
            return False
    return True

def getSetCode(is_used):
    result = ""
    for tf in is_used:
        result += "1" if tf else "0"
    return result

def dfs(is_used, possible_user_idx, cur_ban_idx, ban_cnt, result):
    # print(f"[DEBUG] dfs({is_used}, {cur_ban_idx})")
    if cur_ban_idx == ban_cnt:
        result.add(getSetCode(is_used))
        return 
    
    users = possible_user_idx[cur_ban_idx]
    if len(users) == 1:
        dfs(is_used, possible_user_idx, cur_ban_idx+1, ban_cnt, result)
        return
    
    for user in users:
        if not is_used[user]:
            is_used[user] = True
            dfs(is_used, possible_user_idx, cur_ban_idx+1, ban_cnt, result)
            is_used[user] = False
            
def solution(user_id, banned_id):
    is_used = [False for _ in user_id]
    possible_user_idx = [[] for _ in banned_id]
    
    for ban_idx, ban in enumerate(banned_id):
        cnt = 0
        for user_idx, user in enumerate(user_id):
            
            if(isPossible(user, ban)): 
                possible_user_idx[ban_idx].append(user_idx)
                cnt += 1
        
        if cnt == 0:
            print(f"[DEBUG] ban {ban}에 부합하는 사용자가 없음")
            return 0
        
        elif cnt == 1:
            user = possible_user_idx[ban_idx][0]
            if is_used[user]:
                # print(f"[DEBUG] ban {ban}에 부합하는 유일한 사용자가 {user}가 이미 사용됨")
                return 0
            is_used[user] = True
            
    # print("[DEBUG] possible_user_idx :", possible_user_idx)
    
    ban_cnt = len(banned_id)
    result = set([])
    dfs(is_used, possible_user_idx, 0, ban_cnt, result)
    return len(result)
    
    