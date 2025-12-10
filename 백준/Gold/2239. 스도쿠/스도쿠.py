import sys

input = sys.stdin.readline
print = sys.stdout.write

sdoque = []

for _ in range(9):
    sdoque.append(list(map(int, input().rstrip())))


    
row = [0 for _ in range(9)]
col = [0 for _ in range(9)]
box = [0 for _ in range(9)]

# =============== 출력 함수
def printSdoque():
    global sdoque
    for line in sdoque:
        for c in line:
            print(f"{c}")
        print("\n")
    print("\n")

def printMask(mask):
    for c in mask:
        print(f"{format(c, 'b')}".rjust(11))
    print("\n")
    
def printMasks():
    global row, col, box

    print(f"row : ")
    printMask(row)
    print(f"col : ")
    printMask(col)
    print(f"box : ")
    printMask(box)

# =============== 가로세로박스 비트 마스크 & 빈 박스 목록 값 설정

haveToFill = [] # 빈 박스 목록
haveToFillLen = 0 # 빈 박스 수

for i in range(9):
    for j in range(9):
        if sdoque[i][j] == 0:
            haveToFill.append((i, j))
            haveToFillLen += 1
        else:

            bit = 1 << (sdoque[i][j]-1)
            row[i] |= bit
            col[j] |= bit
            
            bi = i // 3
            bj = j // 3
            box[bi * 3 + bj] |= bit

# =============== 탐색

def backTrack(fillIdx):
    global row, col, box, haveToFill, haveToFillLen

    # 끝까지 도달한 경우
    if fillIdx == haveToFillLen:
        printSdoque()
        return 1
    
    i, j = haveToFill[fillIdx]

    bitMask = row[i] | col[j] | box[(i // 3)*3 + j // 3]

    if bitMask == 2**9-1:
        return -1

    for num in range(1, 10):
        impossible = bitMask & ( 1 << (num-1)) # num 값 삽입 가능 여부 확인
        
        if not impossible:
            bit = 1 << (num-1) # num 값에 해당하는 bit 값
            
            temp = (row[i], col[j], box[(i // 3)*3 + j // 3]) # 값 임시 저장 (되돌리기 위함)
            # 가로 세로 박스 비트 마스크 & 스토쿠 값 설정
            row[i] |= bit
            col[j] |= bit
            box[(i // 3)*3 + j // 3] |= bit
            sdoque[i][j] = num

            if backTrack(fillIdx+1) == 1:
                # 재귀 호출한 함수에서 끝까지 도달한 경우
                # 더 탐색하지 않고 종료
                return 1
            else:
                # 이전 값으로 되돌림
                row[i], col[j], box[(i // 3)*3 + j // 3] = temp
        
backTrack(0)         
    
