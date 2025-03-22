N = int(input())


# N번째 항을 구하는 함수를 재귀함수로 놓자

def function1(n):

    if n == 1:
        return 2
    if n == 2:
        return 4

    return function1(n-2) * function1(n-1) % 100


print(function1(N))