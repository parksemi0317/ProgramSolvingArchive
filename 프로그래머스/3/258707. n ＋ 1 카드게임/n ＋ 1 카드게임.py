from collections import deque

def solution(coin, cards):
    # ========== 초기 값 세팅
    n = len(cards)
    deck = deque(cards[n//3:])
     # 1 : 소유, 0 : 미소유, -1 : 제출, 2 : 가져올 수 있음
    cardStates = [0 for _ in range(n+1)]
    
    result = 1
    useOneCoinPair = 0 # 코인 1개만 내면 되는 경우
    useTwoCoinPair = 0 # 코인 2개만 내면 되는 경우
    # ========= 유틸 함수
    def getTwoNewCard():
        nonlocal cardStates, cards, useOneCoinPair, useTwoCoinPair
        
        for i in range(2):
            if not deck:
                return False
            
            newCard = deck.popleft()
            print("newCard :", newCard, end="")
            pair = n+1-newCard
            
            cardStates[newCard] = 2
            if cardStates[pair] == 1:
                useOneCoinPair += 1
                print("=> useOneCoinPair+1", useOneCoinPair,end="")
            elif cardStates[pair] == 2:
                useTwoCoinPair += 1
                print("=> useTwoCoinPair+1", useTwoCoinPair,end="")
            print()
        return True
    # ========= 초기에 들고 있는 카드 처리
    
    # 초기에 들고 있는 카드 소유로 세팅
    # 짝을 지어 낼 수 있는 경우 내기
    for i in range(n//3):
        c = cards[i]
        cardStates[c] = 1
        
        pair = n+1-c
        if cardStates[pair] == 1: # 짝을 지어 낼 수 있는 경우
            cardStates[pair] = -1
            cardStates[c] = -1
            
            result += 1
    # 초기 진행된 라운드 수 만큼 덱에서 카드 가져오기
    for i in range(result):
        if not getTwoNewCard():
            return result
    
    # ========= 코인을 내서 처리하는 경우 체크
    while coin > 0:
        # 코인 1개만 내면 되는 경우 모두 처리
        while coin > 0 and useOneCoinPair > 0:
            result += 1
            useOneCoinPair -= 1
            coin -= 1
            
            if not getTwoNewCard(): # 새로운 카드 두 장 가져오기
                return result
            
        # 코인 2개 내면 되는 경우 처리 (1번만, 하나 발견 되면 다시 1개만 내도 되는 경우 처리)
        if coin >= 2 and useTwoCoinPair >0:
            result += 1
            useTwoCoinPair -= 1
            coin -= 2
            
            if not getTwoNewCard(): # 새로운 카드 두 장 가져오기
                return result
        else: # 2개 내도 안되는 경우 종료
            return result
    return result
        
    