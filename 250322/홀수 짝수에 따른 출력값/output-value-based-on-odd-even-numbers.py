N = int(input())

# "N까지의 합을 출력하는 함수" 가 우리의 재귀함수이다

def function1(n):

    if n == 1:
        return 1

    if n == 2 and n % 2 == 0:
        return 2

    return function1(n-2) + n 


print(function1(N))