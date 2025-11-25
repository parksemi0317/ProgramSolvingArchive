import sys
INF = 10001 * 2500

input = sys.stdin.readline
print = sys.stdout.write

TC = int(input().rstrip())

## ========= 디버깅용 출력 함수

def printDists(dists):
    for i in dists:
        print(F"{'-INF' if i <= -INF else ('INF' if i >= INF else i)}".ljust(5))
    print("\n")

def printEdges(edges, N):
    for i in range(1, N+1):
        print(f"[DEBUG] edges[{i}] : {edges[i]}\n")

## =========


def solve():
    ## ========= 주요 정보 입력 받기
    N, M, W = map(int, input().rstrip().split())

    edges = {}
    for i in range(1, N+1):
        edges[i] = []

    # 도로 정보
    for i in range(M):
        s, e, t = map(int, input().rstrip().split())
        edges[s].append((e, t))
        edges[e].append((s, t))

    # 웜홀 정보
    starts = []
    for _ in range(W):
        s, e, t = map(int, input().rstrip().split())
        edges[s].append((e, -t))
        starts.append(s)
    # printEdges(edges, N)

    # print(f"[DEBUG] starts : {starts}\n")

    
    ## ========= 각 정점에서의 최단 거리 구하기
    for start in set(starts):
        
        dists = [INF for i in range(N)]
        dists[start-1] = 0
        # print(f"[DEBUG] 시작 위치 {start} 에서 각 정점까지의 최단 거리\n")
        
        for iter in range(N-1):
            # printDists(dists)
            
            for mid in range(1, N+1):
                if dists[mid-1] < INF:
                    for e, t in edges[mid]:
                        dists[e-1] = min(dists[e-1], dists[mid-1] + t)
        
        # printDists(dists)
        
        # 음의 사이클 존재 여부 확인
        for mid in range(1, N+1):
            if dists[mid-1] < INF:
                for e, t in edges[mid]:
                    if e == start and dists[e-1] > dists[mid-1] + t:
                        # print(f"[DEBUG] dists[{e-1}] > dists[{mid-1}] + {t}\n")
                        print("YES\n")
                        return

        if dists[start-1] < 0:
            print("YES\n")
            return
    print("NO\n")


for tc in range(TC):
    # print(f"\n\n\n======== [DEBUG] tc : {tc} ========\n")
    solve()
