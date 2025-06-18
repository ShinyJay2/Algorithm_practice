n = int(input())
num = list(map(int, input().split()))

# We need a move function

# then dfs function(current position)
# for loop with the possible jump length
# in each for loop we call the next dfs
# Do we have to backtrack anything? of course, when the dfs ends, cur_pos = old_pos


min_best = float('inf')

def dfs(cur_pos, jump):

    global min_best
    jump_range = num[cur_pos]

    # How do I do the if not possible case?
    # When there's a 0 in the num, or 

    if cur_pos == n-1:
        min_best = min(min_best, jump)
        return 

    if jump > min_best:
        return 

    if jump_range == 0:
        return 

    for each_jump in range(1, jump_range + 1):

        new_pos = cur_pos + each_jump
        if new_pos < n:
            dfs(new_pos, jump + 1)


dfs(0, 0)

if min_best == float('inf'):
    print(-1)
else:
    print(min_best)





    
