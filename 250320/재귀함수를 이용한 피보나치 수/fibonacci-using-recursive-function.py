# Oh It's "THE" Fibonacci

N = int(input())


def fibonacci(n):

    if n == 1:
        return 1
    if n == 2:
        return 1


    #이전 두 항의 합이 그 다음 항

    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(N))