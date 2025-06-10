n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Record bomb position we don't do two bombs, but many can be possible

bombs = [(w, h) for w in range(n) for h in range(n) if grid[w][h] == 1]

# Precompute damage
# Compute coordinate like dy, dy, with new x and new y
# total_damage = a list of several list, first list first bomb second list second bomb.
# Each list contains 3 sets, each for the 3 different bomb type.

total_damage = []

for (w, h) in bombs:

    # Type 1 bomb
    b1 = set()
    for i in range(-2, 3):
        nw, nh = w + i, h
        if 0 <= nw < n:
            b1.add((nw, nh))

    # Type 2 bomb
    b2 = {(w, h)}
    for dx, dy in [(0,1), (1,0), (0, -1), (-1,0)]:
        nw, nh = w + dx, h + dy
        if 0 <= nw < n and 0 <= nh < n:
            b2.add((nw, nh))

    # Type 3 bomb
    b3 = {(w, h)}
    for dx, dy in [(-1,1), (-1,-1), (1,1), (1,-1)]:
        nw, nh = w + dx, h + dy
        if 0 <= nw < n and 0 <= nh < n:
            b3.add((nw, nh))

    total_damage.append([b1, b2, b3])

# dfs

max_dmg = 0

def dfs(order, exploded):

    global max_dmg

    # We need a terminal condition.
    if order == len(bombs):
        max_dmg = max(max_dmg, len(exploded))
        return 

    # In the function, we try all 3 bombs
    # so every bomb is a list of [b1, b2, b3] and we just choose the bomb with the second index
    for i in range(3):
        dfs(order+1, exploded.union(total_damage[order][i]))

    return

dfs(0, set())
print(max_dmg)



