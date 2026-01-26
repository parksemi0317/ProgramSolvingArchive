import sys

input = sys.stdin.readline
print = sys.stdout.write

MAX = 0b11111111111111111111
bitMask = 0b0

N = int(input().rstrip())

def getMask(x):
    x = int(x)

    return 0b1 << (x-1)
    

for _ in range(N):
    ipt = list(input().rstrip().split())
    # print(f"{ipt} (bitMask : (${bin(bitMask)}) \n")
    opt = ipt[0]

    if opt == "add":
        # add
        bitMask =  bitMask | getMask(ipt[1])
        
    elif opt == "remove":
        # remove
        mask = getMask(ipt[1])

        bitMask = bitMask & (~mask)
    elif opt =="check":
        # check
        
        if bitMask & getMask(ipt[1]) != 0:
            print("1\n")
        else:
            print("0\n")
            
    elif opt == "toggle":
        # toggle
        
        bitMask = bitMask ^ getMask(ipt[1])
    elif opt == "all":
        bitMask = MAX        
    elif opt == "empty":
        # 비우기
        bitMask = 0b0
