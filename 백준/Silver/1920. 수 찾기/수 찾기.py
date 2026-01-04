n = int(input())
nArr = list(map(int, input().split()))

nArr.sort()

def hasNum(num):
    left = 0
    right = n-1
    while(left <= right):
        mid = (left+right)//2
        if nArr[mid] == num:
            return 1
        elif nArr[mid] > num:
            right = mid-1
        else:
            left = mid+1
    return 0

m = int(input())
mArr=list(map(int, input().split()))

for num in mArr:
    print(hasNum(num))