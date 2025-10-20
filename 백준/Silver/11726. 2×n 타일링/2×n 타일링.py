n = int(input())

def factorial(num):
    result =1
    for i in range(2, num+1):
        result *= i
    return result

result = 0

for k in range(n//2 + 1):
    temp = factorial(n-k) // (factorial(k) * factorial(n-2*k))
    result += temp % 10007
    result %= 10007
print(result)