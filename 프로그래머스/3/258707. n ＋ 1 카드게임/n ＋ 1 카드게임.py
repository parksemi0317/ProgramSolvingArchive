from collections import deque

def solution(coin, cards):
    # ========== 초기 값 세팅
    n = len(cards)
    
     # 1 : 소유, 0 : 미소유, -1 : 제출, 2 : 사용 가능
    curCard = [0 for _ in range(n+1)]
    
    # 초기에 들고 있는 카드 소유로 세팅
    for c in cards[:n//3]: 
        curCard[c] = 1
        
    canUse= deque([])
    cardDeck = deque(cards[n//3:])
    curRound = 1
    
    # ========== 유틸 함수
    
    # 두개의 카드를 덱에서 빼는 함수
    # canUse에 추가하고, curCard값을 2(사용 가능)로 둠
    def addTwoCard():
        nonlocal canUse, cardDeck
        for i in range(2):
            if not cardDeck:
                return False
            c = cardDeck.popleft()
            canUse.append(c)
            curCard[c] = 2
        return True
    
    def payTwoCard(c1, c2):
        nonlocal curCard, curRound
        curCard[c1] = -1
        curCard[c2] = -1
        curRound += 1
    
    # 디버깅용 출력 함수    
#     def debug():
#         nonlocal curCard
#         print("소유중 :", end="")
#         for i in range(1, n+1):
#             if curCard[i] == 1:
#                 print(i, end=" ")
#         print()
        
#         print("사용 가능 :", end="")
#         for i in range(1, n+1):
#             if curCard[i] == 2:
#                 print(i, end=" ")
#         print()
        
    # ========== coin 사용하지 않고 초기 카드로 처리 가능한 경우 구하기
    
    addTwoCard()
    for i in range(1, n+1):
        if curCard[i] == 1 and curCard[n+1-i] == 1:
            payTwoCard(i, n+1-i)
            
            if not addTwoCard(): # 더이상 새로 뽑을 카드가 없는 경우
                return curRound # 종료
    # debug()
    
    # ========== coin 사용
    
    while coin > 0:
        # print("[DEBUG][while 1]")
        # debug()
        
        needTwo = deque([])
        
        # 하나로 처리 가능한 경우 확인하기
        while canUse and coin > 0:
            c = canUse.popleft()
            if curCard[c] !=2:
                continue
            #  print("\t[DEBUG] c:", c, "curCard :", curCard)
            pair = n+1-c
            if curCard[pair] == 1: # 하나로 처리 가능한 경우
                # print(f"  useCoin 1 - {c} & {pair}")
                coin -= 1
                payTwoCard(c, pair)
                
                if not addTwoCard():
                    return curRound
                continue
            else: # needTwo
                needTwo.append(c)
                
        if coin < 2:
            # print("[DEBUG][RETURN CASE 1]")
            return curRound
        
        # debug()
        flag = 0
        # print("[DEBUG] needTwo : ", needTwo)
        while needTwo: # 하나로 처리 가능한 케이스가 없는 경우
            c = needTwo.popleft()
            if curCard[c] !=2:
                continue
                    
            pair = n+1-c
            if curCard[pair] == 2:
                # print(f"useCoin 2- {c} & {pair}")
                coin -= 2
                canUse += needTwo
                flag = 1
                payTwoCard(pair, c)
                
                if not addTwoCard():
                    return curRound
                break
        if flag == 0:
            return curRound

    return curRound
    
    