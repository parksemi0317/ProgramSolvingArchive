import sys

A, B = map(int, input().split())

# num 이하의 수에서 1이 나타나는 횟수 총 합
def getSum(num):
    # 예외 처리
    if num <= 0:
        return 0
    
    result = 0
    bitMask = 0b1

    # 낮은 자리수부터 각 자리수에 1이 등장하는 횟수 구하기
    # n번째 자리수는 2 ** n 개씩 반복되는 패턴을 가짐
    while bitMask <= num:
        leftCnts = (num + 1) % (2 * bitMask) # 반복 그룹에 묶이지 않는 숫자의 수
        result += (num + 1 - leftCnts) // 2 # 반복 그룹의 절반은 1이 존재

        if bitMask < leftCnts: # 반복 그룹에 묶이지 않는 숫자들에 1이 존재하는 경우 더하기
            result += leftCnts - bitMask
            
        bitMask = bitMask << 1
    return result

print(getSum(B) - getSum(A-1))