N = int(input())

def function1(n, cnt=0):

    if n == 1:
        return cnt

    

    if n % 2 == 0:
        return function1(n // 2, cnt+1)
    return function1(n // 3, cnt+1)


print(function1(N))





