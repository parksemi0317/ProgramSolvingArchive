import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

result = set([])

def search(selected, is_selected, left):
    global arr, result
    
    if left == 0:
        result.add(tuple(selected))
    else:
        for i in range(N):
            if is_selected[i] == 0:
                new_arr = selected.copy()
                new_arr.append(arr[i])
                
                new_is_selected = is_selected.copy()
                new_is_selected[i] = 1
                
                search(new_arr,new_is_selected, left-1)

for i in range(N):
    search([arr[i]], [1 if i==j else 0 for j in range(N)], M-1)

result = list(result)

result.sort()

def printTup(tup):
    for i in tup:
        print(F"{i} ")
    print("\n")

for a in result:
    printTup(a)