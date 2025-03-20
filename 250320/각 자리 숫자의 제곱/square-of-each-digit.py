N = int(input())

def function1(n):

    if n < 10:
        return n**2

    return function1(n // 10) + (n % 10)**2


print(function1(N))