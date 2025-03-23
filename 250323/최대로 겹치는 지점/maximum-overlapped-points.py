n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

empty = [0] * 100

for a, b in segments:
    for i in range(a,b+1):
        empty[i] += 1


max_num = max(empty)

print(max_num)