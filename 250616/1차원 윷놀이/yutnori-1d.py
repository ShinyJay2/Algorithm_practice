n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# What about making a dictionary of the k pawns
pawns = dict()
for i in range(k):
    pawns[i] = 0


best = 0

def dfs(idx, score):

    global best, pawns

    if idx == n:
        best = max(best, score)
        return 

    # nums's order must be given to k pawns
    # If above 6, call other?

    for pawn in pawns:

        if pawns[pawn] >= m:
            continue

        old_pos = pawns[pawn]
        new_pos = old_pos + nums[idx]

        if new_pos >= m:
            pawns[pawn] = m
            dfs(idx+1, score+1)
        else:
            pawns[pawn] = new_pos
            dfs(idx+1, score)

        pawns[pawn] = old_pos

dfs(0, 0)
print(best)





