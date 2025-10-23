import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

def printArr(arr):
    for n in arr:
        print(f"{n} ")
    print("\n")

def searchArr(arr, current_len, max_num):

    #print(f"\n[Debug] searchArr({arr}, {current_len}, {max_num})\n")
    global M, N
    if current_len == M:
        printArr(arr)
        return

    for i in range(max_num+1, N+1):
        new_arr = arr.copy()
        new_arr.append(i)
        searchArr(new_arr, current_len+1, i)

searchArr([], 0, 0)