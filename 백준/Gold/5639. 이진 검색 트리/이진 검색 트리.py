import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
print = sys.stdout.write

arr = []

while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break


def printConverted(root, len):
    global arr

    if len == 1:
        print(F"{arr[root]}\n")
        return
    
    i = 1

    while i < len and arr[root+i] < arr[root]:
        i+=1
    
    if i-1 > 0:
        printConverted(root+1, i-1)
    if len - i > 0:
        printConverted(root+i, len - i)
    print(F"{arr[root]}\n")

printConverted(0, len(arr))

    