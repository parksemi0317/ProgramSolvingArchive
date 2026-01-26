import sys

input = sys.stdin.readline
print = sys.stdout.write

BASE = ["***", "* *", "***"]


N = int(input().rstrip())
def drawBox(n):
    if n == 3:
        return BASE

    prevBox = drawBox(n//3)

    result = []

    # prevBox 3개
    for line in prevBox:
        newLine = line * 3
        result.append(newLine)

    # prevBox / 빈칸 / prevBox
    for line in prevBox:
        newLine = line + " " * len(line) + line
        result.append(newLine)

    # prevBox 3개
    for line in prevBox:
        newLine = line * 3
        result.append(newLine)
    return result

sol = drawBox(N)

for line in sol:
    for c in line:
        print(F"{c}")
    print("\n")