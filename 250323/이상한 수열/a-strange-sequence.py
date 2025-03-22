N = int(input())

# N번째 수를 구하는 함수를 재귀함수라고 하자

def function1(n):

    if n == 1:
        return 1
    if n == 2:
        return 2


    return function1(n // 3) + function1(n - 1)


print(function1(N))