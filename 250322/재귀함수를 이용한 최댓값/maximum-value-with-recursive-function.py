n = int(input())  #숫자 배열의 길이
arr = list(map(int, input().split()))  #실제 배열

# "N개의 원소 중 최댓값을 구하는 함수" 가 우리의 재귀함수이다

def get_maximum(n):

    tmp = []

    if n == 1:
        return arr[0]

    for i in range(n):
        tmp.append(arr[i])

    MAX = max(tmp)

    return max(get_maximum(n-1), MAX)


print(get_maximum(n))
