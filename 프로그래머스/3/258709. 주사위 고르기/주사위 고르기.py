import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10**6)

def solution(dice):
    dice_cnt = len(dice)
    # ========= 가능 케이스 구하기
    cases = []
    
    def getCase(cur, cur_idx, cur_cnt, dice_cnt):
        if  cur_cnt == dice_cnt // 2:
            cases.append(cur)
            return
        
        if dice_cnt - cur_idx + cur_cnt < (dice_cnt // 2) : # 가지치기
            return 
        getCase(cur, cur_idx+1, cur_cnt, dice_cnt)
        
        new_cur = cur[ : cur_idx] + [1] + cur[cur_idx+1:]
        getCase(new_cur, cur_idx+1, cur_cnt + 1, dice_cnt)
    
    tmp = [0 for _ in range(dice_cnt)]
    tmp[0] = 1 # 절반 케이스만 보기 위해서
    
    getCase(tmp, 1, 1, dice_cnt)
    
    # ========= 각 케이스별 승률 확인
    
    # 특정 주사위 조합에서의 sum 모든 경우의 수 구하기
    def getSumCase(case_dices):
        q = deque([[0, 0]])
        result = []
        
        while q:
            cur_sum, cur_idx = q.popleft()
            
            if cur_idx == dice_cnt // 2:
                result.append(cur_sum)
                continue
            for d in case_dices[cur_idx]:
                q.append([cur_sum + d, cur_idx+1])
        return result
              
    # 특정 case의 승,패,무 확률 구하기
    def getProbabilty(c):
        # 현재 케이스의 a와 b주사위 나누기
        a = []
        b = []
        for i, d in enumerate(dice):
            if c[i] == 0:
                a.append(d)
            else:
                b.append(d)

        # a의 경우의 수 전부 구하기
        sumsA = getSumCase(a)
        sumsA.sort()
        # b의 경우의 수 전부 구하기
        sumsB = getSumCase(b)
        sumsB.sort()
        sumsBLen = len(sumsB)

        # 승률 정보 반환
        aWin = 0
        bWin = 0
        draw = 0
        for sumA in sumsA:
            l = bisect_left(sumsB, sumA)
            r = bisect_right(sumsB, sumA)
            
            if r==l: # draw없는 경우
                bWin += l 
                aWin += sumsBLen - l
            else: 
                draw += r-l
                bWin += l
                aWin += sumsBLen - l - (r-l)
            
        return (aWin, bWin, draw)

        
    prob = 0
    answer = []
    
    for c in cases:
        aWin, bWin, draw = getProbabilty(c)
        # print(c ,"=>", aWin, bWin, draw, aWin+bWin+draw)
        aProb = aWin / (aWin + bWin + draw)
        bProb = bWin / (aWin + bWin + draw)
        
        if aProb > prob:
            answer = []
            prob = aProb
            for i, tf in enumerate(c):
                if tf:
                    answer.append(i+1)
            
        if bProb > prob:
            answer = []
            prob = bProb
            for i, tf in enumerate(c):
                if not tf:
                    answer.append(i+1)
    return answer   