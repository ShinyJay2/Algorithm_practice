N, M = map(int, input().split())

num_list = [i for i in range(1, N+1)]


ans = []

# We need a dfs, maybe with a without used, leftover nums

def dfs(idx, choice_start):

    global ans # The case where we modify global structure, so need of backtracking implementation

    if idx == M:
        print(*ans)
        return

    # We need to decide the first, then call the next
    # The deciding number range is n
    for num in range(choice_start, N+1):
        ans.append(num)
        dfs(idx+1, num+1)
        ans.pop()


dfs(0, 1)


