n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# What about making a dictionary of the k pawns
pawns = dict()
for i in range(k):
    pawns[i] = 1


best = 0

def dfs(move_idx, score):

    global best, pawns

    if move_idx == n:
        best = max(best, score)
        return 

    

    # nums's order must be given to k pawns
    # If above 6, call other?

    can_move = False

    for pawn in pawns:

        if pawns[pawn] >= m:
            continue

        old_pos = pawns[pawn]
        new_pos = old_pos + nums[move_idx]

        can_move = True

        if new_pos >= m:
            pawns[pawn] = m
            dfs(move_idx+1, score+1)
        else:
            pawns[pawn] = new_pos
            dfs(move_idx+1, score)

        pawns[pawn] = old_pos


    # We still have to recurse to the end_command to reach the base terminal condition, for the best score to update.
    if not can_move:
        dfs(move_idx+1, score)

dfs(0, 0)
print(best)





