import sys

print = sys.stdout.write


# ============ 값 입력 받기 ============
S = input()

# ============ 팰린드롬 만족 여부 dp 구하기 ============

N = len(S)

# isPalindrome[시작 인덱스][길이]
# 길이가 0또는  1인경우는 True
isPalindrome = [[True if e <= s else False for e in range(s-1, N)] for s in range(N)]
    
# 2이상인 경우 팰린드롬 여부 확인
for len in range(2, N+1):
     for s in range(0, N - len+1):
         if isPalindrome[s+1][len-2] and S[s] == S[s+len-1]:
                isPalindrome[s][len] = True

# ===== 디버깅용 출력 함수 =====
# 펠린드롬 여부 배열 출력 함수
def printIsPalin():
    for line in isPalindrome:
        for tf in line:
            print(f"{'1' if tf else '0'} ")
        print("\n")
    print("\n")


# 전체 팰린드롬 목록 출력 함수
def printPalinLists():
    for s in range(N):
        for len in range(1, N-s+1):
            if isPalindrome[s][len]:
                print(f"{S[s: s+len]}\n")


# ============ 팰린드롬 분할 dp 구하기 ============
palinDivCnt = [ i for i in range(N+1)] # 특정 길이까지의 최소 팰린드롬 분할 수 

for len in range(2, N+1):

    for newPalLen in range(1, len+1):
        if isPalindrome[len-newPalLen][newPalLen]:
            palinDivCnt[len] = min(palinDivCnt[len], palinDivCnt[len-newPalLen] + 1)
# print(F"palinDivCnt : {palinDivCnt}\n")
print(F"{palinDivCnt[N]}")