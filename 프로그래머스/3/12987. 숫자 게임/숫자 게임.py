from bisect import bisect_left

def solution(A, B):
    A_len = len(A)
    A.sort()
    B.sort()
    
    score = 0 # 결과 값
    for b in B:
        if A[score] < b:
            score += 1
            
            if score == A_len:
                break
    return score