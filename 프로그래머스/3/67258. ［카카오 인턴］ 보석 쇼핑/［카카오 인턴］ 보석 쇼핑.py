def solution(gems):
    # === STEP 1 : gems 가공
    gems_len = len(gems)
    
    # gem 종류 및 id 구하기
    gem_sets = set(gems)
    gem_set_len = len(gem_sets)
    
    gem_id_map = {}
    for idx, gem in enumerate(gem_sets):
        gem_id_map[gem] = idx
        
    # print("[DEBUG] gem_id_map :", gem_id_map)
    
    # === STEP 2 : slide window식 풀이
    gems_cnt = [0 for _ in range(gem_set_len)] # 현재 window 내 각 gem의 수
    
    cur_start = 0 # window 시작 idx
    cur_showed = 0 # 현재 window내 gem 종류 수
    min_len = gems_len # 현재까지 나온 최소 window 길이
    min_result = [1, gems_len] # 현재까지 나온 최소 길이 window 정보
    
    for idx, gem in enumerate(gems):
        cur_gem_id = gem_id_map[gem]
        # print(f"[DEBUG] idx : {idx} (gem : {gem}, id : {cur_gem_id})")
        
        if gems_cnt[cur_gem_id] <= 0:
            cur_showed += 1
            # print(f"\t[DEBUG] {gem} 최초 등장 -> cur_showed : {cur_showed}")
        gems_cnt[cur_gem_id] += 1
        
        # cur_start 줄이기
        while cur_start < idx:
            start_gem = gems[cur_start]
            start_gem_id = gem_id_map[start_gem]
            
            if gems_cnt[start_gem_id] <= 1:
                break
            gems_cnt[start_gem_id] -= 1
            cur_start += 1
        # print(f"\t[DEBUG] cur_start : {cur_start}")
            
        if cur_showed == gem_set_len:
            new_len = idx - cur_start + 1
            if new_len < min_len:
                # print(f"\t[DEBUG] new_len : {new_len}")
                min_len = new_len
                min_result = [cur_start + 1, idx+ 1]
    
    return min_result
# def solution(gems):
#     # gems 가공
#     gem_sets = set(gems)
#     gem_set_len = len(gem_sets)
    
#     gem_idx_map = {}
#     for idx, gem in enumerate(gem_sets):
#         gem_idx_map[gem] = idx
        
#     # print("[DEBUG] gem_idx_map :", gem_idx_map)
    
#     # 앞에서부터 start_idx잡고 해당 시작 지점을 기준으로 하는 최소 구간 구하기
#     gems_cnt = len(gems)
#     min_len = len(gems)
#     min_range = [1, min_len]
    
#     for start_idx in range(gems_cnt - gem_set_len + 1):
#         # print("[DEBUG] start_idx :", start_idx)
#         is_showed = [False for _ in range(gem_set_len)]
#         showed_cnt = 0
        
#         for i in range(start_idx, min(start_idx + min_len, gems_cnt)):
            
#             cur_gem = gems[i]
#             cur_gem_id = gem_idx_map[cur_gem]
            
#             if is_showed[cur_gem_id]:
#                 continue
            
#             is_showed[cur_gem_id] = True
#             showed_cnt += 1
            
#             if showed_cnt == gem_set_len:
#                 new_len = i - start_idx + 1
#                 # print(f"[DEBUG] start_idx :{start_idx}, new_len : {new_len}, min_len : {min_len}")
                
#                 if new_len < min_len:
#                     min_len = new_len
#                     min_range = [start_idx+1, i+1]
#                 break
#     return min_range
        
            
    
        