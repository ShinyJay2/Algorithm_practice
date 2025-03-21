N = int(input())

# "어떤 수 n의 팩토리얼을 계산하는 함수" 가 재귀함수임

def factorial(n):

    if n == 0:
        return 1

    if n == 1:
        return 1

    return n * factorial(n-1)


print(factorial(N))