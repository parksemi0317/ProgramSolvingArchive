def solution(message, spoiler_ranges):
    # ============ message 단어별로 분리하기
    # 단어별 분리
    split_words = list(message.split())
    # print("[DEBUG] split_words : ", split_words)
    
    # 각 str idx의 단어 idx 구하기
    message_word_idx = []
    word_idx = 0
    for idx, c in enumerate(message):
        if c == ' ':
            message_word_idx.append(-1)
            word_idx +=1
        else:
            message_word_idx.append(word_idx)
    # print("[DEBUG] message_word_idx : ", message_word_idx)
    
    # ============ spoiler_ranges가공하기
    
    # 스포일러 단어인지 여부
    is_spoiler_words = [False for _ in range(word_idx + 1)]
    
    # 단어 idx로 변환된 spoiler_rages
    converted_spoiler_ranges = []
    for s, e in spoiler_ranges:
        start_word_idx = message_word_idx[s] if message_word_idx[s] != -1 else message_word_idx[s+1]
        end_word_idx = message_word_idx[e] if message_word_idx[e] != -1 else message_word_idx[e-1]
        
        for word_idx in range(start_word_idx,end_word_idx+1):
            is_spoiler_words[word_idx] = True
        converted_spoiler_ranges.append(list(range(start_word_idx, end_word_idx+1)))
    # print("[DEBUG] is_spoiler_words : ", is_spoiler_words)
    # print("[DEBUG] converted_spoiler_ranges : ", converted_spoiler_ranges)
    
    # ============ 스포 방지 구간이 
    # 스포 방지 구간이 아닌 단어 우선 추출
    non_spoilter_words_map = {} 
    for w_idx, word in enumerate(split_words):
        if not is_spoiler_words[w_idx]:
            non_spoilter_words_map[word] = True

    # 중요 단어 판별
    answer = 0
    
    for word_idxs in converted_spoiler_ranges:
        for word_idx in word_idxs:
            
            if not (split_words[word_idx] in non_spoilter_words_map):
                answer += 1
                non_spoilter_words_map[split_words[word_idx]] = True

    return answer