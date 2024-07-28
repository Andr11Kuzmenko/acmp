import math

n = int(input())
n = math.factorial(n)

while n % 10 == 0:
    n //= 10

print(n % 10)
