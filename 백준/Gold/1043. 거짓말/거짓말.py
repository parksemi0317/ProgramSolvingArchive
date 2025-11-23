import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# ========= N, M 입력 받기
N, M = map(int, input().rstrip().split())

# print(F"[DEBUG] N :{N}, M : {M}\n")

# ========= 진실을 아는 사람 입력 받기
know_truth = list(map(int, input().rstrip().split()))[1 :]
dp_kt = [0 for _ in range(N)] # 큐에 삽입되었는지 여부

for p in know_truth:
    dp_kt[p-1] = 1
    
# print(F"[DEBUG] dp_kt :{dp_kt}\n")

know_truth = deque(know_truth) # 큐

# ========= 파티에 오는 사람 정보 입력 받기

peoples  = []

for _ in range(M):
    peoples.append(list(map(int, input().rstrip().split()))[1:])

'''
print(F"[DEBUG] peoples : \n")
for temp in peoples:
    print(F"{temp}\n")
'''
# =========

cant_lie = [0 for _ in range(M)]
while know_truth:
    # print(F"\n[DEBUG] know_truth :{know_truth}\n")
    
    p = know_truth.popleft()
    # print(F"[DEBUG] p :{p}\n")
    
    for party_idx in range(M):
        if cant_lie[party_idx] == 0 and p in peoples[party_idx]:
            # print(f"[DEBUG] party_idx : {party_idx}\n")
            
            cant_lie[party_idx] = 1
            
            for people in peoples[party_idx]:
                if dp_kt[people-1] == 0:
                    know_truth.append(people)
                    dp_kt[people-1] = 1
    # print(F"[DEBUG] cant_lie :{cant_lie}\n")

# print(F"[DEBUG] cant_lie :{cant_lie}\n")
print(f"{cant_lie.count(0)}")
    