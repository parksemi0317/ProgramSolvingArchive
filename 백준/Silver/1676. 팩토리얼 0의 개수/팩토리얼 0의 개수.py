N = int(input())

factN = 1
for n in range(2, N+1):
    factN *= n

# print(factN)

strN = list(str(factN))
strN.reverse()

cnt = 0
for c in strN:
    if c != '0':
        break
    cnt+=1
print(cnt)