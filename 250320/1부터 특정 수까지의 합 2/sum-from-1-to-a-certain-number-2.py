N = int(input())

def function1(n):

    if n == 0:
        return 0

    return function1(n-1) + n


print(function1(N))