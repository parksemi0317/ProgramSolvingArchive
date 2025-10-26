import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))
arr.sort()

result = []

def printArr(arr):
    global M

    for i in range(M):
        print(f"{arr[i]} ")
    print("\n")

def selectNum(is_selected,selected_arr, leftNum):
    global N, arr
    
    if leftNum == 0:
        printArr(selected_arr)
        return

    for i in range(N):
        if is_selected[i] == 0:
            new_selected_arr = selected_arr.copy()
            new_selected_arr.append(arr[i])
            new_is_selected = is_selected.copy()
            new_is_selected[i] = 1
            selectNum(new_is_selected,new_selected_arr, leftNum-1)

for i in range(N):
    selectNum([ 1 if i == j else 0 for j in range(N)],[arr[i]], M-1)

