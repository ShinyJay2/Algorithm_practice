K, N = map(int, input().split())

# Please write your code here.

# we need a recursive function

def dfs(comb):

    if len(comb) == N:
        print(*comb)
        return

    for i in range(1, K+1):
        if len(comb) >= 2 and comb[-1] == comb[-2] == i:
            continue

        comb.append(i)
        dfs(comb)
        comb.pop()


dfs([])


