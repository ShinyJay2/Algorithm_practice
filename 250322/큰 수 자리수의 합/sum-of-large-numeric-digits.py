a, b, c = map(int, input().split())

# "각 자리 수의 합을 구하는 함수" 가 우리의 재귀함수이다

def function1(n):

    if n < 10:
        return n 

    return function1(n // 10) + (n % 10)

tmp = a * b * c

print(function1(tmp))
