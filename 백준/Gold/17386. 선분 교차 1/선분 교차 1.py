import sys

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)

def solution():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) > 0:
        return 0
    if ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) > 0:
        return 0
    return 1

print(solution())