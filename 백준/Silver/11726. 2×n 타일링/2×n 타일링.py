n = int(input())

def factorial(num):
    result =1
    for i in range(2, num+1):
        result *= i
    return result

def aCb(a, b):
    result = 1
    for i in range(b):
        result *= a
        a-=1
    return result // factorial(b)

result = 0

for k in range(n//2 + 1):
    result += aCb(n-k, k)
    result %= 10007
print(result)