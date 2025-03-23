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
        new_pos = old_pos - amount
        step = -1

    if direction == "R":
        new_pos = old_pos + amount
        step = 1

    for i in range(old_pos, new_pos, step):
        visited[i] += 1
    
    pos = new_pos


cnt = 0
for visit in visited.values():
    if visit >= 2:
        cnt += 1

print(cnt)