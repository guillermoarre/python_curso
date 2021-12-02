"""def factorial(n):
    fact = 1
    while n>= 1:
        fact = fact * n
        n-= 1
    return fact
print(factorial(6))"""

def factorial(n):
    if n == 0 or n== 1:
        return 1
    elif n>1:
        return n * factorial(n-1)
print(factorial(6))
