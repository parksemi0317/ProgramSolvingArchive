import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
paper = []

paper_cnt = [0,0]

for _ in range(N):
    paper.append(list(map(int, input().rstrip().split())))

def isAllSameColor(start_x, start_y, size):
    global paper, paper_cnt
    color = paper[start_x][start_y]

    for x in range(start_x, start_x + size):
        for y in range(start_y, start_y + size):
            if paper[x][y] != color:
                return 0
    paper_cnt[color] += 1
    return 1


def cutPaper(start_x, start_y, size):
    
    # 전부 같은 색상인 경우 반환
    if isAllSameColor(start_x, start_y, size):
        return
    else:
        cutPaper(start_x, start_y, size //2)
        cutPaper(start_x, start_y+size//2, size//2)
        cutPaper(start_x+size//2 , start_y, size//2)
        cutPaper(start_x+size//2, start_y + size//2, size//2)

cutPaper(0, 0, N)

print(f"{paper_cnt[0]}\n{paper_cnt[1]}")