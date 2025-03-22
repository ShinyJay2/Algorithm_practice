n = int(input())

# "N을 2로 나누고 3을 곱하고 하는 함수" 가 우리의 재귀함수

def function1(n, cnt=0):

    if n == 1:
        return cnt


    if n % 2 == 1:
        return function1(n*3 + 1, cnt + 1)
    else:
        return function1(n // 2, cnt + 1)

print(function1(n, 0))
