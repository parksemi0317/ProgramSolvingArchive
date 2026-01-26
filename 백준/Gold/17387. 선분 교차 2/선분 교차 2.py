import sys

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)

def solution():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    ccw1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    ccw2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if ccw1 > 0 or ccw2 > 0:
        return 0
    elif ccw1 == 0 and ccw2 == 0:
        # 두 선분이 한 직선 위에 있는 경우
        if x1 == x2 and x2 == x3 and x3 == x4:
            # x축과 평행한 경우 => y 값을 가지고 비교
            if (y1-y3)*(y2-y3) <= 0 or (y1-y4)*(y2-y4) <= 0 or (y3-y1)*(y4-y1) <= 0 or (y3-y2)*(y4-y2) <= 0:
                return 1
            return 0
                
        # x값을 통해 겹쳐있는지 확인
        if (x1-x3)*(x2-x3) <= 0 or (x1-x4)*(x2-x4) <= 0 or (x3-x1)*(x4-x1) <= 0 or (x3-x2)*(x4-x2) <= 0:
            return 1
        return 0
    else:  
        return 1

print(solution())