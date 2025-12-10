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

# =============== 


haveToFill = []
haveToFillLen = 0

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

# printSdoque()
# printMasks()

def backTrack(fillIdx):
    global row, col, box, haveToFill, haveToFillLen

    if fillIdx == haveToFillLen:
        printSdoque()
        return 1
    
    i, j = haveToFill[fillIdx]

    bitMask = row[i] | col[j] | box[(i // 3)*3 + j // 3]

    if bitMask == 2**9-1:
        return -1

    for num in range(1, 10):
        impossible = bitMask & ( 1 << (num-1))
        bit = 1 << (num-1)
        if not impossible:
            temp = (row[i], col[j], box[(i // 3)*3 + j // 3])
            row[i] |= bit
            col[j] |= bit
            box[(i // 3)*3 + j // 3] |= bit
            sdoque[i][j] = num

            if backTrack(fillIdx+1) == 1:
                return 1
            else:
                row[i], col[j], box[(i // 3)*3 + j // 3] = temp
        
backTrack(0)         
            
        
    
    
