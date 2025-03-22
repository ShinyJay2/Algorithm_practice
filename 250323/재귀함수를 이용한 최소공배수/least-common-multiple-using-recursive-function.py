n = int(input())
arr = list(map(int, input().split()))

# "N개의 수가 주어졌을 때 최소공배수 구하는 함수" 가 재귀함수
# 이전에 최소공배수 구하는 알고리즘을 하나 만들어놓자

tmp_arr = []

def lcm(a, b):
    gcd = 1
    goal = min(a, b)

    for i in range(2, goal+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    return gcd * (a // gcd) * (b // gcd)


def function1(n):

    if n == 1:
        return arr[0]

    for i in range(n):
        tmp_arr.append(arr[i])

    return lcm(function1(n-1), arr[n-1])

print(function1(n))


    