from collections import defaultdict

n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

visited = defaultdict(int)
pos = 0

for amount, direction in zip(x, dir):

    old_pos = pos

    if direction == "L":
        pos = old_pos - amount
        for i in range(pos, old_pos):
            visited[i] += 1

    if direction == "R":
        pos = old_pos + amount
        for i in range(old_pos, pos):
            visited[i] += 1



cnt = 0
for visit in visited.values():
    if visit >= 2:
        cnt += 1

print(cnt)